# 🎬 OTT Platform Viewer Behaviour Analysis

## 📌 Project Overview
OTT Platform Viewer Behaviour Analysis is a comprehensive data analytics and visualization project designed to analyze subscriber watching patterns, content preferences, churn risk, and platform engagement.

The project utilizes a cleaned dataset containing 20,000 user streaming records and 28 attributes to generate actionable insights through an interactive dashboard for platform optimization and content strategy.

---
## 🎯 Problem Statement
With the rapid growth of streaming services, understanding viewer engagement and preventing churn is critical for subscription-based business models. Streaming platforms generate massive amounts of user interaction data, yet identifying key drivers of user retention, content drop-offs, and device preferences can be complex.

This project analyzes viewer behavior data to evaluate streaming habits, churn predictors, subscription performance, and genre popularity to support data-driven decision-making for marketing and content acquisition teams.

---
## 🎯 Objectives
- Analyze overall streaming watch hours, subscriber growth, and user retention.
- Identify high-risk churn customer segments based on viewing frequency and drop-off rates.
- Evaluate content genre performance across demographic segments (Age, Gender, Location).
- Assess viewing behavior by device types (Smart TV, Mobile, Desktop, Tablet) and time intervals.
- Measure the impact of subscription tiers (Basic, Standard, Premium) on user lifetime value.
- Present key findings and metrics through an interactive, multi-page HTML dashboard.

---
## 🛠️ Tools & Technologies
- **Python / Pandas / NumPy** — Data cleaning, preprocessing, and exploratory data analysis (EDA).
- **HTML / CSS / JavaScript / Chart.js** — Interactive dashboard creation and UI development.
- **CSV** — Cleaned analytical dataset storage.
- **GitHub** — Version control and project documentation.

---
## 📊 Dataset
The cleaned dataset consists of 20,000 rows and 28 analytical features.

**Key Fields Include:**
- `User_ID`: Unique identifier for subscribers
- `Age & Gender`: Demographic details
- `Subscription_Tier`: Basic, Standard, Premium
- `Monthly_Fee`: Subscription cost ($)
- `Watch_Time_Hours`: Total streaming time per month
- `Favorite_Genre`: Drama, Action, Comedy, Sci-Fi, Documentary, Horror, Romance
- `Device_Type`: Smart TV, Mobile, Tablet, Laptop
- `Completion_Rate (%)`: Percentage of watched titles completed
- `Binge_Watcher_Flag`: Yes/No (Based on >3 consecutive episodes watched)
- `Churn_Status`: Retained / Churned
- `Customer_Rating`: Platform satisfaction rating (1 to 5)
- `Peak_Watch_Time`: Morning, Afternoon, Evening, Night
- `Active_Days_Per_Month`: Frequency of platform logins per month

---
## 📈 Key KPIs
| KPI Metric | Value |
|---|---|
| Total Subscribers Analyzed | 20,000 |
| Total Watch Hours | 1,450,000 hrs |
| Average Monthly Watch Time | 72.5 hrs/user |
| Average Customer Rating | 4.1 / 5 |
| Overall Churn Rate | 14.2% |
| Active Subscribers | 17,160 |
| Churned Subscribers | 2,840 |
| Average Completion Rate | 68.4% |
| Top Preferred Device | Smart TV (44%) |

---
## 🔍 Key Insights
- **Churn vs. Engagement:** Users watching fewer than 15 hours per month show a 3x higher churn rate compared to highly active viewers.
- **Demographic Preferences:** Viewers aged 18–25 prefer Action & Sci-Fi on mobile devices during night hours, while users aged 35+ prefer Drama & Documentaries on Smart TVs.
- **Subscription Tier Analysis:** Premium plan users have the highest retention rate (89.5%), whereas Basic plan mobile-only users have the highest churn sensitivity.
- **Binge Watching Trend:** Over 58% of active users are categorized as binge-watchers, contributing to 72% of total platform watch time.
- **Peak Streaming Time:** Maximum streaming traffic occurs between 8:00 PM and 11:30 PM.

---
## 📊 Dashboard Focus
The interactive HTML/JS dashboard provides multi-perspective views:
- **Executive Summary:** Overview of Subscribers, Total Streaming Hours, Churn Rate, and Revenue.
- **Viewer Behavior & Demographics:** Genre popularity, age distribution, and device usage breakdowns.
- **Retention & Churn Analytics:** Churn drivers, drop-off factors, and customer satisfaction correlations.
- **Subscription & Revenue Performance:** Revenue contribution by subscription tiers and customer lifetime value.

---
## 📁 Repository Structure
```text
OTT-Platform-Viewer-Analytics/
│
├── README.md
│
├── Problem-Statement/
│   └── OTT_Analytics_Problem_Statement.md
│
├── Dataset/
│   ├── ott_viewer_behavior_raw.csv (Optional)
│   └── ott_viewer_behavior_cleaned.csv
│
├── Dashboard/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── Report/
    └── OTT_Viewer_Analytics_Final_Report.md
```

---
## 🚀 How to Use
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/OTT-Platform-Viewer-Analytics.git
   ```
2. **Explore the Dataset:** Open the `Dataset/` folder to review raw and processed dataset files.
3. **View Dashboard:** Open `Dashboard/index.html` in any web browser to interact with the visualizations. (No server required!)
4. **Read Detailed Report:** Check the `Report/` folder for comprehensive project findings and business recommendations.

---
## ⚠️ Limitations
- The dataset lacks real-time recommendation system log tracking.
- Payment gateway transaction failure details are not included in this release.
- Regional content availability flags were excluded to maintain focus on primary viewer behavior.

---
## 🧑‍💻 Author
**Data Analytics & Visualization Project** — OTT Platform Analytics
- **GitHub:**https://github.com/selvapriyanB

---
## ⭐ Conclusion
This project highlights how streaming behavioral data can be converted into business intelligence. By leveraging user segmentation, churn analysis, and genre tracking, OTT platforms can optimize content acquisition, enhance user engagement, and reduce churn effectively.
