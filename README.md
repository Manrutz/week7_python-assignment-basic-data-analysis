# week7_python-assignment-basic-data-analysis
# 📊 Sales Data Analysis Assignment

## 🎯 Objective
The objective of this assignment was to:
- Load and explore a dataset using **pandas**.
- Perform **basic data analysis** such as descriptive statistics and groupings.
- Create **visualizations** using matplotlib and seaborn to gain insights from the dataset.
- Summarize findings and patterns observed in the data.

---

## 📂 Dataset Description
The dataset used in this analysis contains **sales transactions** with the following columns:

- **date**: The transaction date (monthly).
- **region**: The geographical region where sales occurred (North, South, East, West).
- **product**: The type of product sold (Laptop, Phone, Tablet).
- **sales**: The sales amount in USD.

---

## 🔍 Data Exploration & Cleaning
- The dataset was successfully loaded and previewed using `.head()`.
- No missing values were found; however, handling mechanisms were applied (`dropna`) as a safeguard.
- Data types were confirmed, with `date` treated as time data for trend analysis.

---

## 📊 Analysis & Key Findings
1. **Descriptive Statistics**
   - The mean sales value was around mid-range, with variability across months.
   - Standard deviation indicated moderate variation in sales figures.

2. **Group Analysis**
   - Average sales per **region** showed that some regions consistently outperformed others.
   - Average sales per **product** revealed that higher-priced products like **Laptops** contributed more to revenue compared to Tablets and Phones.

---

## 📈 Visualizations & Insights
1. **Line Chart (Sales Over Time)**  
   Sales fluctuated month to month, showing peaks in certain months.  

2. **Bar Chart (Average Sales by Region)**  
   The **West** region recorded the highest average sales.  

3. **Histogram (Sales Distribution)**  
   Sales values were concentrated around mid-range amounts, with fewer very high sales.  

4. **Scatter Plot (Sales by Region & Product)**  
   - Clear variation in sales performance across both products and regions.  
   - Phones and Tablets had more modest sales, while Laptops were dominant.  

---

## 📝 Conclusion
The analysis demonstrated how Python libraries (**pandas, matplotlib, seaborn**) can be used to load, analyze, and visualize sales data. Key takeaways include:

- Regional differences play a significant role in sales performance.  
- Laptops are the strongest product category.  
- Sales trends fluctuate monthly, suggesting possible seasonal or market influences.  

👉 Future analysis could include **forecasting sales trends** or **correlating sales with external factors** (e.g., marketing spend, holidays).  

---
