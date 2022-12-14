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

tab1, tab2, tab3 = st.tabs(["μ’κ°", "λ±λ½λ₯ ", "κ±°λλ"])

with tab1:
    st.write("\n")
    fig_close = plt.figure(figsize=(15, 5))
    plt.title("μ°λμλ³ μ’κ° λΉκ΅ (2019λ~)")
    sns.lineplot(data=data_merge[1969:], x="μ°λμ", y="KOSPI 200 μ’κ°", label="KOSPI 200 μ’κ°", errorbar=None)
    sns.lineplot(data=data_merge[1969:], x="μ°λμ", y="KOSPI 200 ESG μ’κ°", label="KOSPI 200 ESG μ’κ°", errorbar=None)
    st.pyplot(fig_close)
    
    st.write("β» 2012λ 1μ 2μΌμ κΈ°μ€μΌλ‘ μ½μ€νΌ 200 μ§μ μ λλ²μ€μ μ μ©νμ¬ 2018λ 12μ 24μΌλΆν° μ§μκ° μ°μΆλμλ€.")
    
    st.write("\n")
    fig_close = plt.figure(figsize=(15, 5))
    plt.title("μ°λμλ³ μ’κ° λΉκ΅ (2011λ~)")
    sns.lineplot(data=data_merge, x="μ°λμ", y="KOSPI 200 μ’κ°", label="KOSPI 200 μ’κ°", errorbar=None)
    sns.lineplot(data=data_merge, x="μ°λμ", y="KOSPI 200 ESG μ’κ°", label="KOSPI 200 ESG μ’κ°", errorbar=None)
    st.pyplot(fig_close)
    
with tab2:
    kospi_max = data_merge[data_merge["KOSPI 200 λ±λ½λ₯ "] == data_merge["KOSPI 200 λ±λ½λ₯ "].max()].iloc[0]["KOSPI 200 λ±λ½λ₯ "]
    kospi_min = data_merge[data_merge["KOSPI 200 λ±λ½λ₯ "] == data_merge["KOSPI 200 λ±λ½λ₯ "].min()].iloc[0]["KOSPI 200 λ±λ½λ₯ "]

    esg_max = data_merge[data_merge["KOSPI 200 ESG λ±λ½λ₯ "] == data_merge["KOSPI 200 ESG λ±λ½λ₯ "].max()].iloc[0]["KOSPI 200 ESG λ±λ½λ₯ "]
    esg_min = data_merge[data_merge["KOSPI 200 ESG λ±λ½λ₯ "] == data_merge["KOSPI 200 ESG λ±λ½λ₯ "].min()].iloc[0]["KOSPI 200 ESG λ±λ½λ₯ "]

    df_norm = pd.concat([data_merge["μΌμ"], data_merge["μ°λμ"], (data_merge["KOSPI 200 λ±λ½λ₯ "] - kospi_min) / (kospi_max - kospi_min), (data_merge["KOSPI 200 ESG λ±λ½λ₯ "] - esg_min) / (esg_max - esg_min)], axis=1)
    df_norm.columns = ["μΌμ", "μ°λμ", "μ½μ€νΌ λ±λ½λ₯  μ κ·ν", "ESG λ±λ½λ₯  μ κ·ν"]
    
    st.write("\n")
    fig_change = plt.figure(figsize=(25, 5))
    plt.title("μ°λμλ³ λ±λ½λ₯  λΉκ΅ (2019λ~)")
    sns.lineplot(data=df_norm[1969:], x="μ°λμ", y="μ½μ€νΌ λ±λ½λ₯  μ κ·ν", label="KOSPI 200 λ±λ½λ₯ ", errorbar=None)
    sns.lineplot(data=df_norm[1969:], x="μ°λμ", y="ESG λ±λ½λ₯  μ κ·ν", label="KOSPI 200 ESG λ±λ½λ₯ ", errorbar=None)
    st.pyplot(fig_change)
    
    st.write("\n")
    fig_change = plt.figure(figsize=(25, 5))
    plt.title("μ°λμλ³ λ±λ½λ₯  λΉκ΅ (2011λ~)")
    sns.lineplot(data=df_norm, x="μ°λμ", y="μ½μ€νΌ λ±λ½λ₯  μ κ·ν", label="KOSPI 200 λ±λ½λ₯ ", errorbar=None)
    sns.lineplot(data=df_norm, x="μ°λμ", y="ESG λ±λ½λ₯  μ κ·ν", label="KOSPI 200 ESG λ±λ½λ₯ ", errorbar=None)
    st.pyplot(fig_change)

with tab3:
    st.write("\n")
    fig_volume = plt.figure(figsize=(15, 5))
    plt.title("μ°λμλ³ κ±°λλ λΉκ΅ (2018λ~)")
    sns.lineplot(data=data_merge[data_merge["μ°λ"] >= 2018], x="μ°λμ", y="KOSPI 200 κ±°λλ", label="KOSPI 200 κ±°λλ", errorbar=None)
    sns.lineplot(data=data_merge[data_merge["μ°λ"] >= 2018], x="μ°λμ", y="KOSPI 200 ESG κ±°λλ", label="KOSPI 200 ESG κ±°λλ", errorbar=None)
    st.pyplot(fig_volume)
    
    st.write("\n")
    fig_volume = plt.figure(figsize=(15, 5))
    plt.title("μ°λμλ³ κ±°λλ λΉκ΅ (2011λ~)")
    sns.lineplot(data=data_merge, x="μ°λμ", y="KOSPI 200 κ±°λλ", label="KOSPI 200 κ±°λλ", errorbar=None)
    sns.lineplot(data=data_merge, x="μ°λμ", y="KOSPI 200 ESG κ±°λλ", label="KOSPI 200 ESG κ±°λλ", errorbar=None)
    st.pyplot(fig_volume)

