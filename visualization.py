import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
df = pd.read_csv("data/students_cleaned.csv")

# Sort by average for ranking
df_sorted = df.sort_values(by="Average", ascending=False).reset_index(drop=True)

# Create a color palette with top 3 highlighted
colors = ['#FFD700' if i == 0 else '#C0C0C0' if i == 1 else '#CD7F32' if i == 2 else '#3498db' for i in range(len(df_sorted))]

# Set seaborn style
sns.set(style="whitegrid")

# Create the plot
plt.figure(figsize=(20, 9))
barplot = sns.barplot(x="Name", y="Average", data=df_sorted, palette=colors)

# Customize labels
barplot.set_xticklabels(barplot.get_xticklabels(), rotation=45, ha='right', fontsize=10)
plt.title("🎯 Average Marks per Student with Grades & Top 3 Highlights", fontsize=18, fontweight='bold')
plt.xlabel("Student", fontsize=12)
plt.ylabel("Average Marks", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value and grade labels
for i, row in df_sorted.iterrows():
    grade = row['Grade']
    avg = row['Average']
    plt.text(i, avg + 1, f"{avg:.1f}\n({grade})", ha='center', va='bottom', fontsize=9)



# Save to output folder
os.makedirs("output", exist_ok=True)
plt.tight_layout()
plt.savefig("output/average_marks_highlighted.png", dpi=300)

plt.show()

# Facet plot by class



