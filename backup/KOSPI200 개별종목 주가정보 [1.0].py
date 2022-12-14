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
    page_icon="๐",
    layout="wide",
)

file_name = r"./data/KOSPI200_ESGrate.csv"

st.markdown("# KOSPI200 ๊ฐ๋ณ์ข๋ชฉ ์ฃผ๊ฐ์ ๋ณด")


@st.cache(allow_output_mutation=True)
def load_data(file_path):
    df = pd.read_csv(file_path)
    df["์ข๋ชฉ์ฝ๋"] = df["์ข๋ชฉ์ฝ๋"].astype(str).apply(lambda x: x.zfill(6))
    df[['์ข๊ฐ', '์๊ฐ', '๊ณ ๊ฐ', '์ ๊ฐ', '๊ฑฐ๋๋']] = df[['์ข๊ฐ', '์๊ฐ', '๊ณ ๊ฐ', '์ ๊ฐ', '๊ฑฐ๋๋']].astype("uint64")
    df["๋ฑ๋ฝ๋ฅ "] = df["๋ฑ๋ฝ๋ฅ "].apply(lambda x: round(x, 1))
    return df
df = load_data(file_name)
col1, col2 = st.columns(2)

with col1:
    options_list_11 = ['์ผ์', "์ฐ๋", "์ฐ๋์", '์ข๋ชฉ์ฝ๋', '์ข๋ชฉ๋ช', 'ESG_์ขํฉ', 'ESG_ํ๊ฒฝ', 'ESG_์ฌํ', 'ESG_์ง๋ฐฐ๊ตฌ์กฐ']
    options_list_12 = ["์ข๋ชฉ์ฝ๋","์ข๋ชฉ๋ช","์ผ์"]
    options1 = st.multiselect('INDEX', options_list_11, options_list_12)

with col2:
    options_list_21 = ['์ผ์', "์ฐ๋", "์ฐ๋์", '์ข๋ชฉ์ฝ๋', '์ข๋ชฉ๋ช', '์ข๊ฐ', '์๊ฐ', '๊ณ ๊ฐ', '์ ๊ฐ', '๋ฑ๋ฝ๋ฅ ', '๊ฑฐ๋๋', 'ESG_์ขํฉ', 'ESG_ํ๊ฒฝ', 'ESG_์ฌํ', 'ESG_์ง๋ฐฐ๊ตฌ์กฐ']
    options_list_22 = ["์ข๊ฐ", "๋ฑ๋ฝ๋ฅ ", "๊ฑฐ๋๋","ESG_์ขํฉ"]
    options2 = st.multiselect('COLUMN', options_list_21, options_list_22)


dict_agg = {'์ผ์': "count", "์ฐ๋": "count", "์ฐ๋์": "count", '์ข๋ชฉ์ฝ๋': lambda x:x.mode(), '์ข๋ชฉ๋ช': lambda x:x.mode(), 
            '์ข๊ฐ': lambda x: np.mean(x), '์๊ฐ': 'mean', '๊ณ ๊ฐ': 'mean', '์ ๊ฐ': 'mean', '๋ฑ๋ฝ๋ฅ ': 'mean', '๊ฑฐ๋๋': np.sum, 
            'ESG_์ขํฉ': lambda x:x.mode(), 'ESG_ํ๊ฒฝ': lambda x:x.mode(), 'ESG_์ฌํ': lambda x:x.mode(), 'ESG_์ง๋ฐฐ๊ตฌ์กฐ': lambda x:x.mode()}

def fn(dict):
    tmp = {}
    for k, v in dict_agg.items():
        if k in options2:
            tmp[k] = v
    return tmp

df = df.groupby(options1)[options2].aggregate(fn(dict_agg))
st.dataframe(df)

# columns
# ['์ผ์', '์ข๋ชฉ์ฝ๋', '์ข๋ชฉ๋ช', '์ข๊ฐ', '์๊ฐ', '๊ณ ๊ฐ', '์ ๊ฐ', '๋ฑ๋ฝ๋ฅ ', '๊ฑฐ๋๋', 'ESG_์ขํฉ',
#        'ESG_ํ๊ฒฝ', 'ESG_์ฌํ', 'ESG_์ง๋ฐฐ๊ตฌ์กฐ', 'ESG_์ขํฉ_num', 'ESG_ํ๊ฒฝ_num',
#        'ESG_์ฌํ_num', 'ESG_์ง๋ฐฐ๊ตฌ์กฐ_num', '์ฐ๋์', '์ฐ๋']

# fig = px.