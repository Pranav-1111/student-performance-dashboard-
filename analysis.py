import pandas as pd
import os

# Load data
file_path = "student-performance-dashboard/data/students.csv"
df = pd.read_csv(file_path)


# Calculate average
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Grade assignment
def assign_grade(avg):
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 45:
        return 'c'
    elif avg >= 33:
        return 'd'
    else:
        return 'Fail'

# Add grade column
df['Grade'] = df['Average'].apply(assign_grade)

os.makedirs("data", exist_ok=True)

# Save cleaned & graded data
cleaned_path = "data/students_cleaned.csv"
df.to_csv(cleaned_path, index=False)

# Save report
with open("report.txt", "w") as f:
    f.write("\nSummary Report\n")
    f.write("======================\n")
    f.write(f"\nAverage Marks per Subject:\n{df[['Math','Science','English']].mean()}\n")
    f.write(f"\nGrade Distribution:\n{df['Grade'].value_counts()}\n")

print("✅ Data analysis complete. Report saved to report.txt")
