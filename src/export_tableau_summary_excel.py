import os
import sqlite3
import pandas as pd

DB_PATH = "cyclistic.db"
OUTPUT_PATH = "data/summary/tableau_summary.xlsx"

QUERIES = {
    "kpi_total_rides": """
        SELECT COUNT(*) AS total_rides
        FROM cyclistic_trips;
    """,

    "kpi_rides_by_rider_type": """
        SELECT
            member_casual,
            COUNT(*) AS total_rides
        FROM cyclistic_trips
        GROUP BY member_casual
        ORDER BY total_rides DESC;
    """,

    "kpi_avg_ride_length_filtered": """
        SELECT
            member_casual,
            ROUND(AVG(ride_length_minutes), 2) AS avg_ride_length_minutes
        FROM cyclistic_trips
        WHERE ride_length_minutes BETWEEN 1 AND 1440
        GROUP BY member_casual
        ORDER BY member_casual;
    """,

    "rides_by_day": """
        SELECT
            day_of_week_num,
            day_of_week,
            member_casual,
            COUNT(*) AS total_rides
        FROM cyclistic_trips
        GROUP BY day_of_week_num, day_of_week, member_casual
        ORDER BY day_of_week_num, member_casual;
    """,

    "avg_ride_length_by_day": """
        SELECT
            day_of_week_num,
            day_of_week,
            member_casual,
            ROUND(AVG(ride_length_minutes), 2) AS avg_ride_length_minutes
        FROM cyclistic_trips
        WHERE ride_length_minutes BETWEEN 1 AND 1440
        GROUP BY day_of_week_num, day_of_week, member_casual
        ORDER BY day_of_week_num, member_casual;
    """,

    "rides_by_hour": """
        SELECT
            hour,
            member_casual,
            COUNT(*) AS total_rides
        FROM cyclistic_trips
        GROUP BY hour, member_casual
        ORDER BY hour, member_casual;
    """,

    "rides_by_month": """
        SELECT
            month,
            month_name,
            member_casual,
            COUNT(*) AS total_rides
        FROM cyclistic_trips
        GROUP BY month, month_name, member_casual
        ORDER BY month, member_casual;
    """,

    "rideable_type": """
        SELECT
            rideable_type,
            member_casual,
            COUNT(*) AS total_rides
        FROM cyclistic_trips
        GROUP BY rideable_type, member_casual
        ORDER BY rideable_type, total_rides DESC;
    """
}


def main():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database not found: {DB_PATH}")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
        for sheet_name, query in QUERIES.items():
            print(f"Exporting sheet: {sheet_name}")
            df = pd.read_sql_query(query, conn)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    conn.close()
    print(f"\nExcel summary file created: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()