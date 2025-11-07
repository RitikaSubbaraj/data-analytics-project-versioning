import pandas as pd
import numpy as np

# Create dataset
data = pd.DataFrame({
    'Age': [23, 27, np.nan, 30, 25],
    'Experience': [1, 3, 2, 4, np.nan]
})

# Handle missing values
data.fillna(data.mean(), inplace=True)
print('Data after preprocessing:')
print(data)
