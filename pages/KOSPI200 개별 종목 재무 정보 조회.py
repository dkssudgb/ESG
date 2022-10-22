# import module ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import seaborn as sns
import streamlit as st

import koreanize_matplotlib

from glob import glob
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="📈",
    layout="wide",
)

file_name = "./data\KOSPI200_ESGrate.csv"

st.markdown("# KOSPI200 개별 종목 정보 조회")