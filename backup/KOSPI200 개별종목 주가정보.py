# import module ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import seaborn as sns
import streamlit as st

# import koreanize_matplotlib
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="📈",
    layout="wide",
)

file_name = r"./data/KOSPI200_ESGrate.csv"

st.markdown("# KOSPI200 개별종목 주가정보")


@st.cache(allow_output_mutation=True)
def load_data(file_path):
    df = pd.read_csv(file_path)
    df["종목코드"] = df["종목코드"].astype(str).apply(lambda x: x.zfill(6))
    df[['종가', '시가', '고가', '저가', '거래량']] = df[['종가', '시가', '고가', '저가', '거래량']].astype("uint64")
    df["등락률"] = df["등락률"].apply(lambda x: round(x, 1))
    return df
df = load_data(file_name)
col1, col2 = st.columns(2)

with col1:
    options_list_11 = ['일자', "연도", "연도월", '종목코드', '종목명', 'ESG_종합', 'ESG_환경', 'ESG_사회', 'ESG_지배구조']
    options_list_12 = ["종목코드","종목명","일자"]
    options1 = st.multiselect('INDEX', options_list_11, options_list_12)

with col2:
    options_list_21 = ['일자', "연도", "연도월", '종목코드', '종목명', '종가', '시가', '고가', '저가', '등락률', '거래량', 'ESG_종합', 'ESG_환경', 'ESG_사회', 'ESG_지배구조']
    options_list_22 = ["종가", "등락률", "거래량","ESG_종합"]
    options2 = st.multiselect('COLUMN', options_list_21, options_list_22)


dict_agg = {'일자': "count", "연도": "count", "연도월": "count", '종목코드': lambda x:x.mode(), '종목명': lambda x:x.mode(), 
            '종가': lambda x: np.mean(x), '시가': 'mean', '고가': 'mean', '저가': 'mean', '등락률': 'mean', '거래량': np.sum, 
            'ESG_종합': lambda x:x.mode(), 'ESG_환경': lambda x:x.mode(), 'ESG_사회': lambda x:x.mode(), 'ESG_지배구조': lambda x:x.mode()}

def fn(dict):
    tmp = {}
    for k, v in dict_agg.items():
        if k in options2:
            tmp[k] = v
    return tmp

df = df.groupby(options1)[options2].aggregate(fn(dict_agg))
st.dataframe(df)

# columns
# ['일자', '종목코드', '종목명', '종가', '시가', '고가', '저가', '등락률', '거래량', 'ESG_종합',
#        'ESG_환경', 'ESG_사회', 'ESG_지배구조', 'ESG_종합_num', 'ESG_환경_num',
#        'ESG_사회_num', 'ESG_지배구조_num', '연도월', '연도']

# fig = px.