# Final Report: OTT Viewer Behavior Analytics

## Executive Summary
This report summarizes the findings from the analysis of viewer behavioral data collected from our OTT platform. The objective of this analysis is to evaluate streaming habits, churn predictors, and genre popularity to facilitate data-driven content strategy and optimize retention. The underlying data consists of **20,000 user streaming records**.

## Key Performance Indicators (KPIs)
- **Total Subscribers Analyzed:** 20,000
- **Total Watch Hours:** ~1.45M hrs
- **Average Monthly Watch Time:** ~72.5 hrs/user
- **Average Customer Rating:** 4.1 / 5
- **Overall Churn Rate:** ~14.2%
- **Average Completion Rate:** 68.4%

## Core Insights

### 1. Churn vs. Engagement
The strongest predictor of churn is watch time. Users who watch fewer than 15 hours per month show a **3x higher churn rate** compared to highly active viewers. Increasing early engagement through personalized recommendations should be the top priority to retain new subscribers.

### 2. Demographic Preferences
- **Younger Demographics (18-25):** Heavily favor Action & Sci-Fi content and predominantly consume media on Mobile devices during night hours.
- **Older Demographics (35+):** Show strong preferences for Drama & Documentaries, largely consuming content via Smart TVs.

### 3. Subscription Tier Analysis
- **Premium Tier:** Users exhibit the highest retention rate (89.5%).
- **Basic Tier:** High churn sensitivity, particularly among mobile-only users.

### 4. Viewing Behaviors
- **Binge-Watching:** Over 58% of active users are categorized as binge-watchers, accounting for 72% of total watch time on the platform.
- **Peak Hours:** Maximum traffic consistently occurs between 8:00 PM and 11:30 PM.

## Business Recommendations
1. **Targeted Campaigns for At-Risk Users:** Deploy automated push notifications and email campaigns for users falling below the 15-hour watch time threshold within the first two weeks of their billing cycle.
2. **Mobile Optimization for Basic Tier:** Since Basic tier mobile users have the highest churn sensitivity, optimizing the mobile app experience (faster load times, better offline viewing support) could significantly reduce basic tier churn.
3. **Content Acquisition Strategy:** Given the high engagement from binge-watchers, prioritize acquiring serialized content (miniseries, multi-season dramas) over standalone films. Focus on Action/Sci-Fi for mobile-first acquisition campaigns, and Drama/Documentary for TV-centric promotions.

## Limitations of Current Analysis
- Real-time recommendation system log tracking is not present in the current dataset.
- Payment gateway transaction failures (involuntary churn) could not be decoupled from voluntary churn due to lack of billing data.
