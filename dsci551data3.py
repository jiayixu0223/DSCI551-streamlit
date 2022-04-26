import streamlit as st
import pandas as pd
import requests
url = 'https://dsci551-project-data3-default-rtdb.firebaseio.com/.json'
response = requests.get(url)
response1 = response.json()
#df1 = pd.DataFrame.from_dict(response1)
cols = ['Position Name','Hourly Pay','Location','Course Related','Description','Requirement']
final = []
for key,value in response1.items():
    each_row = ['','','','','','']
    each_row[0] = key
    dict1 = response1[key]
    for key1,value1 in dict1.items():
        if key1 in cols:
            each_row[cols.index(key1)] = value1
    final.append(each_row)
df1 = pd.DataFrame(final)
df1.columns = cols
#st.dataframe(data=None, width=None, height=None)
st.title('Job List Data')
st.dataframe(df1)
url2 = 'https://empowerusc.netlify.app/application.html'
st.write("Link to apply [link](%s)" % url2)
