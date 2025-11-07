import pandas as pd

# Load dummy data
data = pd.DataFrame({
    'Age': [23, 27, 29, 30, 25],
    'Salary': [45000, 52000, 48000, 60000, 50000]
})

# Calculate summary stats
print('📊 Data Analysis Report')
print('Mean Salary:', data['Salary'].mean())
print('Max Salary:', data['Salary'].max())
print('Min Salary:', data['Salary'].min())
