# Cyclistic Bike-Share Case Study Report

## 1. Executive Summary

This case study examines how Cyclistic annual members and casual riders use the bike-share service differently. The purpose of the analysis is to support Cyclistic’s business goal of increasing the number of annual memberships by identifying clear behavioral differences between the two rider segments. The main business question is how annual members and casual riders use Cyclistic bikes differently.

Using the previous 12 months of trip data, the analysis compares the two rider groups across total ride volume, ride duration, weekday behavior, hourly behavior, seasonal variation, and bike type preference. The results show that annual members generate more rides overall, while casual riders take longer rides on average. Members display a strong weekday and commute-like usage pattern, while casual riders are more active on weekends and during warmer months.

These findings suggest that Cyclistic should not position annual membership only as a commuter product. A stronger opportunity exists in targeting repeat casual users, especially those who ride on weekends and during high season, with membership messaging focused on value, flexibility, and frequent leisure use.

---

## 2. Business Task

Cyclistic wants to convert more casual riders into annual members. The business task of this analysis is to identify and explain the main behavioral differences between casual riders and annual members in order to support marketing strategies that increase annual memberships.

### Primary Business Question
How do annual members and casual riders use Cyclistic bikes differently?

### Why This Matters
Cyclistic’s finance analysts concluded that annual members are more profitable than casual riders. Because of that, understanding the behavioral gap between the two groups is necessary before designing campaigns aimed at conversion.

### Stakeholders
- Lily Moreno, Director of Marketing
- Cyclistic Marketing Analytics Team
- Cyclistic Executive Team

---

## 3. Data Source

This analysis uses Cyclistic historical bike trip data covering the previous 12 months, as instructed in the case study. The company scenario is fictional, but the trip data is publicly available and appropriate for answering the business question.

### Data Characteristics
The dataset contains ride-level trip data, including:
- Ride ID
- Bike type
- Start time
- End time
- Start station
- End station
- Rider type, member or casual

### Data Privacy Note
The dataset does not include personally identifiable information. Because of this limitation, the analysis focuses only on trip-level behavior and cannot identify individual user characteristics such as home location, income level, or repeated single-pass purchases.

### Data Scope Used in This Project
The working dataset used in this project covered 12 monthly trip files from April 2025 through March 2026, after correcting one file naming inconsistency in the downloaded archive and excluding older legacy Divvy files that used incompatible schemas.

---

## 4. Tools Used

The following tools were used in this project:

- **Python** for combining files, cleaning data, feature engineering, and exporting the cleaned dataset
- **Pandas** for data manipulation
- **SQLite** for query-based analysis
- **DB Browser for SQLite** for running and reviewing SQL queries
- **Tableau** for dashboard creation and final visualizations
- **GitHub** for project organization and portfolio presentation

### Why These Tools Were Chosen
Python was the most efficient tool for combining and cleaning multiple monthly CSV files. SQLite was used to perform structured analytical queries on the cleaned dataset. Tableau was selected for executive-facing visual communication.

---

## 5. Data Preparation and Cleaning

Before analysis, the monthly trip datasets were cleaned and transformed to ensure consistency and analytical usability.

### Cleaning Steps Performed
- Imported monthly trip data files
- Standardized column names across files
- Combined the monthly files into a single dataset
- Converted `started_at` and `ended_at` into datetime format
- Created `ride_length_minutes`
- Created derived columns:
  - `day_of_week_num`
  - `day_of_week`
  - `month`
  - `month_name`
  - `hour`
  - `season`
- Removed rows with missing values in critical fields such as `ride_id`, `started_at`, `ended_at`, and `member_casual`
- Removed duplicate `ride_id` records
- Removed rides with zero or negative duration
- Standardized `member_casual` and `rideable_type` values to lowercase text
- Restricted rider labels to valid categories: `member` and `casual`

### Result of Cleaning
- Total cleaned rows: **5,620,515**
- Rider type breakdown:
  - **member:** 3,605,025
  - **casual:** 2,015,490

