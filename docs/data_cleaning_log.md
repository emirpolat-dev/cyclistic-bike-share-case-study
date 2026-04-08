# Data Cleaning Log

## Cleaning Actions
- Imported 12 monthly trip data files
- Standardized column names
- Combined files into one dataset
- Converted started_at and ended_at to datetime format
- Created ride_length_minutes
- Created day_of_week_num, day_of_week, month, month_name, hour, and season columns
- Removed rows with missing values in critical fields
- Removed duplicate ride_id values
- Removed rides with zero or negative duration
- Standardized member_casual and rideable_type values

## Final Cleaned Dataset
- Total rows: 5,620,515
- Members: 3,605,025
- Casual riders: 2,015,490

## Notes
- Very short and very long rides were retained in the cleaned dataset but filtered in selected analytical comparisons
- Filtered ride-length analysis used rides between 1 and 1440 minutes