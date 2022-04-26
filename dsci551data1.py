import streamlit as st
import pandas as pd
import requests
import html
url = 'https://dsci551-project-data1-default-rtdb.firebaseio.com/.json'
response = requests.get(url)
response1 = response.json()
#df1 = pd.DataFrame.from_dict(response1)
cols = ['Name','Experience','Introduction','Location','Number of Organizations','Number of Positions','Number of Skills',
       'Organizations','Positions','skills']
final = []
for key,value in response1.items():
    each_row = []
    each_row.append(key)
    dict1 = response1[key]
    for key1,value1 in dict1.items():
        if type(value1) ==str:
            value1 = value1.strip()
            value1 = value1.replace(' ','')
        each_row.append(value1)
    final.append(each_row)
df1 = pd.DataFrame(final)
df1.columns = cols
st.dataframe(data=None, width=None, height=None)
st.dataframe(df1,500,500)
st.dataframe(df.style.highlight_max(axis=0))
