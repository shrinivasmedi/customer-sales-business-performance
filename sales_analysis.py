# ============================================================
# PROJECT: Customer Sales & Business Performance Analytics
# TOOLS: Python, Pandas, NumPy
# PURPOSE: Analyze sales performance and customer behavior
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------------------
# 1. DATA LOADING
# ------------------------------------------------------------

DATA_PATH = Path(__file__).parent / "train.csv"
OUTPUT_DIR = Path(__file__).parent / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)


print("=" * 60)
print("CUSTOMER SALES & BUSINESS PERFORMANCE ANALYTICS")
print("=" * 60)

print(f"\nDataset loaded successfully: {df.shape[0]:,} rows, {df.shape[1]} columns")


# ------------------------------------------------------------
# 2. DATA QUALITY ASSESSMENT
# ------------------------------------------------------------

missing_values = df.isnull().sum()
duplicate_count = df.duplicated().sum()

df["Order Date"] = pd.to_datetime(
    df["Order Date"], dayfirst=True, errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], dayfirst=True, errors="coerce"
)
df.to_csv(OUTPUT_DIR / "sales_data_clean.csv", index=False)

print("\n--- DATA QUALITY REPORT ---")
print(f"Duplicate rows: {duplicate_count}")
print(f"Missing postal codes: {df['Postal Code'].isnull().sum()}")
print(f"Invalid order dates: {df['Order Date'].isnull().sum()}")
print(f"Invalid shipping dates: {df['Ship Date'].isnull().sum()}")


# ------------------------------------------------------------
# 3. KEY BUSINESS KPIs
# ------------------------------------------------------------

total_sales = df["Sales"].sum()
total_records = len(df)
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

average_sales_per_record = df["Sales"].mean()

average_sales_per_order = (
    df.groupby("Order ID")["Sales"].sum().mean()
)

kpis = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Sales Records",
        "Unique Orders",
        "Unique Customers",
        "Average Sales per Record",
        "Average Sales per Order"
    ],
    "Value": [
        total_sales,
        total_records,
        total_orders,
        total_customers,
        average_sales_per_record,
        average_sales_per_order
    ]
})

print("\n--- KEY BUSINESS KPIs ---")
print(f"Total sales: ${total_sales:,.2f}")
print(f"Sales records: {total_records:,}")
print(f"Unique orders: {total_orders:,}")
print(f"Unique customers: {total_customers:,}")
print(f"Average sales per record: ${average_sales_per_record:,.2f}")
print(f"Average sales per order: ${average_sales_per_order:,.2f}")


# ------------------------------------------------------------
# 4. PRODUCT CATEGORY ANALYSIS
# ------------------------------------------------------------

category_analysis = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Sales_Records=("Sales", "count"),
        Average_Sales=("Sales", "mean")
    )
    .sort_values("Total_Sales", ascending=False)
)

category_analysis["Sales_Contribution_Pct"] = (
    category_analysis["Total_Sales"] / total_sales * 100
)

print("\n--- PRODUCT CATEGORY PERFORMANCE ---")
print(category_analysis.round(2).to_string())


# ------------------------------------------------------------
# 5. CUSTOMER SEGMENT ANALYSIS
# ------------------------------------------------------------

segment_analysis = (
    df.groupby("Segment")
    .agg(
        Total_Sales=("Sales", "sum"),
        Sales_Records=("Sales", "count"),
        Unique_Customers=("Customer ID", "nunique"),
        Unique_Orders=("Order ID", "nunique")
    )
    .sort_values("Total_Sales", ascending=False)
)

segment_analysis["Sales_Contribution_Pct"] = (
    segment_analysis["Total_Sales"] / total_sales * 100
)

print("\n--- CUSTOMER SEGMENT PERFORMANCE ---")
print(segment_analysis.round(2).to_string())


# ------------------------------------------------------------
# 6. REGIONAL SALES ANALYSIS
# ------------------------------------------------------------

regional_analysis = (
    df.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Sales_Records=("Sales", "count"),
        Unique_Customers=("Customer ID", "nunique"),
        Unique_Orders=("Order ID", "nunique")
    )
    .sort_values("Total_Sales", ascending=False)
)

regional_analysis["Sales_Contribution_Pct"] = (
    regional_analysis["Total_Sales"] / total_sales * 100
)

print("\n--- REGIONAL SALES PERFORMANCE ---")
print(regional_analysis.round(2).to_string())


# ------------------------------------------------------------
# 7. EXPORT ANALYSIS RESULTS
# ------------------------------------------------------------

kpis.to_csv(OUTPUT_DIR / "business_kpis.csv", index=False)

category_analysis.to_csv(
    OUTPUT_DIR / "category_analysis.csv"
)

segment_analysis.to_csv(
    OUTPUT_DIR / "customer_segment_analysis.csv"
)

regional_analysis.to_csv(
    OUTPUT_DIR / "regional_analysis.csv"
)

print("\n--- EXPORT STATUS ---")
print(f"Analysis results saved to: {OUTPUT_DIR}")
print("\nAnalysis completed successfully.")

# ==========================================
# VISUALIZATION 1: SALES BY CATEGORY
# ==========================================

plt.figure(figsize=(10, 6))

sns.barplot(
    data=category_analysis.reset_index(),
    x="Category",
    y="Total_Sales"
)

plt.title("Total Sales by Product Category", fontsize=16)
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR.parent / "visualizations" / "sales_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nVisualization saved: sales_by_category.png")

# ==========================================
# VISUALIZATION 2: MONTHLY SALES TREND
# ==========================================

monthly_sales = (
    df.set_index("Order Date")
    .resample("MS")["Sales"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(14, 6))

sns.lineplot(
    data=monthly_sales,
    x="Order Date",
    y="Sales"
)

plt.title("Monthly Sales Trend (2015–2018)", fontsize=16)
plt.xlabel("Order Date", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR.parent / "visualizations" / "monthly_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Visualization saved: monthly_sales_trend.png")