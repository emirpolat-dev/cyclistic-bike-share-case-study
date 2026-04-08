-- Total row count
SELECT COUNT(*) AS total_rows
FROM cyclistic_trips;

-- Distinct rider types
SELECT member_casual, COUNT(*) AS ride_count
FROM cyclistic_trips
GROUP BY member_casual;

-- Distinct bike types
SELECT rideable_type, COUNT(*) AS ride_count
FROM cyclistic_trips
GROUP BY rideable_type
ORDER BY ride_count DESC;

-- Check for nulls in critical columns
SELECT
    SUM(CASE WHEN ride_id IS NULL THEN 1 ELSE 0 END) AS null_ride_id,
    SUM(CASE WHEN started_at IS NULL THEN 1 ELSE 0 END) AS null_started_at,
    SUM(CASE WHEN ended_at IS NULL THEN 1 ELSE 0 END) AS null_ended_at,
    SUM(CASE WHEN member_casual IS NULL THEN 1 ELSE 0 END) AS null_member_casual,
    SUM(CASE WHEN ride_length_minutes IS NULL THEN 1 ELSE 0 END) AS null_ride_length_minutes
FROM cyclistic_trips;

-- Check duplicate ride_id values
SELECT ride_id, COUNT(*) AS duplicate_count
FROM cyclistic_trips
GROUP BY ride_id
HAVING COUNT(*) > 1
LIMIT 20;

-- Min, max, avg ride length
SELECT
    MIN(ride_length_minutes) AS min_ride_length,
    MAX(ride_length_minutes) AS max_ride_length,
    AVG(ride_length_minutes) AS avg_ride_length
FROM cyclistic_trips;

-- Check month distribution
SELECT month, COUNT(*) AS ride_count
FROM cyclistic_trips
GROUP BY month
ORDER BY month;

-- Check weekday distribution
SELECT day_of_week, COUNT(*) AS ride_count
FROM cyclistic_trips
GROUP BY day_of_week
ORDER BY
    CASE day_of_week
        WHEN 'Monday' THEN 1
        WHEN 'Tuesday' THEN 2
        WHEN 'Wednesday' THEN 3
        WHEN 'Thursday' THEN 4
        WHEN 'Friday' THEN 5
        WHEN 'Saturday' THEN 6
        WHEN 'Sunday' THEN 7
    END;