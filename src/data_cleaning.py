import os
import glob
import pandas as pd


RAW_DATA_PATH = "data/raw/*-divvy-tripdata.csv"
OUTPUT_PATH = "data/cleaned/cyclistic_cleaned.csv"


def get_season(month: int) -> str:
    if month in [12, 1, 2]:
        return "Winter"
    if month in [3, 4, 5]:
        return "Spring"
    if month in [6, 7, 8]:
        return "Summer"
    return "Autumn"


def load_and_combine_csvs(file_pattern: str) -> pd.DataFrame:
    print(f"Using file pattern: {file_pattern}")
    file_list = sorted(glob.glob(file_pattern))
    print(f"Matched files count: {len(file_list)}")

    if not file_list:
        raise FileNotFoundError(f"No matching CSV files found for pattern: {file_pattern}")

    print("\nFiles to be loaded:")
    for file in file_list:
        print(f" - {file}")

    dataframes = []
    for file in file_list:
        print(f"Reading: {file}")
        df = pd.read_csv(file)
        dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)
    print(f"\nCombined shape: {combined_df.shape}")
    return combined_df


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.lower()
    return df


def convert_datetime_columns(df: pd.DataFrame) -> pd.DataFrame:
    df["started_at"] = pd.to_datetime(df["started_at"], errors="coerce")
    df["ended_at"] = pd.to_datetime(df["ended_at"], errors="coerce")
    return df


def create_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
    df["ride_length_minutes"] = (df["ended_at"] - df["started_at"]).dt.total_seconds() / 60

    day_map = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    df["day_of_week_num"] = df["started_at"].dt.weekday
    df["day_of_week"] = df["day_of_week_num"].map(day_map)
    df["month"] = df["started_at"].dt.month
    df["month_name"] = df["started_at"].dt.month_name()
    df["hour"] = df["started_at"].dt.hour
    df["season"] = df["month"].apply(lambda x: get_season(x) if pd.notnull(x) else None)

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    initial_rows = len(df)

    required_columns = [
        "ride_id",
        "rideable_type",
        "started_at",
        "ended_at",
        "member_casual"
    ]

    missing_required = [col for col in required_columns if col not in df.columns]
    if missing_required:
        raise ValueError(f"Missing required columns: {missing_required}")

    df = df.dropna(subset=["ride_id", "started_at", "ended_at", "member_casual"])
    df = df.drop_duplicates(subset=["ride_id"])

    df["member_casual"] = df["member_casual"].astype(str).str.strip().str.lower()
    df["rideable_type"] = df["rideable_type"].astype(str).str.strip().str.lower()

    df = df[df["member_casual"].isin(["member", "casual"])]
    df = df[df["ride_length_minutes"] > 0]

    final_rows = len(df)

    print(f"\nRows before cleaning: {initial_rows}")
    print(f"Rows after cleaning: {final_rows}")
    print(f"Removed rows: {initial_rows - final_rows}")

    return df


def reorder_columns(df: pd.DataFrame) -> pd.DataFrame:
    preferred_order = [
        "ride_id",
        "rideable_type",
        "started_at",
        "ended_at",
        "ride_length_minutes",
        "day_of_week_num",
        "day_of_week",
        "month",
        "month_name",
        "hour",
        "season",
        "start_station_name",
        "start_station_id",
        "end_station_name",
        "end_station_id",
        "start_lat",
        "start_lng",
        "end_lat",
        "end_lng",
        "member_casual"
    ]

    existing_columns = [col for col in preferred_order if col in df.columns]
    remaining_columns = [col for col in df.columns if col not in existing_columns]

    return df[existing_columns + remaining_columns]


def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")


def main() -> None:
    print("Script started...")
    df = load_and_combine_csvs(RAW_DATA_PATH)
    df = standardize_columns(df)
    df = convert_datetime_columns(df)
    df = create_derived_columns(df)
    df = clean_data(df)
    df = reorder_columns(df)

    print("\nDataset info:")
    print(df.info())

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMember vs Casual counts:")
    print(df["member_casual"].value_counts())

    save_cleaned_data(df, OUTPUT_PATH)
    print("Script finished successfully.")


if __name__ == "__main__":
    main()