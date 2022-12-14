import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="π",
    layout="wide",
)

st.markdown("# KOSPI 200 μ§μμ KOSPI 200 ESG μ§μ λΉκ΅")
file_name = "./data/KOSPI_ESG_MERGE.csv"

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

data_merge = load_data(file_name)

st.markdown("### KOSPI 200 μ§μμ KOSPI 200 ESG μ§μμ λ°μ΄ν°νλ μ")
st.write("κΈ°κ°: 2011.01.03 ~ 2022.09.30")

st.dataframe(data_merge.iloc[:, :7].fillna("ν΄λΉμμ"))

st.write("β» 2011λ μ΄μ κΉμ§λ μ§λ°°κ΅¬μ‘°(G) νκ°λ§ μ€μν΄μ€λ€κ° 2011λλΆν° νκ²½(E) λ° μ¬ν(S)λΆλ¬Έμ μΆκ°νμ¬ μ§κΈμ ESGνκ°κ° μνλκ³  μλ€. ")
st.write("β» 2011λμ νκ° λ±κΈμ ν΅ν΄ 2012λλΆν° ESG μ§μκ° μ°μΆλμκΈ° λλ¬Έμ 2011λμ ESGμ§μλ μ‘΄μ¬νμ§ μλλ€.")

tab1, tab2 = st.tabs(["μ’κ°", "κ±°λλ"])

with tab1:
    st.write("\n")
    fig_close = plt.figure(figsize=(15, 5))
    plt.title("μ°λμλ³ μ’κ° λΉκ΅")
    sns.lineplot(data=data_merge, x="μ°λμ", y="KOSPI 200 μ’κ°", label="KOSPI 200 μ’κ°", ci=None)
    sns.lineplot(data=data_merge, x="μ°λμ", y="KOSPI 200 ESG μ’κ°", label="KOSPI 200 ESG μ’κ°", ci=None)
    st.pyplot(fig_close)

    # st.write("\nμκ΄κ΄κ³ νμ")
    # fig_close = plt.figure(figsize=(15, 15))
    # plt.title("μ’κ° λΉκ΅")
    # plt.xlabel('KOSPI 200')
    # plt.ylabel('KOSPI 200 ESG')
    # plt.scatter(data_merge['KOSPI 200 μ’κ°'], data_merge['KOSPI 200 ESG μ’κ°'])
    # st.pyplot(fig_close)

with tab2:
    st.write("\n")
    fig_volume = plt.figure(figsize=(15, 5))
    plt.title("μ°λμλ³ κ±°λλ λΉκ΅")
    sns.lineplot(data=data_merge, x="μ°λμ", y="KOSPI 200 κ±°λλ", label="KOSPI 200 κ±°λλ", ci=None)
    sns.lineplot(data=data_merge, x="μ°λμ", y="KOSPI 200 ESG κ±°λλ", label="KOSPI 200 ESG κ±°λλ", ci=None)
    st.pyplot(fig_volume)

    st.write("\n")
    fig_volume = plt.figure(figsize=(15, 5))
    plt.title("μ°λμλ³ κ±°λλ λΉκ΅2")
    sns.lineplot(data=data_merge[data_merge["μ°λ"] >= 2018], x="μ°λμ", y="KOSPI 200 κ±°λλ", label="KOSPI 200 κ±°λλ", ci=None)
    sns.lineplot(data=data_merge[data_merge["μ°λ"] >= 2018], x="μ°λμ", y="KOSPI 200 ESG κ±°λλ", label="KOSPI 200 ESG κ±°λλ", ci=None)
    st.pyplot(fig_volume)

