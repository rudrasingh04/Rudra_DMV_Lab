import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# 1. Load dataset and select the top 30 companies
df = pd.read_csv('9000_companies_dataset.csv')
top_30 = df.head(30).copy()

# 2. Data Cleaning Functions
def clean_reviews(x):
    """Converts review strings like '(59.9k Reviews)' into numeric values."""
    if pd.isna(x): return 0
    x = str(x).replace('(', '').replace(')', '').replace(' Reviews', '').replace(' Review', '').strip()
    if 'k' in x:
        return float(x.replace('k', '')) * 1000
    elif 'L' in x: 
        return float(x.replace('L', '')) * 100000
    try:
        return float(x)
    except:
        return 0

def clean_years(x):
    """Extracts numeric years from strings like '55 years old'."""
    if pd.isna(x): return 0
    match = re.search(r'(\d+)', str(x))
    return int(match.group(1)) if match else 0

# Apply cleaning functions
top_30['review_count_num'] = top_30['review_count'].apply(clean_reviews)
top_30['years_num'] = top_30['years'].apply(clean_years)

# 3. Find the name of headquarters company wise
hq_df = top_30[['name', 'hq']]
hq_df.to_csv('top_30_hq.csv', index=False)
print("Headquarters data saved to 'top_30_hq.csv'.")
print("\nSample Headquarters Data:")
print(hq_df.head())

# 4. Data Visualization
plt.figure(figsize=(15, 20))

# Chart A: Pie chart [Company Employees Wise]
plt.subplot(4, 1, 1)
emp_counts = top_30['employees'].value_counts()
plt.pie(emp_counts, labels=emp_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart - Employee Categories for Top 30 Companies')

# Chart B: Format Chart [Companies Reviews Wise] (Using a Horizontal Bar Chart)
plt.subplot(4, 1, 2)
sns.barplot(
    x='review_count_num', 
    y='name', 
    data=top_30.sort_values('review_count_num', ascending=False), 
    palette='viridis'
)
plt.title('Horizontal Bar Chart - Total Reviews per Company')
plt.xlabel('Number of Reviews')
plt.ylabel('Company Name')

# Chart C: Bar chart [Companies Rating Wise]
plt.subplot(4, 1, 3)
sns.barplot(x='name', y='ratings', data=top_30, palette='magma')
plt.title('Bar Chart - Ratings per Company')
plt.xlabel('Company Name')
plt.ylabel('Ratings out of 5.0')
plt.xticks(rotation=90)
plt.ylim(0, 5)

# Chart D: Line chart [Companies Year Wise]
plt.subplot(4, 1, 4)
plt.plot(top_30['name'], top_30['years_num'], marker='o', linestyle='-', color='b')
plt.title('Line Chart - Years of Existence per Company')
plt.xlabel('Company Name')
plt.ylabel('Years')
plt.xticks(rotation=90)
plt.grid(True)

# Adjust layout and save/show plots
plt.tight_layout()
plt.savefig('company_charts.png')
plt.show()