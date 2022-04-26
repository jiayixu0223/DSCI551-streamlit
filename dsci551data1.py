import streamlit as st
import pandas as pd
import requests
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
        each_row.append(value1)
    final.append(each_row)
c = st.empty()
st.write("List of Linkedin")
for text in final:
    res = str(text)[1:-1]
    c.write("res")
