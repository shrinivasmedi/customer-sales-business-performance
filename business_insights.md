# Customer Sales & Business Performance Analytics

## 1. Project Objective

Analyze historical retail sales data to understand product category performance, customer segment contributions, regional sales distribution, and monthly sales trends.

The objective is to transform raw sales records into actionable business insights using Python and data visualization.

## 2. Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Power BI

## 3. Dataset Overview

- Total records: 9,800
- Total columns: 18
- Unique orders: 4,922
- Unique customers: 793
- Analysis period: January 2015 to December 2018

The dataset contains order dates, shipping details, customer segments,
geographic information, product categories, product names, and sales values.

## 4. Key Performance Indicators

| Metric | Value |
|---|---:|
| Total Sales | $2,261,536.78 |
| Sales Records | 9,800 |
| Unique Orders | 4,922 |
| Unique Customers | 793 |
| Average Sales per Record | $230.77 |
| Average Sales per Order | $459.48 |

## 5. Key Findings

### Product Category Performance

- Technology generated the highest sales at $827,455.87.
- Furniture generated $728,658.58.
- Office Supplies generated $705,422.33.
- Technology contributed 36.59% of total sales.

### Customer Segment Performance

- Consumer customers generated $1,148,060.53 in sales.
- Corporate customers generated $688,494.07.
- Home Office customers generated $424,982.18.
- Consumer sales accounted for 50.76% of total sales.

### Regional Performance

- West generated the highest regional sales at $710,219.68.
- East generated $669,518.73.
- Central generated $492,646.91.
- South generated $389,151.46.

## 6. Data Quality Assessment

- No exact duplicate rows were identified.
- Eleven records have missing postal codes.
- No invalid order dates were identified.
- No invalid shipping dates were identified.

Missing postal codes were retained because they do not prevent the planned sales analysis.

## 7. Business Recommendations

1. Investigate which products and subcategories contribute most to Technology sales.
2. Examine customer purchasing patterns across the three customer segments.
3. Investigate the differences in sales between the West and South regions.
4. Analyze monthly sales trends to identify seasonal patterns.
5. Use an interactive dashboard to make these findings accessible to business stakeholders.

These recommendations are areas for further investigation, not claims that the dataset has already established their causes.

## 8. Project Limitations

The dataset does not contain profit, cost, discount, or margin fields.

Consequently, this project evaluates sales performance rather than profitability.

## 9. Deliverables

- Python data analysis script
- Data quality assessment
- Business KPI calculations
- Product category analysis
- Customer segment analysis
- Regional sales analysis
- Python visualizations
- Exported CSV reports
- Interactive Power BI dashboard with KPI cards, category analysis, customer segment analysis, regional analysis, monthly sales trends, and Year/Region/Category slicers