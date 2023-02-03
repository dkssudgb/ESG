import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Likelion AI School Midproject Team13",
    page_icon="📈",
    layout="wide",
)

st.title('ESG')

img = Image.open("./fig/esg.png")
st.image(img)

st.markdown("")
st.markdown("""#### ESG는 환경(Environmental), 사회(Social), 기업 지배구조(corporate Governance)를 말하며 
            \n#### 기업이나 비즈니스에 대한 투자의 지속 가능성과 사회에 미치는 영향을 측정하는 세 가지 핵심 요소입니다.""")

st.markdown("")
st.markdown("")

st.title('ESG의 중요성')

st.markdown("""### 소비자들의 인식이 변화하고 있습니다.
            \n ##### 2021년 대한상의 조사에 따르면 60%가 넘는 소비자들이 제품 구매 시 ESG 활동을 고려한다고 응답한 것을 확인할 수 있습니다.
            \n ##### 가격이 다소 높더라도 ESG 우수 기업의 제품을 구매하려 하고, ESG 활동에 부정적인 기업의 제품은 불매하는 소비자들이 많아졌습니다.""")

col1, col2 = st.columns(2)
with col1:
    img = Image.open("./fig/esg_imp1.png")
    st.image(img)
with col2:
    img = Image.open("./fig/esg_imp2.png")
    st.image(img)

st.markdown("")
st.markdown("""#### 우리나라의 ESG 경영 실패 사례를 살펴보면,""")
col1, mid, col2 = st.columns([0.48, 0.04, 0.48])
with col1:
    img = Image.open("./fig/purmil.png")
    st.image(img)
    st.markdown("""##### 사업 종료 위험에 처했었던 푸르밀 기업은 2018년 대표가 바뀌면서 '오너 경영 실패'가 사업 종료의 가장 큰 배경이 되었다는 시각이 지배적이었습니다.
            \n ##### 이는 ESG항목 중 지배구조에 소홀했던 사례로 볼 수 있습니다.""")
with col2:
    st.markdown("")
    st.markdown("")
    img = Image.open("./fig/namyang.png")
    st.image(img)
    st.markdown("")
    st.markdown("")
    st.markdown("""##### '불가리스 사태', '온라인 비방 댓글 사태'와 같이 논란이 많았던 남양유업도 ESG 활동에 부정적인 사례로 볼 수 있습니다.
            \n ##### 이는 ESG항목 중 사회 항목에 소홀했던 사례입니다.""")

st.markdown("")
st.markdown("")

st.title('ESG에 대한 전망')
st.write("ESG는 투자자들에게 많은 관심을 받고 있는 추세로 보입니다. 이에 따라 회사 경영에서 ESG를 고려할 뿐만 아니라, 많은 연구들에서도 ESG를 통한 투자가 수익률이 뒤떨어지지 않고 투자의 안정성을 고무시키는 것으로 보고 있습니다.")



st.markdown("")
st.markdown("")
st.markdown("""##### reference 
            \n- [ESG포털](https://esg.krx.co.kr/contents/01/01010100/ESG01010100.jsp)
            \n- [위키백과:환경, 사회, 기업 지배구조](https://ko.wikipedia.org/wiki/%ED%99%98%EA%B2%BD,_%EC%82%AC%ED%9A%8C,_%EA%B8%B0%EC%97%85_%EC%A7%80%EB%B0%B0%EA%B5%AC%EC%A1%B0)""")
st.markdown("""- [박준신, 안재준 and 오경주. (2021). 코로나19 이후 ESG 투자 전략 평가: ESG 인덱스 성과를 중심으로. 지식경영연구, 22(4), 87-101.](http://doi.org/10.15813/kmr.2021.22.4.005)""")
