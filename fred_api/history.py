from datetime import datetime
import pandas as pd
import requests

def get_history(key, index, timeperiod):
    # Send a request to St.Louis Fed
    url = 'https://api.stlouisfed.org/fred/series/observations?series_id=' + index + '&api_key=' + key + '&file_type=json'
    response = requests.get(url)
    
    # Clean the response
    df = pd.DataFrame(response.json()['observations'])
    df.index = pd.to_datetime(df.date)
    
    # Transform integers into floats
    df = df.loc[:,'value']
    df = df[df != "."]
    df = df.astype(float)
    
    # Resample value in the needed timeperiod
    df = df.resample(timeperiod).ffill()
    df = df.to_period(timeperiod)
    return(pd.DataFrame(df))