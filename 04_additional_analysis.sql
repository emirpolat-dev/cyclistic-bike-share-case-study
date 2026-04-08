-- ============================================
-- Additional Analysis Queries
-- Cyclistic Bike-Share Case Study
-- ============================================

-- ============================================
-- 1. WINTER CASUAL ANALYSIS
-- Monthly average ride duration comparison
-- Shows gap narrowing in winter months
-- ============================================

SELECT 
    member_casual,
    SUBSTR(started_at, 1, 7) AS month,
    ROUND(AVG(ride_length), 1) AS avg_ride_length_min,
    COUNT(*) AS total_rides
FROM trips
GROUP BY member_casual, month
ORDER BY month, member_casual;


-- ============================================
-- 2. ROUND TRIP ANALYSIS  
-- Identifies rides starting and ending at same station
-- Casual riders are 4x more likely to take tours
-- ============================================

SELECT 
    member_casual,
    COUNT(*) AS total_rides,
    SUM(CASE WHEN start_station_name = end_station_name THEN 1 ELSE 0 END) AS round_trips,
    ROUND(SUM(CASE WHEN start_station_name = end_station_name THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS round_trip_pct
FROM trips
WHERE start_station_name IS NOT NULL AND end_station_name IS NOT NULL
GROUP BY member_casual;


-- ============================================
-- 3. WEEKDAY VS WEEKEND (NORMALIZED PER DAY)
-- Raw totals mislead because 5 weekdays vs 2 weekend days
-- Per-day normalization shows casual +49% on weekends
-- ============================================

SELECT 
    member_casual,
    CASE 
        WHEN day_of_week IN ('Saturday', 'Sunday') THEN 'Weekend'
        ELSE 'Weekday'
    END AS day_type,
    COUNT(*) AS total_rides,
    ROUND(AVG(ride_length), 1) AS avg_ride_length_min
FROM trips
GROUP BY member_casual, day_type
ORDER BY member_casual, day_type;


-- ============================================
-- 4. TOP CASUAL STATIONS (for targeted marketing)
-- Shows where to place conversion ads
-- ============================================

SELECT 
    member_casual,
    start_station_name,
    COUNT(*) AS total_rides
FROM trips
WHERE start_station_name IS NOT NULL
GROUP BY member_casual, start_station_name
ORDER BY total_rides DESC
LIMIT 20;


-- ============================================
-- 5. BIKE TYPE PREFERENCE BY RIDER TYPE
-- Both groups prefer electric (~65%) - no differentiator
-- ============================================

SELECT 
    member_casual,
    rideable_type,
    COUNT(*) AS total_rides,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY member_casual), 1) AS pct
FROM trips
GROUP BY member_casual, rideable_type
ORDER BY member_casual, total_rides DESC;
