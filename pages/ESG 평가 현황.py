import koreanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objs as go
import streamlit as st

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="📈",
    layout="wide",
)

st.write("평가기관 - 한국기업지배구조원(KCGS)")
st.write("2011년 이전까지는 지배구조(G) 평가만 실시해오다가 2011년부터 환경(E) 및 사회(S)부문을 추가하여 지금의 ESG평가가 수행되고 있다.")
st.write("2011년의 평가 등급을 통해 2012년부터 ESG 지수가 산출되었기 때문에 2011년의 ESG지수는 존재하지 않는다.")

st.markdown("# ESG 등급 분포 시각화")



file_name = "./data/ESG_KOSPI200_ca.csv"

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

data = load_data(file_name)
# st.dataframe(data)
data = data[~data["평가년도"].isnull()]
st.dataframe(data.fillna({"ESG등급":"없음", "환경": "없음", "사회":"없음", "지배구조":"없음"}))
# ESG등급 / 환경 / 사회 / 지배구조 / 
# 평가년도 null : 평가 안한 기업 => 표시 X
# ESG등급_ca / 환경_ca / 사회_ca / 지배구조_ca -> 결측치 어떻게 처리??

# plotly의 Bar그래프
trace1 = go.Bar(x=data['ESG등급'], y=data['종목명'],marker = {'color':'black'})
trace1 = [trace1]
layout = go.Layout(title='ESG등급 분포',font={'size':20})
fig = go.Figure(data=trace1, layout=layout)
fig.update_xaxes(categoryorder='category ascending')
st.plotly_chart(fig)

# pie 그래프
ko_esg=data[['종목명','ESG등급','환경','사회','지배구조']].drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
ko_esg.sort_values(by=['ESG등급'], ascending=True)
ko_grouped= ko_esg.groupby(['ESG등급']).count()

labels = ['A','A+','B','B+','C','D']
values = ko_grouped['종목명']
layout = go.Layout(title='ESG등급 분포', font={'size':20})
fig = go.Figure(data=[go.Pie(labels=labels, values=values)],layout=layout)
st.plotly_chart(fig)

# data.groupby("ESG등급")["종목명"].count().plot(kind="bar", rot=0)
