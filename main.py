import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import numpy as np

# --- 1. Dataset Simulation ---
# In a real scenario, this would be loaded from a CSV file (pd.read_csv('employees.csv')).
# For this self-contained script, we'll simulate the data.
np.random.seed(42) # for reproducibility
num_employees = 100
departments = ['Sales', 'IT', 'HR', 'Marketing', 'Operations']
regions = ['Africa', 'Asia Pacific', 'North America', 'Middle East', 'Europe', 'South America']

data = {
    'employee_id': [f'EMP{str(i).zfill(3)}' for i in range(1, num_employees + 1)],
    'department': np.random.choice(departments, num_employees, p=[0.2, 0.25, 0.1, 0.15, 0.3]),
    'region': np.random.choice(regions, num_employees),
    'performance_score': np.random.uniform(50, 100, num_employees).round(2),
    'years_experience': np.random.randint(1, 15, num_employees),
    'satisfaction_rating': np.random.uniform(1, 5, num_employees).round(1)
}
df = pd.DataFrame(data)

# --- 2. Data Analysis ---
# Calculate the frequency count for the "Operations" department
operations_count = df[df['department'] == 'Operations'].shape[0]

# Print the frequency count to the console
print(f"Frequency count for the 'Operations' department: {operations_count}")

# --- 3. Data Visualization ---
# Create a count plot showing department distribution
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
ax = sns.countplot(
    x='department', 
    data=df, 
    palette='viridis', 
    order=df['department'].value_counts().index,
    hue='department', # Assign 'department' to hue to resolve warning
    legend=False      # Hide the legend as it's redundant
)

# Add titles and labels for clarity
ax.set_title('Employee Distribution Across Departments', fontsize=16, fontweight='bold')
ax.set_xlabel('Department', fontsize=12)
ax.set_ylabel('Number of Employees', fontsize=12)

# Add data labels on top of each bar
for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height())}', 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha='center', 
        va='center', 
        xytext=(0, 9), 
        textcoords='offset points',
        fontweight='medium'
    )

plt.tight_layout()
plt.savefig('chart.png', dpi=300)