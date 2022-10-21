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

st.markdown("# KOSPI 200 ESG 지수")
st.sidebar.markdown("# 시각화 📊")

file_name = "data\KOSPI200_ESG.csv"

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

data_load_state = st.text('Loading data...')
# data_zero = load_data(file_names[0])
data = load_data(file_name) # 결측치를 0으로 대체한 파일로 사용
data_load_state.text("Done! (using st.cache)")

st.dataframe(data)

# 종가, 거래량, 등락률 중 선택
standard = ["None", "종가", "거래량", "등락률"]
selected_standard = st.sidebar.selectbox("시각화할 column", standard) 

# 기준 날짜 선택
v_list = ["None", "전체 날짜에 대한 시각화", "연도별 시각화", "연도-월별 시각화"]
selected_v = st.sidebar.selectbox("시각화 기준", v_list)

def visualize(s, v):    # selectbox 동작 함수
    if v == v_list[0]:
        pass
    elif v == v_list[1]:
        st.line_chart(data.set_index("일자")[s])
    elif selected_v == v_list[2]:
        fig = plt.figure(figsize=(20, 5))
        sns.lineplot(data=data, x="연도", y=s, ci=None)
        st.pyplot(fig)
    else:
        fig = plt.figure(figsize=(20, 5))
        sns.lineplot(data=data, x="연도월", y=s, ci=None)
        st.pyplot(fig)
        
visualize(selected_standard, selected_v)
