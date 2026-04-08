import pandas as pd

CSV_PATH = "data/cleaned/cyclistic_cleaned.csv"

df = pd.read_csv(CSV_PATH)

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nRide length summary:")
print(df["ride_length_minutes"].describe())

print("\nTop 10 smallest ride lengths:")
print(df["ride_length_minutes"].nsmallest(10))

print("\nTop 10 largest ride lengths:")
print(df["ride_length_minutes"].nlargest(10))

print("\nSample rows:")
print(df[["ride_id", "started_at", "ended_at", "ride_length_minutes", "member_casual"]].head())