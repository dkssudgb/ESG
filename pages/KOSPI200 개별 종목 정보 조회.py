# import module ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import seaborn as sns
import streamlit as st

import koreanize_matplotlib

import os
from glob import glob
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="📈",
    layout="wide",
)

file_name = "./data\KOSPI200_ESGrate.csv"

st.markdown("# KOSPI 200 지수와 KOSPI 200 ESG 지수 비교")
st.markdown("## KOSPI 200 지수와 KOSPI 200 ESG 지수의 데이터프레임")

@st.cache(allow_output_mutation=True)
def load_data(file_path, encoding="utf-8"):
    file_format = os.path.splitext(file_path)
    if file_format == "csv":
        data = pd.read_csv(file_path, encoding=encoding)
        return data
    elif file_format == "parquet" or "gzip":
        df = pd.read_parquet(file_name, engine='python')
    else:
        raise Exception("data format err")
    return df
df = load_data(file_name)



col1, col2, col3 = st.columns(3)

with col1:
    options_list_11 = pd.read_csv(file_name).columns
    options_list_12 = ["일자"]
    options1 = st.multiselect('Index 선택', options_list_11, options_list_12)

with col2, col3:
    options_list_21 = pd.read_csv(file_name).columns
    options_list_22 = ["KOSPI 200 종가", "KOSPI 200 ESG 종가"]
    options2 = st.multiselect('Column 선택', options_list_21, options_list_22)


# if options1 == []:
#     st.dataframe(df)
# else:
#     st.dataframe(df[options2])


# df = df.pivot(index=[], columns="일자", values="KOSPI 200 종가")
df.groupby(['일자'], as_index=False).mean()
st.dataframe(df)


'''
['일자', 'KOSPI 200 종가', 'KOSPI 200 등락률', 'KOSPI 200 거래량',
       'KOSPI 200 ESG 종가', 'KOSPI 200 ESG 등락률', 'KOSPI 200 ESG 거래량', '연도',
       '연도월', '분기']
'''