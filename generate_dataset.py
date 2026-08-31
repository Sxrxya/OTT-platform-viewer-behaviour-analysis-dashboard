import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

n_rows = 20000

# Generating Data
user_ids = [f"USR{str(i).zfill(5)}" for i in range(1, n_rows + 1)]
ages = np.random.randint(18, 65, size=n_rows)
genders = np.random.choice(["Male", "Female", "Non-Binary", "Prefer not to say"], size=n_rows, p=[0.45, 0.45, 0.05, 0.05])

subscription_tiers = np.random.choice(["Basic", "Standard", "Premium"], size=n_rows, p=[0.3, 0.4, 0.3])
monthly_fees = []
for tier in subscription_tiers:
    if tier == "Basic": monthly_fees.append(9.99)
    elif tier == "Standard": monthly_fees.append(14.99)
    else: monthly_fees.append(19.99)

# We need average watch time around 72.5 hrs/user.
watch_time = np.random.normal(loc=72.5, scale=25, size=n_rows)
watch_time = np.clip(watch_time, 5, 200)

favorite_genres = np.random.choice(["Drama", "Action", "Comedy", "Sci-Fi", "Documentary", "Horror", "Romance"], size=n_rows)
device_types = np.random.choice(["Smart TV", "Mobile", "Tablet", "Desktop"], size=n_rows, p=[0.44, 0.30, 0.10, 0.16]) # Smart TV (44%)

completion_rate = np.random.normal(loc=68.4, scale=15, size=n_rows)
completion_rate = np.clip(completion_rate, 0, 100)

# Binge watcher flag
binge_watcher_flag = np.random.choice(["Yes", "No"], size=n_rows, p=[0.58, 0.42])

# Churn Status (14.2% overall churn)
# High risk for < 15 hours watch time.
churn_status = []
for i in range(n_rows):
    prob_churn = 0.142
    if watch_time[i] < 15:
        prob_churn *= 3 # 3x higher churn
    if subscription_tiers[i] == "Premium":
        prob_churn *= 0.3 # High retention
    if subscription_tiers[i] == "Basic" and device_types[i] == "Mobile":
        prob_churn *= 2.0 # High churn sensitivity
        
    prob_churn = min(prob_churn, 1.0)
    churn = np.random.choice(["Churned", "Retained"], p=[prob_churn, 1 - prob_churn])
    churn_status.append(churn)

# Let's adjust churn manually if the average isn't exactly 14.2%
churned_count = churn_status.count("Churned")
print(f"Current Churn Rate: {churned_count/n_rows * 100}%")

# Fix churn rate to exactly 2840 (14.2%)
target_churn = 2840
if churned_count > target_churn:
    indices_to_retain = [i for i, x in enumerate(churn_status) if x == "Churned"]
    change_idx = random.sample(indices_to_retain, churned_count - target_churn)
    for idx in change_idx:
        churn_status[idx] = "Retained"
elif churned_count < target_churn:
    indices_to_churn = [i for i, x in enumerate(churn_status) if x == "Retained"]
    change_idx = random.sample(indices_to_churn, target_churn - churned_count)
    for idx in change_idx:
        churn_status[idx] = "Churned"

customer_rating = np.random.choice([1, 2, 3, 4, 5], size=n_rows, p=[0.02, 0.03, 0.15, 0.4, 0.4]) # Avg ~ 4.1
peak_watch_time = np.random.choice(["Morning", "Afternoon", "Evening", "Night"], size=n_rows, p=[0.1, 0.15, 0.25, 0.5]) # Max traffic evening/night
active_days = np.random.randint(1, 31, size=n_rows)

# Create 28 columns total (filler columns to match '28 attributes')
df = pd.DataFrame({
    "User_ID": user_ids,
    "Age": ages,
    "Gender": genders,
    "Location": np.random.choice(["USA", "UK", "Canada", "Australia", "India", "Germany", "France"], size=n_rows),
    "Subscription_Tier": subscription_tiers,
    "Monthly_Fee": monthly_fees,
    "Watch_Time_Hours": np.round(watch_time, 2),
    "Favorite_Genre": favorite_genres,
    "Device_Type": device_types,
    "Completion_Rate_Pct": np.round(completion_rate, 2),
    "Binge_Watcher_Flag": binge_watcher_flag,
    "Churn_Status": churn_status,
    "Customer_Rating": customer_rating,
    "Peak_Watch_Time": peak_watch_time,
    "Active_Days_Per_Month": active_days,
    # Additional filler attributes to reach 28
    "Account_Age_Months": np.random.randint(1, 60, size=n_rows),
    "Total_Profiles": np.random.randint(1, 5, size=n_rows),
    "Kids_Profile_Active": np.random.choice(["Yes", "No"], size=n_rows),
    "Payment_Method": np.random.choice(["Credit Card", "PayPal", "Debit Card", "Apple Pay"], size=n_rows),
    "Auto_Renew": np.random.choice(["Enabled", "Disabled"], size=n_rows, p=[0.85, 0.15]),
    "Last_Login_Days_Ago": np.random.randint(0, 30, size=n_rows),
    "Content_Downloads_Per_Month": np.random.randint(0, 20, size=n_rows),
    "Ads_Watched": np.random.randint(0, 50, size=n_rows) * (np.array(subscription_tiers) == "Basic").astype(int),
    "Support_Tickets_Opened": np.random.choice([0, 1, 2, 3], size=n_rows, p=[0.8, 0.15, 0.04, 0.01]),
    "Recommendation_Click_Rate_Pct": np.round(np.random.uniform(5, 50, size=n_rows), 2),
    "Social_Share_Count": np.random.randint(0, 10, size=n_rows),
    "Primary_Language": np.random.choice(["English", "Spanish", "French", "German"], size=n_rows, p=[0.7, 0.15, 0.1, 0.05]),
    "Watchlist_Size": np.random.randint(0, 100, size=n_rows)
})

# Recalculate watch time to exactly match average 72.5
current_avg = df["Watch_Time_Hours"].mean()
df["Watch_Time_Hours"] = df["Watch_Time_Hours"] * (72.5 / current_avg)
df["Watch_Time_Hours"] = np.round(df["Watch_Time_Hours"], 2)

import os
os.makedirs("c:/Users/welcome/Downloads/OTT platform viewer  behaviour analysis dashboard/OTT-platform-viewer-behaviour-analysis-dashboard/Dataset", exist_ok=True)
df.to_csv("c:/Users/welcome/Downloads/OTT platform viewer  behaviour analysis dashboard/OTT-platform-viewer-behaviour-analysis-dashboard/Dataset/ott_viewer_behavior_cleaned.csv", index=False)
print("Dataset successfully generated!")
