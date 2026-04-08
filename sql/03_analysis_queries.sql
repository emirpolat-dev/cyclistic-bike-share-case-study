-- 1. Total rides by rider type
SELECT
    member_casual,
    COUNT(*) AS total_rides
FROM cyclistic_trips
GROUP BY member_casual
ORDER BY total_rides DESC;

-- 2. Average and median-like ride length by rider type
SELECT
    member_casual,
    COUNT(*) AS total_rides,
    ROUND(AVG(ride_length_minutes), 2) AS avg_ride_length_minutes,
    ROUND(MIN(ride_length_minutes), 2) AS min_ride_length_minutes,
    ROUND(MAX(ride_length_minutes), 2) AS max_ride_length_minutes
FROM cyclistic_trips
GROUP BY member_casual;

-- 3. Ride count by day of week and rider type
SELECT
    day_of_week,
    member_casual,
    COUNT(*) AS total_rides
FROM cyclistic_trips
GROUP BY day_of_week, member_casual
ORDER BY
    CASE day_of_week
        WHEN 'Monday' THEN 1
        WHEN 'Tuesday' THEN 2
        WHEN 'Wednesday' THEN 3
        WHEN 'Thursday' THEN 4
        WHEN 'Friday' THEN 5
        WHEN 'Saturday' THEN 6
        WHEN 'Sunday' THEN 7
    END,
    member_casual;

-- 4. Average ride length by day of week and rider type
SELECT
    day_of_week,
    member_casual,
    ROUND(AVG(ride_length_minutes), 2) AS avg_ride_length_minutes
FROM cyclistic_trips
GROUP BY day_of_week, member_casual
ORDER BY
    CASE day_of_week
        WHEN 'Monday' THEN 1
        WHEN 'Tuesday' THEN 2
        WHEN 'Wednesday' THEN 3
        WHEN 'Thursday' THEN 4
        WHEN 'Friday' THEN 5
        WHEN 'Saturday' THEN 6
        WHEN 'Sunday' THEN 7
    END,
    member_casual;

-- 5. Ride count by hour and rider type
SELECT
    hour,
    member_casual,
    COUNT(*) AS total_rides
FROM cyclistic_trips
GROUP BY hour, member_casual
ORDER BY hour, member_casual;

-- 6. Ride count by month and rider type
SELECT
    month,
    month_name,
    member_casual,
    COUNT(*) AS total_rides
FROM cyclistic_trips
GROUP BY month, month_name, member_casual
ORDER BY month, member_casual;

-- 7. Average ride length by month and rider type
SELECT
    month,
    month_name,
    member_casual,
    ROUND(AVG(ride_length_minutes), 2) AS avg_ride_length_minutes
FROM cyclistic_trips
GROUP BY month, month_name, member_casual
ORDER BY month, member_casual;

-- 8. Rideable type distribution by rider type
SELECT
    rideable_type,
    member_casual,
    COUNT(*) AS total_rides
FROM cyclistic_trips
GROUP BY rideable_type, member_casual
ORDER BY rideable_type, total_rides DESC;

-- 9. Top 10 start stations for casual riders
SELECT
    start_station_name,
    COUNT(*) AS total_rides
FROM cyclistic_trips
WHERE member_casual = 'casual'
  AND start_station_name IS NOT NULL
  AND start_station_name <> ''
GROUP BY start_station_name
ORDER BY total_rides DESC
LIMIT 10;

-- 10. Top 10 start stations for members
SELECT
    start_station_name,
    COUNT(*) AS total_rides
FROM cyclistic_trips
WHERE member_casual = 'member'
  AND start_station_name IS NOT NULL
  AND start_station_name <> ''
GROUP BY start_station_name
ORDER BY total_rides DESC
LIMIT 10;

-- 11. Seasonal distribution by rider type
SELECT
    season,
    member_casual,
    COUNT(*) AS total_rides
FROM cyclistic_trips
GROUP BY season, member_casual
ORDER BY season, member_casual;