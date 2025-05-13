import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

def calc_change_percentage(df_indices):
    change = df_indices['Close'].diff().iloc[-1]
    last_date = df_indices.index[-1]

    df_indices.loc[last_date, ('Change$', '^DJI')]  = np.round(change['^DJI'], 2)
    df_indices.loc[last_date, ('Change$', '^SPX')]  = np.round(change['^SPX'], 2)
    df_indices.loc[last_date, ('Change$', '^IXIC')] = np.round(change['^IXIC'], 2)
    df_indices.loc[last_date, ('Change$', '^SOX')]  = np.round(change['^SOX'], 2)

    change_percentage = df_indices['Close'].diff().iloc[-1]/df_indices['Close'].iloc[-2]
        
    df_indices.loc[last_date, ('Change%', '^DJI')]  = f"{np.round(change_percentage['^DJI']*100, 2)}%"
    df_indices.loc[last_date, ('Change%', '^SPX')]  = f"{np.round(change_percentage['^SPX']*100, 2)}%"
    df_indices.loc[last_date, ('Change%', '^IXIC')] = f"{np.round(change_percentage['^IXIC']*100, 2)}%"
    df_indices.loc[last_date, ('Change%', '^SOX')]  = f"{np.round(change_percentage['^SOX']*100, 2)}%"

    df_indices['Close'] = np.round(df_indices['Close'],    2)

    return df_indices

def get_close_price(tickers, day):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=day)
    stock = yf.Tickers(tickers)
    df = stock.history(start=start_date, end=end_date)
    return df

def main():
    tickers = ['NVDA']
    df_tickers = get_close_price(tickers, 1)

    indices = ['^DJI', '^SPX', '^IXIC', '^SOX']
    selected_columns = [
        ('Close', '^DJI'),
        ('Change%', '^DJI'),
        ('Close', '^SPX'),
        ('Change%', '^SPX'),
        ('Close', '^IXIC'),
        ('Change%', '^IXIC'),
        ('Close', '^SOX'),
        ('Change%', '^SOX'),
    ]
    df_indices = get_close_price(indices, 4)
    df_indices = calc_change_percentage(df_indices)

    print(np.round(df_tickers['Close'], 2))
    print('-------------------------------------------')
    print(df_indices[selected_columns].iloc[-1].round(2))
        


if __name__ == '__main__':
    main()