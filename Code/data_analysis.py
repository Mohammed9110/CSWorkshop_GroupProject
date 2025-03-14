import pandas as pd

# Load the dataset
file_path = "../Data/qatar_visitor_arrivals.csv"
df = pd.read_csv(file_path)

# Display the first 5 rows
print("🔍 Preview of the Dataset:")
print(df.head())
