import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Age': [23, 27, np.nan, 30, 25],
    'Experience': [1, 3, 2, 4, np.nan]
})

data.fillna(data.mean(), inplace=True)
print('✅ Cleaned Data:')
print(data)
