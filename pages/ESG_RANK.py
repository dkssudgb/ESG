import koreanize_matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as pyo
import plotly.graph_objs as go
import streamlit as st

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="📈",
    layout="wide",
)

st.markdown("# ESG 등급 분포 시각화")

file_name = "./data/ESG_KOSPI200_ca.csv"

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

data = load_data(file_name)

st.markdown("## 종목별 ESG 등급")
st.dataframe(data.fillna({"ESG등급":"없음", "환경": "없음", "사회":"없음", "지배구조":"없음"}))

st.markdown("## 시각화")

df_year_esg = data[['평가년도', 'ESG등급']]
df_year_esg.groupby("평가년도")["ESG등급"].value_counts().unstack()
df_year = data.groupby(["평가년도", "ESG등급"])["ESG등급"].count().unstack().reset_index()
df_eco = data.groupby(["평가년도", "환경"])["환경"].count().unstack().reset_index()
df_social = data.groupby(["평가년도", "사회"])["사회"].count().unstack().reset_index()
df_g = data.groupby(["평가년도", "지배구조"])["지배구조"].count().unstack().reset_index()

def draw_group_barchart(df,main_category,sub_category,fig_width=10,fig_height=5, \
                        bar_type='vertical', between_bar_padding=0.85,\
                        within_bar_padding=0.8, config_bar=None):
    
    # %matplotlib inline 

    num_sub_category = len(sub_category) ## 서브 카테고리 개수

    fig = plt.figure(figsize=(fig_width,fig_height)) ## 캔버스 생성
    fig.set_facecolor('white') ## 캔버스 색상 지정
    ax = fig.add_subplot() ## 그림이 그려질 축을 생성
    
    colors = sns.color_palette('hls',num_sub_category) ## 막대기 색상 지정
    
    tick_label = list(df[main_category].unique()) ## 메인 카테고리 라벨 생성
    tick_number = len(tick_label) ## 메인 카테고리 눈금 개수
    
    tick_coord = np.arange(tick_number) ## 메인 카테고리안에서 첫번째 서브 카테고리 막대기가 그려지는 x좌표

    width = 1/num_sub_category*between_bar_padding ## 막대기 폭 지정

    config_tick = dict()
    config_tick['ticks'] = [t + width*(num_sub_category-1)/2 for t in tick_coord] ## 메인 카테고리 라벨 x좌표
    config_tick['labels'] = tick_label 

    if bar_type == 'vertical': ## 수직 바 차트를 그린다.
        plt.xticks(**config_tick) ## x축 눈금 라벨 생성

        for i in range(num_sub_category):
            if config_bar: ## 바 차트 추가 옵션이 있는 경우
                ax.bar(tick_coord+width*i, df[sub_category[i]], \
                    width*within_bar_padding, label=sub_category[i], \
                       color=colors[i], **config_bar) ## 수직 바 차트 생성
            else:
                ax.bar(tick_coord+width*i, df[sub_category[i]], \
                    width*within_bar_padding, label=sub_category[i], \
                    color=colors[i]) ## 수직 바 차트 생성
#         plt.legend() ## 범례 생성
        plt.legend(bbox_to_anchor=(1, 1))
        plt.savefig('./fig/fig03.png',format='png',dpi=300)
        st.pyplot(fig)
    else: ## 수평 바 차트를 그린다.
        plt.yticks(**config_tick) ## x축 눈금 라벨 생성

        for i in range(num_sub_category):
            if config_bar: # 바 차트 추가 옵션이 있는 경우
                ax.barh(tick_coord+width*i, df[sub_category[i]], \
                    width*within_bar_padding, label=sub_category[i], \
                        color=colors[i], **config_bar) ## 수평 바 차트 생성
            else:
                ax.barh(tick_coord+width*i, df[sub_category[i]], \
                    width*within_bar_padding, label=sub_category[i], \
                    color=colors[i]) ## 수평 바 차트 생성
        plt.legend(bbox_to_anchor=(1, 1))
        st.pyplot(fig)

all, e, s, g = st.tabs(["ESG 전체", "환경(E)", "사회(S)", "지배구조(G)"])

with all:
    st.markdown("#### ESG 통합 등급별 기업 분포")
    main_category = '평가년도' ## 메인 카테고리 지정
    sub_category = ['A+', 'A', 'B+', 'B', 'B이하', 'C'] ## 서브카테고리 지정

    draw_group_barchart(df_year,main_category,sub_category,\
                            bar_type='vertical', between_bar_padding=0.85,\
                            within_bar_padding=0.9, config_bar = None)
    
with e:
    st.markdown("#### 환경(E) 등급별 기업 분포")
    main_category = '평가년도' ## 메인 카테고리 지정
    sub_category = ['S', 'A+', 'A', 'B+', 'B+ 이하', 'B', 'C', 'D'] ## 서브카테고리 지정

    draw_group_barchart(df_eco,main_category,sub_category,\
                            bar_type='vertical', between_bar_padding=0.85,\
                            within_bar_padding=0.9, config_bar = None)
    
with s:
    st.markdown("#### 사회(S) 등급별 기업 분포")
    main_category = '평가년도' ## 메인 카테고리 지정
    sub_category = ['A+', 'A', 'B+', 'B', 'B이하', 'C', 'D'] ## 서브카테고리 지정

    draw_group_barchart(df_social,main_category,sub_category,\
                            bar_type='vertical', between_bar_padding=0.85,\
                            within_bar_padding=0.9, config_bar = None)
    
with g:
    st.markdown("#### 지배구조(G) 등급별 기업 분포")
    main_category = '평가년도' ## 메인 카테고리 지정
    sub_category = ['A+', 'A', 'B+', 'B', 'B이하', 'C', 'D'] ## 서브카테고리 지정

    draw_group_barchart(df_g,main_category,sub_category,\
                            bar_type='vertical', between_bar_padding=0.85,\
                            within_bar_padding=0.9, config_bar = None)
    
