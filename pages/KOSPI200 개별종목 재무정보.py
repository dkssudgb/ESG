# import module ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import seaborn as sns
import streamlit as st

import koreanize_matplotlib

from glob import glob
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="📈",
    layout="wide",
)

file_name = "./data\finaStatInfo.csv.csv"
@st.cache(allow_output_mutation=True)
def load_data(file_path):
    df = pd.read_csv(file_path)
    df["종목코드"] = df["종목코드"].astype(str).apply(lambda x: x.zfill(6))
    return df
df = load_data(file_name)

st.markdown("# KOSPI200 개별 종목 정보 조회")
st.dataframe(df)