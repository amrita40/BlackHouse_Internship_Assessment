import pandas as pd

# Load the CSV
# df = pd.read_csv("C:\\Users\\amrit\OneDrive\Desktop\blackhouse\CRWV_2025-05-02 00_00_00+00_00.csv")  # repeat for FROG and SOUN
df = pd.read_csv(r"C:\Users\amrit\OneDrive\Desktop\blackhouse\CRWV_2025-05-02 00_00_00+00_00.csv")

# Filter only executed trades
df = df[df['action'] == 'T']

# Parse timestamps
df['timestamp'] = pd.to_datetime(df['ts_event'])
df.set_index('timestamp', inplace=True)

# Signed volume: size * (1 for Buy, -1 for Sell, 0 for Neutral)
df['signed_volume'] = df['size'] * df['side'].map({'B': 1, 'S': -1, 'N': 0})


# Resample to 1-minute intervals
resampled = df.resample('1min').agg({
    'price': ['first', 'last'],
    'signed_volume': 'sum'
})

resampled.columns = ['price_start', 'price_end', 'signed_volume']
resampled['price_change'] = resampled['price_end'] - resampled['price_start']

# Filter valid entries
resampled = resampled.dropna()
resampled = resampled[(resampled['signed_volume'] != 0) & (resampled['price_change'] != 0)]


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Scatterplot: Signed Volume vs Price Change
plt.figure(figsize=(10, 6))
sns.scatterplot(x='signed_volume', y='price_change', data=resampled, alpha=0.5)
plt.title("Temporary Market Impact (Signed Volume vs Price Change)")
plt.xlabel("Signed Volume")
plt.ylabel("Price Change")
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.grid(True)
plt.show()

# Fit a regression model (optional)
from sklearn.linear_model import LinearRegression

X = resampled['signed_volume'].values.reshape(-1, 1)
y = resampled['price_change'].values
model = LinearRegression()
model.fit(X, y)

print("Slope (Temporary Impact Coefficient):", model.coef_[0])
