import streamlit as st
import pandas as pd

# uploaded_file = st.file_uploader('excelfile', type=['xlsx'])
# if uploaded_file is None:
#     st.stop()

# @st.cache_data
# def load_data(file):
#     print('执行加载数据')
#     return pd.read_excel(file,None)

# dfs = load_data(uploaded_file)

# # dfs = pd.read_excel(uploaded_file, None)
# names = list(dfs.keys())
# sheet_selects = st.multiselect('工作表',names,[])

# if len(sheet_selects)==0:
#     st.stop()

# tabs = st.tabs(sheet_selects)
# for tab, name in zip(tabs,sheet_selects):
#     with tab:
#         df = dfs[name]
#         st.dataframe(df)

st.write("""
## 我是你爸爸
### 我才是你爸爸

""")

st.image("picture.jpg")

import numpy as np
map_data = pd.DataFrame(
    np.random.randn(500, 2)/[50,50] + [31.05, 121.37],
    columns = ['lat','lon']

)
st.map(map_data)
