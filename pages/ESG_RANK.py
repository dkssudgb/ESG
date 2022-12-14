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
    page_icon="๐",
    layout="wide",
)

st.markdown("# ESG ๋ฑ๊ธ ๋ถํฌ ์๊ฐํ")

file_name = "./data/ESG_KOSPI200_ca.csv"

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

data = load_data(file_name)

st.markdown("## ์ข๋ชฉ๋ณ ESG ๋ฑ๊ธ")
st.dataframe(data.fillna({"ESG๋ฑ๊ธ":"์์", "ํ๊ฒฝ": "์์", "์ฌํ":"์์", "์ง๋ฐฐ๊ตฌ์กฐ":"์์"}))

st.markdown("## ์๊ฐํ")

df_year_esg = data[['ํ๊ฐ๋๋', 'ESG๋ฑ๊ธ']]
df_year_esg.groupby("ํ๊ฐ๋๋")["ESG๋ฑ๊ธ"].value_counts().unstack()
df_year = data.groupby(["ํ๊ฐ๋๋", "ESG๋ฑ๊ธ"])["ESG๋ฑ๊ธ"].count().unstack().reset_index()
df_eco = data.groupby(["ํ๊ฐ๋๋", "ํ๊ฒฝ"])["ํ๊ฒฝ"].count().unstack().reset_index()
df_social = data.groupby(["ํ๊ฐ๋๋", "์ฌํ"])["์ฌํ"].count().unstack().reset_index()
df_g = data.groupby(["ํ๊ฐ๋๋", "์ง๋ฐฐ๊ตฌ์กฐ"])["์ง๋ฐฐ๊ตฌ์กฐ"].count().unstack().reset_index()

def draw_group_barchart(df,main_category,sub_category,fig_width=10,fig_height=5, \
                        bar_type='vertical', between_bar_padding=0.85,\
                        within_bar_padding=0.8, config_bar=None):
    
    # %matplotlib inline 

    num_sub_category = len(sub_category) ## ์๋ธ ์นดํ๊ณ ๋ฆฌ ๊ฐ์

    fig = plt.figure(figsize=(fig_width,fig_height)) ## ์บ๋ฒ์ค ์์ฑ
    fig.set_facecolor('white') ## ์บ๋ฒ์ค ์์ ์ง์ 
    ax = fig.add_subplot() ## ๊ทธ๋ฆผ์ด ๊ทธ๋ ค์ง ์ถ์ ์์ฑ
    
    colors = sns.color_palette('hls',num_sub_category) ## ๋ง๋๊ธฐ ์์ ์ง์ 
    
    tick_label = list(df[main_category].unique()) ## ๋ฉ์ธ ์นดํ๊ณ ๋ฆฌ ๋ผ๋ฒจ ์์ฑ
    tick_number = len(tick_label) ## ๋ฉ์ธ ์นดํ๊ณ ๋ฆฌ ๋๊ธ ๊ฐ์
    
    tick_coord = np.arange(tick_number) ## ๋ฉ์ธ ์นดํ๊ณ ๋ฆฌ์์์ ์ฒซ๋ฒ์งธ ์๋ธ ์นดํ๊ณ ๋ฆฌ ๋ง๋๊ธฐ๊ฐ ๊ทธ๋ ค์ง๋ x์ขํ

    width = 1/num_sub_category*between_bar_padding ## ๋ง๋๊ธฐ ํญ ์ง์ 

    config_tick = dict()
    config_tick['ticks'] = [t + width*(num_sub_category-1)/2 for t in tick_coord] ## ๋ฉ์ธ ์นดํ๊ณ ๋ฆฌ ๋ผ๋ฒจ x์ขํ
    config_tick['labels'] = tick_label 

    if bar_type == 'vertical': ## ์์ง ๋ฐ ์ฐจํธ๋ฅผ ๊ทธ๋ฆฐ๋ค.
        plt.xticks(**config_tick) ## x์ถ ๋๊ธ ๋ผ๋ฒจ ์์ฑ

        for i in range(num_sub_category):
            if config_bar: ## ๋ฐ ์ฐจํธ ์ถ๊ฐ ์ต์์ด ์๋ ๊ฒฝ์ฐ
                ax.bar(tick_coord+width*i, df[sub_category[i]], \
                    width*within_bar_padding, label=sub_category[i], \
                       color=colors[i], **config_bar) ## ์์ง ๋ฐ ์ฐจํธ ์์ฑ
            else:
                ax.bar(tick_coord+width*i, df[sub_category[i]], \
                    width*within_bar_padding, label=sub_category[i], \
                    color=colors[i]) ## ์์ง ๋ฐ ์ฐจํธ ์์ฑ
