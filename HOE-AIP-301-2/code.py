# =========================================
# Hands-on Exercise 2
# Data Preparation and Preprocessing
# =========================================

# Import Libraries
import pandas as pd
\
from google.colab import files
uploaded = files.upload()

# =========================================
# 1. Dataset Loading
# =========================================

# Load Dataset
df = pd.read_csv("HousePricePrediction.csv")

# Display First 10 Rows
print("First 10 Rows of Dataset:")
print(df.head(10))

# =========================================
# 2. Data Exploration
# =========================================

# Display Shape of Dataset
print("\nShape of Dataset:")
print(df.shape)

# Display Data Types
print("\nData Types of Columns:")
print(df.dtypes)

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# =========================================
# 3. Data Cleaning
# =========================================

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle Missing Values

# Fill numerical missing values with mean
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill categorical missing values with mode
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Check duplicates
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

# =========================================
# 4. Feature Selection
# =========================================

# Remove unnecessary identifier column if exists
if 'Id' in df.columns:
    df.drop('Id', axis=1, inplace=True)

print("\nColumns After Feature Selection:")
print(df.columns)

# =========================================
# 5. Data Preprocessing
# =========================================

# Convert categorical variables into numerical form
df_encoded = pd.get_dummies(df, drop_first=True)

# Display preview of processed dataset
print("\nPreview of Preprocessed Dataset:")
print(df_encoded.head())

# Display final shape
print("\nFinal Dataset Shape:")
print(df_encoded.shape)