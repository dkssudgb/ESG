import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="📈",
    layout="wide",
)

file_name = "./data/KOSPI_ESG_MERGE.csv"

st.markdown("# KOSPI 200 지수와 KOSPI 200 ESG 지수 비교")
st.markdown("## KOSPI 200 지수와 KOSPI 200 ESG 지수의 데이터프레임")

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data
data_merge = load_data(file_name)

option = st.selectbox(
    '종목 선택',
    ('All', 'KOSPI 200 INDEX', 'KOSPI 200 ESG INDEX'))

st.write('You selected:', option)


options_list_1 = pd.read_csv(file_name).columns
options_list_2 = ["KOSPI 200 종가", "KOSPI 200 ESG 종가"]
options = st.multiselect('컬럼 선택', options_list_1, options_list_2)

data_merge = load_data(file_name)
st.dataframe(data_merge)

st.write(options)
