import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Comment this out if using Jupyter
sns.set(style="whitegrid")
# === 1. Load Dataset ===
# Load the dataset
file_path = r'C:\Users\vinee\OneDrive\Documents\Github\tech501-preassignment\Data Pathway notes\Global_AI_Content_Impact_Dataset.csv'
df = pd.read_csv(file_path)
# Display first 5 rows
df.head()
# === 2. Data Exploration ===
# Get basic information about the dataset
df.info()
# Basic statistics
df.describe(include='all')
# Check for missing values
missing = df.isnull().sum()
print("Missing values per column:\n", missing)
# Check shape
print(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns")
# Check column names
print("Columns:\n", df.columns.tolist())
# === 3.Clean the Data Set ===
# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
# Check for duplicates
df.drop_duplicates(inplace=True)
# Show the cleaned dataset
df.head()
# === 4. Transform/ Add new fields ===
# Since 'impact_level' doesn't exist in your dataset, let's create visualizations with existing data
# For example, we can analyze AI adoption rates by industry
 
# Industry adoption analysis
industry_adoption = df.groupby('industry')['ai_adoption_rate_(%)'].mean().sort_values(ascending=False)
print("Average AI Adoption Rate by Industry:\n", industry_adoption)
# === 5. Data Visualization ===
# Let's create appropriate visualizations with your existing data
 
# Bar plot: AI adoption rate by industry
plt.figure(figsize=(12, 6))
sns.barplot(x=industry_adoption.index, y=industry_adoption.values)
plt.title("Average AI Adoption Rate by Industry")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
 
# Relationship between AI adoption and job loss
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='ai_adoption_rate_(%)', y='job_loss_due_to_ai_(%)', hue='industry')
plt.title("Relationship Between AI Adoption and Job Loss")
plt.tight_layout()
plt.show()
 
# Distribution of top AI tools 
plt.figure(figsize=(9, 6))
tool_counts = df['top_ai_tools_used'].value_counts()
sns.barplot(x=tool_counts.index, y=tool_counts.values)
plt.title("Most Commonly Used AI Tools")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()