### Data Quality Notes
The cleaned CSV showed a valid numerical distribution for ride length. However, the data still contained very short rides under one minute and very long rides above 24 hours. Because of that, both raw and filtered analyses were considered, and filtered ride-length comparisons used rides between 1 and 1440 minutes.

### Assumptions and Limitations
- Missing station values were not removed globally because they were not necessary for all parts of the analysis
- Trip purpose is inferred from behavior patterns, not directly recorded
- No customer-level linkage or demographic segmentation is available

---

## 6. Data Transformation

To make the dataset useful for business analysis, several new fields were created from the original datetime columns.

### Derived Features
- **ride_length_minutes**  
  Total trip duration in minutes

- **day_of_week_num**  
  Numeric day order used for proper weekday sorting

- **day_of_week**  
  Day name used to compare weekday and weekend behavior

- **month**  
  Numeric month used for chronological ordering

- **month_name**  
  Month label used in visuals and summaries

- **hour**  
  Hour of ride start used to detect daily usage patterns

- **season**  
  Seasonal grouping used to compare broad shifts in demand

### Why These Features Matter
These features make it possible to distinguish routine commute-like behavior from leisure-like behavior. Without them, the raw timestamps would provide little business value.

---

## 7. Analysis Approach

The analysis was designed to answer the business question through descriptive and comparative methods.

### Key Analytical Questions
1. Do casual riders and annual members differ in average ride duration?
2. Do they ride more often on different days of the week?
3. Do they use the service at different times of day?
4. Are there seasonal differences between rider types?
5. Do they prefer different bike types?

### Metrics Examined
- Total number of rides by rider type
- Average ride length by rider type
- Filtered average ride length by rider type
- Ride count by day of week and rider type
- Average ride length by day of week and rider type
- Ride count by hour and rider type
- Ride count by month and rider type
- Rideable type distribution by rider type

### Outlier Handling
Ride duration was analyzed in two ways:
1. Raw average ride length
2. Filtered average ride length using rides between 1 and 1440 minutes

This allowed the project to compare overall behavior while reducing distortion from unrealistic or extreme ride durations.

---

## 8. Summary of Analysis

The analysis found consistent and meaningful differences between annual members and casual riders.

### Finding 1
Annual members completed more total rides than casual riders.

- **member:** 3,605,025 rides
- **casual:** 2,015,490 rides

**Interpretation:**  
Annual members represent the core repeat-use segment of the service.

**Business Meaning:**  
Cyclistic already has a strong recurring user base. The opportunity is not to replace members, but to convert the most promising casual users into that recurring segment.

### Finding 2
Casual riders had significantly longer average ride durations than members.

Raw average ride length:
- **casual:** 22.59 minutes
- **member:** 12.43 minutes

Filtered average ride length:
- **casual:** 19.86 minutes
- **member:** 12.25 minutes

**Interpretation:**  
Even after removing extreme values, casual riders still take meaningfully longer rides.

**Business Meaning:**  
Casual users appear to use Cyclistic more for leisure, exploration, or longer discretionary trips, while members appear to use it more for shorter and more practical trips.

### Finding 3
Members were much stronger on weekdays, while casual riders increased sharply near the weekend.

Casual rides by day:
- Monday: 225,076
- Tuesday: 219,078
- Wednesday: 215,463
- Thursday: 249,482
- Friday: 301,588
- Saturday: 397,441
- Sunday: 323,153

Member rides by day:
- Monday: 501,306
- Tuesday: 569,680
- Wednesday: 551,713
- Thursday: 569,711
- Friday: 518,958
- Saturday: 441,219
- Sunday: 379,486

**Interpretation:**  
Members are more weekday-oriented, while casual riders are more weekend-oriented.

**Business Meaning:**  
This supports the idea that member behavior is tied more closely to routine mobility, while casual riders are more active during leisure periods.

### Finding 4
Casual riders not only rode more on weekends, but also rode longer on weekends.

Filtered average ride length by day for casual riders:
- Monday: 19.91
- Tuesday: 17.34
- Wednesday: 16.45
- Thursday: 17.39
- Friday: 19.42
- Saturday: 22.37
- Sunday: 23.02