#         plt.legend() ## ๋ฒ๋ก ์์ฑ
        plt.legend(bbox_to_anchor=(1, 1))
        plt.savefig('./fig/fig03.png',format='png',dpi=300)
        st.pyplot(fig)
    else: ## ์ํ ๋ฐ ์ฐจํธ๋ฅผ ๊ทธ๋ฆฐ๋ค.
        plt.yticks(**config_tick) ## x์ถ ๋๊ธ ๋ผ๋ฒจ ์์ฑ

        for i in range(num_sub_category):
            if config_bar: # ๋ฐ ์ฐจํธ ์ถ๊ฐ ์ต์์ด ์๋ ๊ฒฝ์ฐ
                ax.barh(tick_coord+width*i, df[sub_category[i]], \
                    width*within_bar_padding, label=sub_category[i], \
                        color=colors[i], **config_bar) ## ์ํ ๋ฐ ์ฐจํธ ์์ฑ
            else:
                ax.barh(tick_coord+width*i, df[sub_category[i]], \
                    width*within_bar_padding, label=sub_category[i], \
                    color=colors[i]) ## ์ํ ๋ฐ ์ฐจํธ ์์ฑ
        plt.legend(bbox_to_anchor=(1, 1))
        st.pyplot(fig)

all, e, s, g = st.tabs(["ESG ์ ์ฒด", "ํ๊ฒฝ(E)", "์ฌํ(S)", "์ง๋ฐฐ๊ตฌ์กฐ(G)"])

with all:
    st.markdown("#### ESG ํตํฉ ๋ฑ๊ธ๋ณ ๊ธฐ์ ๋ถํฌ")
    main_category = 'ํ๊ฐ๋๋' ## ๋ฉ์ธ ์นดํ๊ณ ๋ฆฌ ์ง์ 
    sub_category = ['A+', 'A', 'B+', 'B', 'B์ดํ', 'C'] ## ์๋ธ์นดํ๊ณ ๋ฆฌ ์ง์ 

    draw_group_barchart(df_year,main_category,sub_category,\
                            bar_type='vertical', between_bar_padding=0.85,\
                            within_bar_padding=0.9, config_bar = None)
    
with e:
    st.markdown("#### ํ๊ฒฝ(E) ๋ฑ๊ธ๋ณ ๊ธฐ์ ๋ถํฌ")
    main_category = 'ํ๊ฐ๋๋' ## ๋ฉ์ธ ์นดํ๊ณ ๋ฆฌ ์ง์ 
    sub_category = ['S', 'A+', 'A', 'B+', 'B+ ์ดํ', 'B', 'C', 'D'] ## ์๋ธ์นดํ๊ณ ๋ฆฌ ์ง์ 

    draw_group_barchart(df_eco,main_category,sub_category,\
                            bar_type='vertical', between_bar_padding=0.85,\
                            within_bar_padding=0.9, config_bar = None)
    
with s:
    st.markdown("#### ์ฌํ(S) ๋ฑ๊ธ๋ณ ๊ธฐ์ ๋ถํฌ")
    main_category = 'ํ๊ฐ๋๋' ## ๋ฉ์ธ ์นดํ๊ณ ๋ฆฌ ์ง์ 
    sub_category = ['A+', 'A', 'B+', 'B', 'B์ดํ', 'C', 'D'] ## ์๋ธ์นดํ๊ณ ๋ฆฌ ์ง์ 

    draw_group_barchart(df_social,main_category,sub_category,\
                            bar_type='vertical', between_bar_padding=0.85,\
                            within_bar_padding=0.9, config_bar = None)
    
with g:
    st.markdown("#### ์ง๋ฐฐ๊ตฌ์กฐ(G) ๋ฑ๊ธ๋ณ ๊ธฐ์ ๋ถํฌ")
    main_category = 'ํ๊ฐ๋๋' ## ๋ฉ์ธ ์นดํ๊ณ ๋ฆฌ ์ง์ 
    sub_category = ['A+', 'A', 'B+', 'B', 'B์ดํ', 'C', 'D'] ## ์๋ธ์นดํ๊ณ ๋ฆฌ ์ง์ 

    draw_group_barchart(df_g,main_category,sub_category,\
                            bar_type='vertical', between_bar_padding=0.85,\
                            within_bar_padding=0.9, config_bar = None)
    
