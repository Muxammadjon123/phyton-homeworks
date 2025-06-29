import pandas as pd

#Filter flights with departure delay > 30 minutes
def filter_delayed(df):
    return df[df['DepDelay'] > 30]

# Add Delay_Per_Hour column (DepDelay divided by AirTime in hours)
def add_delay_per_hour(df):
    df = df.copy()
    df['Scheduled_Hours'] = df['AirTime'] / 60  # Convert to hours
    df['Delay_Per_Hour'] = df['DepDelay'] / df['Scheduled_Hours']
    return df

# Read data (replace with actual file if needed)
df = pd.read_csv('flights.csv')  # or .parquet() etc.

# Apply pipeline
result = (
    df.pipe(filter_delayed)
      .pipe(add_delay_per_hour)
)

# View result
print(result[['DepDelay', 'AirTime', 'Scheduled_Hours', 'Delay_Per_Hour']].head())