Filtered average ride length by day for members:
- Monday: 11.95
- Tuesday: 11.84
- Wednesday: 11.75
- Thursday: 11.79
- Friday: 12.16
- Saturday: 13.41
- Sunday: 13.48

**Interpretation:**  
Weekend casual behavior is different in both frequency and duration.

**Business Meaning:**  
This is strong evidence that casual riders use Cyclistic differently from members, and that weekend-oriented campaigns are likely to be highly relevant.

### Finding 5
Member hourly behavior strongly resembled commuting patterns.

Examples of member ride peaks:
- 08:00: 261,786
- 16:00: 340,998
- 17:00: 388,598
- 18:00: 299,831

Casual riders were more spread across midday and afternoon periods.

**Interpretation:**  
Members use the system more like a transportation routine, especially during morning and post-work hours.

**Business Meaning:**  
Cyclistic should avoid assuming that casual riders can be converted with the same message that appears to fit members.

### Finding 6
Casual usage rose strongly in warmer months, while member usage remained more stable throughout the year.

Casual rider demand increased sharply from spring into summer and peaked during the warmer months. Member usage also increased seasonally, but the member segment remained more balanced across the year compared with casual riders.

**Interpretation:**  
Casual demand is highly seasonal.

**Business Meaning:**  
Conversion campaigns should be concentrated in high-engagement months rather than spread evenly across the year.

### Finding 7
Electric bikes were the most used bike type across both rider groups.

- member electric bike: 2,332,020
- member classic bike: 1,273,005
- casual electric bike: 1,346,888
- casual classic bike: 668,602

**Interpretation:**  
Electric bikes dominate usage for both segments.

**Business Meaning:**  
Membership messaging can include convenience and ease of use, since the most-used product format already aligns with that value proposition.

---

## 9. Visualizations and Key Findings

### Visualization 1: Total Rides by Rider Type
**Purpose:** Compare total usage volume between casual riders and annual members.  
**Key Takeaway:** Members generated substantially more rides overall and represent the core repeat-use segment.

### Visualization 2: Filtered Average Ride Length by Rider Type
**Purpose:** Compare average ride duration without extreme ride-length distortion.  
**Key Takeaway:** Casual riders take significantly longer trips than members.

### Visualization 3: Rides by Day of Week and Rider Type
**Purpose:** Compare weekday and weekend behavior between rider groups.  
**Key Takeaway:** Members are strongest during weekdays, while casual riders increase sharply on Fridays and peak on Saturdays.

### Visualization 4: Filtered Average Ride Length by Day of Week and Rider Type
**Purpose:** Compare how ride duration changes across the week.  
**Key Takeaway:** Casual rider trip length rises materially on weekends, especially Saturday and Sunday.

### Visualization 5: Rides by Hour of Day and Rider Type
**Purpose:** Compare time-of-day usage patterns.  
**Key Takeaway:** Members show distinct commute-like peaks in the morning and late afternoon, while casual riders are more dispersed across the day.

### Visualization 6: Rides by Month and Rider Type
**Purpose:** Detect seasonality and identify peak demand periods.  
**Key Takeaway:** Casual usage rises sharply during spring and summer, especially from May through August.

### Visualization 7: Rideable Type by Rider Type
**Purpose:** Support the analysis by comparing bike type preference across rider segments.  
**Key Takeaway:** Electric bikes are the dominant rideable type for both members and casual riders.

### Visualization Design Note
The final dashboard focused on the visuals most directly tied to the business question: ride volume, ride duration, weekday behavior, hourly behavior, and seasonality. Rideable type analysis was retained as a supporting insight rather than a primary dashboard visual.

---

## 10. Key Insights

### Insight 1
Annual members use Cyclistic more frequently, but casual riders use it for longer trips.

### Why It Matters
This shows that the two groups are not simply different in size. They use the product differently. Members appear to be the repeat routine segment, while casual users appear to engage in longer discretionary rides.

### Insight 2
Members show a clear weekday and commute-oriented pattern, while casual riders peak on weekends.

