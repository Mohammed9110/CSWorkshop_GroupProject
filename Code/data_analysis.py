import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = "Data/qatar_visitor_arrivals.csv"

# Read CSV and fix column separation issues
df = pd.read_csv(file_path, encoding="utf-8", sep=",", engine="python")

# Print the detected column names
print("Columns in CSV:", df.columns)

# **Fix column names by stripping spaces and removing special characters**
df.columns = df.columns.str.strip()

# **Manually rename columns if needed**
expected_columns = ["Month", "Air", "Land", "Sea", "Total Visitor Arrivals"]
df.columns = expected_columns

# Debug: Print final column names after correction
print("Fixed Columns:", df.columns)

# **Check if "Total Visitor Arrivals" exists**
if "Total Visitor Arrivals" not in df.columns:
    print("❌ Column 'Total Visitor Arrivals' not found! Check column names again.")
    exit()

# Display first 5 rows to confirm correct data loading
print("✅ CSV file loaded successfully!")
print(df.head())

# Ensure the "Reports" folder exists
reports_folder = "Reports"
os.makedirs(reports_folder, exist_ok=True)

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df["Month"], df["Total Visitor Arrivals"], marker="o", linestyle="-", color="b", label="Total Visitors")

# Labels and title
ax.set_xlabel("Month")
ax.set_ylabel("Total Visitor Arrivals")
ax.set_title("Qatar Visitor Arrivals Over Time")
ax.legend()
ax.grid()

# **Fix overlapping x-axis labels**
ax.set_xticks(np.arange(0, len(df["Month"]), step=5))  # Show every 5th month
ax.set_xticklabels(df["Month"][::5], rotation=45)  # Rotate and set step

# Save the plot in the Reports folder
save_path = os.path.join(reports_folder, "visitor_arrivals_plot.png")
fig.savefig(save_path)
print(f"✅ Plot saved successfully at: {save_path}")

# **Find key insights**
max_visitors = df.loc[df["Total Visitor Arrivals"].idxmax()]
min_visitors = df.loc[df["Total Visitor Arrivals"].idxmin()]
avg_visitors = df["Total Visitor Arrivals"].mean()

# Print insights
print("\n🔴 Highest Visitors:", max_visitors["Total Visitor Arrivals"], "in", max_visitors["Month"])
print("🟢 Lowest Visitors:", min_visitors["Total Visitor Arrivals"], "in", min_visitors["Month"])
print("🔵 Average Monthly Visitors:", round(avg_visitors, 2))

# **Calculate Yearly Averages**
df["Year"] = df["Month"].str[:4]  # Extract Year from Month
yearly_avg = df.groupby("Year")["Total Visitor Arrivals"].mean()

# Print yearly averages
print("\n📊 Yearly Average Visitor Arrivals:\n", yearly_avg)

# **Save insights into a text report**
report_path = os.path.join(reports_folder, "visitor_arrivals_report.txt")

with open(report_path, "w", encoding="utf-8") as report:
    report.write(f"🔴 Highest Visitors: {max_visitors['Total Visitor Arrivals']} in {max_visitors['Month']}\n")
    report.write(f"🟢 Lowest Visitors: {min_visitors['Total Visitor Arrivals']} in {min_visitors['Month']}\n")
    report.write(f"🔵 Average Monthly Visitors: {avg_visitors:.2f}\n\n")
    report.write("📊 Yearly Average Visitor Arrivals:\n")
    report.write(yearly_avg.to_string())

print(f"\n✅ Report saved successfully at: {report_path}")

# Show the plot (optional)
plt.show()
