#import streamlit as st
import pandas as pd
import requests
def get_json():
    url = 'https://dsci551-project-data1-default-rtdb.firebaseio.com/.json'
    response = requests.get(url)
    response1 = response.json()
    df1 = pd.DataFrame.from_dict(response1)
    return df1
df = get_json()
st.dataframe(df)

