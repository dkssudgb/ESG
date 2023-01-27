# ESG평가가 기업 가치 측정의 기준으로 적절한가?

## 팀원
|팀원|역할|
|:---:|:---:|
|<span style="color:blue">[조현준(팀장)](https://github.com/chohj118)|데이터 수집 · 전처리 · 시각화(코스피200 기업 주가), PPT, 발표|
|<span style="color:blue">[이혜빈](https://github.com/dkssudgb)|데이터 수집 · 전처리 · 시각화(코스피200 기업 ESG지수)| 
|<span style="color:blue">[박성용](https://github.com/Sankamita3131)|데이터 수집 · 전처리 · 시각화(재무제표, 코스피200 개별 종목 ESG 평가 전처리)| 
|<span style="color:blue">노나은|데이터 수집 · 전처리 · 시각화(ESG 평가등급, 네이버 ESG 관련 뉴스기사)| 
|<span style="color:blue">이주민|데이터 수집 · 전처리 · 시각화(코스피200), PPT|

## 주제 선정 이유
<img src="https://user-images.githubusercontent.com/115917627/215085827-099c5fe3-cf75-4bb8-8994-3704188a7ac0.png" weight="1000" height="400">

```
과거에는 기업들이 돈을 얼마나 벌 수 있는지를 중점에 두고 투자를 하거나 기업을 평가 해왔습니다. 하지만 최근 기상이변이나 코로나19 같이 
돈으로 환산하기 힘들고 예상하기 어려운 위기상황에 기업이 대처할 수 있는 능력을 파악하기 위해 ESG 등급을 기준으로 평가하고 있습니다.
저희 팀에서는 한국 ESG 기준원과 KRX 정보데이터시스템에서 기업의 ESG 평가등급을 가져와 코스피200 지수,기업의 주가데이터와 비교해
ESG 등급이 기업을 평가하는데 적절한지 알아보았습니다.
```
## 프로젝트 활용 방안
- 기업들의 ESG 평가 등급 개선을 유도하는 하나의 기준으로써 활용
- 취업준비생이 지원하는 기업의 미래 가치를 평가하는 데 활용
- 투자자들에게 투자 기업의 미래 주가 흐름을 예측할 수 있는 지표로 활용

## 가설 설정
**ESG가 기업의 가치 평가에 적절한가**

- **KOSPI200 지수**와 **KOSPI200 ESG 지수** 비교

- **ESG 평가**와 **기업 주가** 비교

## **KOSPI200 지수**와 **KOSPI200 ESG 지수** 비교

<img src="https://user-images.githubusercontent.com/115917627/215096247-b7a7439c-6b2e-4d69-b4f8-190b0a8f74bc.png" weight="200" height="400">

- 연도별 종가 비교 : KOSPI200 ESG 종가를 산출하기 시작한 2019년 기준으로 보면 두 지수의 변화 추이는 비슷하지만 ESG 평가를 추가한 ESG 지수가 더 높은 종가를 보여주고 있는데, 이는 코스피200ESG지수가 상대적으로 우량한 기업의 영향을 더 받기 때문으로 보인다.
 
<img src="https://user-images.githubusercontent.com/115917627/215096480-c14b24ec-b7f9-4515-a2e0-027f385c3fcb.png" weight="200" height="400">

- 연도별 등락률 비교: 두 지수간의 등락률은 매우 유사하게 움직이는 것으로 보인다.
 
<img src="https://user-images.githubusercontent.com/115917627/215096655-fa8e5536-0bda-4987-871e-c66c6709bd19.png" weight="200" height="400">

- 연도별 거래량 비교: 두 지수의 변화 추이는 비슷한 것으로 보입니다.

## **ESG 평가**와 **기업 주가** 비교

<img src="https://user-images.githubusercontent.com/115917627/215100517-1732ef36-6e72-4f02-95ae-bff03cc6675f.png" weight="200" height="300">

- 환경에 대한 기업들의 관심은 이전에도 높은 편이였기 때문에 ESG 평가 초기에도 높은 등급을 유지하다 잠시 주춤한 뒤 전체적으로 등급이 상승하는 모습을 보여주고 있습니다.

<img src="https://user-images.githubusercontent.com/115917627/215100541-16cd7244-5813-49b3-b513-b1255b59cbe8.png" weight="200" height="300">

- 사회적 책임에 대한 기업 등급 분포를 확인해보면 ESG 평가 초기에는 낮은 등급을 유지하다 2015년을 기점으로 상승하는 모습을 볼 수 있습니다.

<img src="https://user-images.githubusercontent.com/115917627/215100568-4cea7313-229f-4bb8-b7cd-675ddcd5d4e8.png" weight="200" height="300">

- 지배구조 역시 ESG 평가 초기에는 기업들이 크게 등급에 신경을 쓰지 않았지만 코스피 200 ESG 지수를 산출하기 시작한 2019년부터 급상승하는 모습을 볼 수 있습니다.

<img src="https://user-images.githubusercontent.com/115917627/215100490-4dd7c6cf-0245-4289-b307-fc724852a06e.png" weight="200" height="300">

- ESG 각각 등급에서 공통적인 특징은 ESG 평가를 도입한 직후에는 상대적으로 낮은 등급의 비율이 높았는데 ESG 관심이 높아지기 시작한 최근 데이터를 보면 높은 등급의 평가가 높은 비중을 차지하고 있는 것을 볼 수 있습니다.

## data 폴더의 파일 설명
- ESG_KOSPI200_ca.csv : 코스피200 기업들의 연도별 ESG등급
- KOSPI200.csv : 코스피200 지수
- KOSPI200_ESG.csv : 코스피200 기업의 ESG 지수
- KOSPI_ESG_MERGE.csv : 코스피200 지수와 코스피200 기업의 ESG 지수 데이터를 병합
- ESG_KOSPI200_ca.csv : 코스피200 기업의 ESG 등급

## 참고자료
- https://esg.krx.co.kr/contents/02/02020000/ESG02020000.jsp
- http://www.cgs.or.kr/business/esg_tab01.jsp
- http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010105&idxCd=1&idxCd2=180
- http://data.krx.co.kr/contents/MDC/HARD/hardController/MDCHARD050.cmd#none
- http://www.cgs.or.kr/business/esg_tab04.jsp?pg=%7B%7D&pp=10&skey=&svalue=&sfyear=2021&styear=2021&sgtype=&sgrade=#ui_contents
