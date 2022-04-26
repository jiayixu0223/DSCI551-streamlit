import streamlit as st
import pandas as pd
import requests
url = 'https://dsci551-project-data1-default-rtdb.firebaseio.com/.json'
response = requests.get(url)
response1 = response.json()
df1 = pd.DataFrame.from_dict(response1)
st.dataframe(df1)
