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

st.markdown("# KOSPI 200 지수와 KOSPI 200 ESG 지수 비교")
file_name = "./data/KOSPI_ESG_MERGE.csv"

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

data_merge = load_data(file_name)

st.markdown("### KOSPI 200 지수와 KOSPI 200 ESG 지수의 데이터프레임")
st.write("기간: 2011.01.03 ~ 2022.09.30")

st.dataframe(data_merge.iloc[:, :7].fillna("해당없음"))

st.write("※ 2011년 이전까지는 지배구조(G) 평가만 실시해오다가 2011년부터 환경(E) 및 사회(S)부문을 추가하여 지금의 ESG평가가 수행되고 있다. ")
st.write("※ 2011년의 평가 등급을 통해 2012년부터 ESG 지수가 산출되었기 때문에 2011년의 ESG지수는 존재하지 않는다.")

tab1, tab2, tab3 = st.tabs(["종가", "등락률", "거래량"])

with tab1:
    st.write("\n")
    fig_close = plt.figure(figsize=(15, 5))
    plt.title("연도월별 종가 비교")
    sns.lineplot(data=data_merge, x="연도월", y="KOSPI 200 종가", label="KOSPI 200 종가", ci=None)
    sns.lineplot(data=data_merge, x="연도월", y="KOSPI 200 ESG 종가", label="KOSPI 200 ESG 종가", ci=None)
    st.pyplot(fig_close)
    
with tab2:
    kospi_max = data_merge[data_merge["KOSPI 200 등락률"] == data_merge["KOSPI 200 등락률"].max()].iloc[0]["KOSPI 200 등락률"]
    kospi_min = data_merge[data_merge["KOSPI 200 등락률"] == data_merge["KOSPI 200 등락률"].min()].iloc[0]["KOSPI 200 등락률"]

    esg_max = data_merge[data_merge["KOSPI 200 ESG 등락률"] == data_merge["KOSPI 200 ESG 등락률"].max()].iloc[0]["KOSPI 200 ESG 등락률"]
    esg_min = data_merge[data_merge["KOSPI 200 ESG 등락률"] == data_merge["KOSPI 200 ESG 등락률"].min()].iloc[0]["KOSPI 200 ESG 등락률"]

    df_norm = pd.concat([data_merge["일자"], data_merge["연도월"], (data_merge["KOSPI 200 등락률"] - kospi_min) / (kospi_max - kospi_min), (data_merge["KOSPI 200 ESG 등락률"] - esg_min) / (esg_max - esg_min)], axis=1)
    df_norm.columns = ["일자", "연도월", "코스피 등락률 정규화", "ESG 등락률 정규화"]
    
    st.write("\n")
    fig_change = plt.figure(figsize=(25, 5))
    plt.title("연도월별 등락률 비교")
    plt.xticks(rotation=90)
    sns.lineplot(data=df_norm, x="연도월", y="코스피 등락률 정규화", label="KOSPI 200 등락률", ci=None)
    sns.lineplot(data=df_norm, x="연도월", y="ESG 등락률 정규화", label="KOSPI 200 ESG 등락률", ci=None)
    st.pyplot(fig_change)

with tab3:
    st.write("\n")
    fig_volume = plt.figure(figsize=(15, 5))
    plt.title("연도월별 거래량 비교")
    sns.lineplot(data=data_merge, x="연도월", y="KOSPI 200 거래량", label="KOSPI 200 거래량", ci=None)
    sns.lineplot(data=data_merge, x="연도월", y="KOSPI 200 ESG 거래량", label="KOSPI 200 ESG 거래량", ci=None)
    st.pyplot(fig_volume)

    st.write("\n")
    fig_volume = plt.figure(figsize=(15, 5))
    plt.title("연도월별 거래량 비교2")
    sns.lineplot(data=data_merge[data_merge["연도"] >= 2018], x="연도월", y="KOSPI 200 거래량", label="KOSPI 200 거래량", ci=None)
    sns.lineplot(data=data_merge[data_merge["연도"] >= 2018], x="연도월", y="KOSPI 200 ESG 거래량", label="KOSPI 200 ESG 거래량", ci=None)
    st.pyplot(fig_volume)

