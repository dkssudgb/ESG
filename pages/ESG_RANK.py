import koreanize_matplotlib
import pandas as pd
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
# st.dataframe(data)
st.dataframe(data.fillna({"ESG등급":"없음", "환경": "없음", "사회":"없음", "지배구조":"없음"}))
# ESG등급 / 환경 / 사회 / 지배구조 / 
# 평가년도 null : 평가 안한 기업 
# data = data[~data["평가년도"].isnull()]
# ESG등급_ca / 환경_ca / 사회_ca / 지배구조_ca -> 결측치 어떻게 처리??

st.markdown("## 시각화")

all, e, s, g = st.tabs(["ESG 전체", "환경(E)", "사회(S)", "지배구조(G)"])

with all:
    # Bar그래프
    trace1 = go.Bar(x=data['ESG등급'], y=data['종목명'].value_counts(),marker = {'color':'cadetblue'})
    trace = [trace1]
    layout = go.Layout(title='ESG 통합 등급 분포 _ Bar 그래프',font={'size':15})
    fig = go.Figure(data=trace, layout=layout)
    fig.update_xaxes(categoryorder='category ascending')
    st.plotly_chart(fig)
    
    # pie 그래프
    ko_esg=data[['종목명','ESG등급','환경','사회','지배구조']].drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
    ko_esg.sort_values(by=['ESG등급'], ascending=True)
    ko_grouped= ko_esg.groupby(['ESG등급']).count()

    labels = ['A','A+','B','B+','C','D']
    values = ko_grouped['종목명']
    layout = go.Layout(title='ESG 통합 등급 분포 _ Pie 그래프', font={'size':15})
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)],layout=layout)
    st.plotly_chart(fig)
    
with e:
    # Bar그래프
    trace1 = go.Bar(x=data['환경'], y=data['종목명'].value_counts(),marker = {'color':'green'})
    trace = [trace1]
    layout = go.Layout(title='환경 등급 분포 _ Bar 그래프',font={'size':15})
    fig = go.Figure(data=trace, layout=layout)
    fig.update_xaxes(categoryorder='category ascending')
    st.plotly_chart(fig)
    
    # pie 그래프
    # ko_esg=data[['종목명','ESG등급','환경','사회','지배구조']].drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
    # ko_esg.sort_values(by=['ESG등급'], ascending=True)
    ko_e_grouped= data.groupby(['환경']).count()

    labels = ['A','A+','B','B+','C','D']
    values = ko_e_grouped['종목명']
    layout = go.Layout(title='환경 등급 분포 _ Pie 그래프', font={'size':15})
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)],layout=layout)
    st.plotly_chart(fig)
with s:
    # Bar그래프
    trace1 = go.Bar(x=data['사회'], y=data['종목명'].value_counts(),marker = {'color':'gray'})
    trace = [trace1]
    layout = go.Layout(title='사회 등급 분포 _ Bar 그래프',font={'size':15})
    fig = go.Figure(data=trace, layout=layout)
    fig.update_xaxes(categoryorder='category ascending')
    st.plotly_chart(fig)
    
    # pie 그래프
    ko_s_grouped= data.groupby(['사회']).count()

    labels = ['A','A+','B','B+','C','D']
    values = ko_s_grouped['종목명']
    layout = go.Layout(title='사회 등급 분포 _ Pie 그래프', font={'size':15})
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)],layout=layout)
    st.plotly_chart(fig)
with g:
    # Bar그래프
    trace1 = go.Bar(x=data['지배구조'], y=data['종목명'].value_counts(),marker = {'color':'sandybrown'})
    trace = [trace1]
    layout = go.Layout(title='지배구조 등급 분포 _ Bar 그래프',font={'size':15})
    fig = go.Figure(data=trace, layout=layout)
    fig.update_xaxes(categoryorder='category ascending')
    st.plotly_chart(fig)
    
    # pie 그래프
    ko_g_grouped= data.groupby(['지배구조']).count()

    labels = ['A','A+','B','B+','C','D']
    values = ko_g_grouped['종목명']
    layout = go.Layout(title='지배구조 등급 분포 _ Pie 그래프', font={'size':15})
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)],layout=layout)
    st.plotly_chart(fig)