### Why It Matters
This suggests that conversion messaging aimed at casual users should not rely only on commuter benefits. Their behavior indicates a different use case and a different motivation structure.

### Insight 3
Casual rider activity increases sharply in warmer months.

### Why It Matters
Cyclistic should time conversion efforts when casual riders are already highly active. Campaign timing matters because demand is not evenly distributed across the year.

### Insight 4
Weekend casual rides are not only more frequent, but also longer.

### Why It Matters
This is strong evidence that leisure-oriented riders are a high-potential target for membership conversion if the offer is framed around repeated value rather than commute utility alone.

### Insight 5
Electric bikes dominate usage across both segments.

### Why It Matters
Convenience, ease, and low-friction mobility appear to matter broadly, which can strengthen future positioning.

---

## 11. Recommendations

### Recommendation 1: Build weekend-focused conversion campaigns for casual riders
The analysis shows that casual riders are especially active on Fridays, Saturdays, and Sundays, and that their weekend ride durations are longer than weekday rides.

Cyclistic should target these users with weekend-specific annual membership offers and messaging that emphasizes better value for frequent city rides, repeated leisure usage, and spontaneous mobility.

**Expected Benefit:**  
Higher conversion rates from casual riders who already demonstrate repeated high-engagement behavior during leisure periods.

### Recommendation 2: Concentrate conversion campaigns in peak seasonal months
Casual rider activity rises sharply from late spring into summer, especially between May and August.

Cyclistic should increase membership promotion intensity during these months through app messages, email campaigns, station signage, and limited-time offers.

**Expected Benefit:**  
Higher campaign efficiency by targeting casual riders when they are already using the service more often.

### Recommendation 3: Position membership as a lifestyle and value product, not only a commuter product
Members behave like routine transportation users, but casual riders behave differently. Their longer ride durations and weekend emphasis indicate that they are not primarily acting like commuters.

Cyclistic should frame annual membership as a smart option for regular city exploration, repeated weekend riding, and flexible everyday movement, not just weekday commuting.

**Expected Benefit:**  
Better alignment between customer behavior and message strategy, which should improve the likelihood of conversion.

---

## 12. Final Conclusion

This analysis identified clear behavioral differences between Cyclistic annual members and casual riders. Members generate more rides overall and appear to use the service in a more routine, commute-like way. Casual riders, by contrast, take longer rides, become more active on weekends, and show stronger seasonal growth during warmer months.

These findings provide a practical basis for targeted membership conversion strategies. Rather than promoting annual membership only as a commuter tool, Cyclistic should also market it as a high-value option for repeat leisure riders and weekend users. The strongest opportunities appear to be weekend-focused campaigns, summer conversion pushes, and messaging built around value for frequent discretionary use.

---

## 13. Limitations

This project has several important limitations:

- The dataset does not include personally identifiable customer information
- Trip purpose is inferred from patterns rather than directly recorded
- No demographic variables are available
- No campaign exposure or digital engagement data is available
- No customer-level purchase history is available
- Very short and very long rides required outlier handling to avoid distorted averages

These limitations mean the analysis is strong for descriptive pattern detection and strategy support, but it cannot prove rider motivation or establish causation.

---

## 14. Next Steps

To improve the analysis in the future, Cyclistic could:

- test membership offers targeted specifically at weekend casual riders
- run seasonal conversion campaigns and compare results across months
- add digital engagement data to measure response to campaign exposure
- segment casual riders further by ride frequency and ride duration
- compare one-time casual riders with repeated casual riders
- add station-level analysis to compare tourist and business-area usage
- isolate winter casual riders as a high-potential conversion segment
- build a predictive model for likelihood of conversion

---

## 15. Portfolio Reflection

This project demonstrates the ability to:
- translate a business question into an analytical framework
- combine and clean raw monthly operational data
- engineer useful analytical features from datetime fields
- perform comparative analysis using SQL
- identify meaningful behavioral differences between customer segments
- handle outliers appropriately when interpreting business metrics
- translate analysis into clear recommendations for stakeholders

This case study is suitable for a data analytics portfolio because it combines business framing, data preparation, SQL analysis, and stakeholder-oriented communication.