# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Data Generation ---
# Create a dictionary of student data
data = {
    'Student_ID': range(101, 111),
    'Subject_A_Score': np.random.randint(60, 100, 10),
    'Subject_B_Score': np.random.randint(50, 95, 10),
    'Study_Hours': np.random.uniform(2, 10, 10).round(1)
}

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the initial DataFrame
print("Initial DataFrame:")
print(df)

# --- 2. Data Analysis ---
# Calculate the average score for each subject
avg_score_A = df['Subject_A_Score'].mean()
avg_score_B = df['Subject_B_Score'].mean()

print(f"\nAverage Score for Subject A: {avg_score_A:.2f}")
print(f"Average Score for Subject B: {avg_score_B:.2f}")

# Find the student with the highest total score
df['Total_Score'] = df['Subject_A_Score'] + df['Subject_B_Score']
top_student_id = df.loc[df['Total_Score'].idxmax()]['Student_ID']
print(f"Student with the highest total score is ID: {int(top_student_id)}")

# --- 3. Data Visualization ---
# Create a bar chart to compare average scores
subjects = ['Subject A', 'Subject B']
avg_scores = [avg_score_A, avg_score_B]

plt.figure(figsize=(8, 6))
plt.bar(subjects, avg_scores, color=['skyblue', 'lightgreen'])
plt.title('Average Scores for Subjects A and B')
plt.ylabel('Average Score')
plt.ylim(0, 100)
plt.show()

# Create a scatter plot to show the relationship between study hours and total score
plt.figure(figsize=(8, 6))
plt.scatter(df['Study_Hours'], df['Total_Score'], color='coral')
plt.title('Relationship between Study Hours and Total Score')
plt.xlabel('Study Hours')
plt.ylabel('Total Score')
plt.grid(True)
plt.show()