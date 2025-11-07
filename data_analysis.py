import pandas as pd

data = pd.DataFrame({
    'Age': [23, 27, 29, 30, 25],
    'Salary': [45000, 52000, 48000, 60000, 50000]
})

print('📊 Basic Data Insights')
print('Mean Salary:', data['Salary'].mean())
print('Max Salary:', data['Salary'].max())
print('Min Salary:', data['Salary'].min())
