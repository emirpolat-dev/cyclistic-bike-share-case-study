import os
import sqlite3
import pandas as pd


CSV_PATH = "data/cleaned/cyclistic_cleaned.csv"
DB_PATH = "cyclistic.db"
TABLE_NAME = "cyclistic_trips"


def main():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV not found: {CSV_PATH}")

    print("Reading cleaned CSV...")
    df = pd.read_csv(CSV_PATH)

    print(f"CSV shape: {df.shape}")

    print("\nRide length summary from CSV:")
    print(df["ride_length_minutes"].describe())

    print("\nConnecting to SQLite...")
    conn = sqlite3.connect(DB_PATH)

    print(f"Writing table '{TABLE_NAME}' to database '{DB_PATH}'...")
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

    print("Creating indexes...")
    cursor = conn.cursor()
    cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_ride_id ON {TABLE_NAME}(ride_id);")
    cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_member_casual ON {TABLE_NAME}(member_casual);")
    cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_day_of_week ON {TABLE_NAME}(day_of_week);")
    cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_month ON {TABLE_NAME}(month);")
    cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_hour ON {TABLE_NAME}(hour);")
    conn.commit()

    print("\nValidation from SQLite:")

    row_count = pd.read_sql_query(
        f"SELECT COUNT(*) AS total_rows FROM {TABLE_NAME};", conn
    )
    print("\nRow count:")
    print(row_count)

    rider_counts = pd.read_sql_query(
        f"""
        SELECT member_casual, COUNT(*) AS ride_count
        FROM {TABLE_NAME}
        GROUP BY member_casual;
        """,
        conn
    )
    print("\nMember vs Casual:")
    print(rider_counts)

    ride_length_check = pd.read_sql_query(
        f"""
        SELECT
            MIN(ride_length_minutes) AS min_ride_length,
            MAX(ride_length_minutes) AS max_ride_length,
            AVG(ride_length_minutes) AS avg_ride_length
        FROM {TABLE_NAME};
        """,
        conn
    )
    print("\nRide length check:")
    print(ride_length_check)

    conn.close()
    print("\nSQLite load completed successfully.")


if __name__ == "__main__":
    main()