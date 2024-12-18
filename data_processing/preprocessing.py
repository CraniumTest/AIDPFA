import numpy as np

def preprocess_data(df):
    # Handle missing values
    df.fillna(method='ffill', inplace=True)

    # Feature engineering
    df['daily_return'] = df['close'].pct_change()
    df['volatility'] = df['daily_return'].rolling(window=30).std()

    # Drop NaN values created by rolling window
    df.dropna(inplace=True)
    return df
