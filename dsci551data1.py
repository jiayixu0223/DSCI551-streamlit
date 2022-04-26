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
df1 = pd.DataFrame(final)
final2 = pd.DataFrame.transpose(df1)
val = final2.values
val2 = val.tolist()
st.title("Table for Linkedin!")
for i in range(len(val2)):
    cols = st.columns(9)
    cols[0].write(val2[0])
    cols[1].write(val2[1])
    cols[2].write(val2[2])
    cols[3].write(val2[3])
    cols[4].write(val2[4])
    cols[5].write(val2[5])
    cols[6].write(val2[6])
    cols[7].write(val2[7])
    cols[8].write(val2[8]) 
