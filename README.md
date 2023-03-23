# ESG평가가 기업 가치 측정의 기준으로 적절한가?

## 팀원
|팀원|역할|
|:---:|:---:|
|<span style="color:blue">[조현준(팀장)](https://github.com/chohj118)|데이터 수집 · 전처리 · 시각화(코스피200 기업 주가), PPT, 발표|
|<span style="color:blue">[이혜빈](https://github.com/dkssudgb)|데이터 수집 · 전처리 · 시각화(코스피200 기업 ESG지수)| 
|<span style="color:blue">[박성용](https://github.com/mols3131d)|데이터 수집 · 전처리 · 시각화(재무제표, 코스피200 개별 종목 ESG 평가 전처리)| 
|<span style="color:blue">[노나은](https://github.com/better-noh)|데이터 수집 · 전처리 · 시각화(ESG 평가등급, 네이버 ESG 관련 뉴스기사)| 
|<span style="color:blue">이주민|데이터 수집 · 전처리 · 시각화(코스피200), PPT|

## 1-1 주제
### KCGS의 ESG등급을 통한 주가지수와 개별종목의 주가, 재무제표 분석

## 1-2 주제 선정 이유
<img src="https://user-images.githubusercontent.com/115917627/218306160-7e9a4133-41b5-41cd-9c55-fd9b98cd90f4.png" weight="1000" height="400">

- 최근 ESG 관련 지표에 관심을 가지는 기업과 투자자들이 많아지는 추세이며, 다양한 연구를 통해 **ESG가 기업의 지속가능성 및 장기적인 가치 창출을 평가하는 중요한 기준**이 된다고 보고있다.
- ESG 평가 등급과 다른 평가 지표와의 비교를 통해 인사이트를 도출해보기 위해 주제를 선정하였습니다.

## 1-3 ESG등급 관련 선행 연구
### 황성준 and 오상희. (2021). [코스피 200 ESG 지수의 종목변경에 대한 시장반응](https://www.kyungnam.ac.kr/riim/5339/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGcmlpbSUyRjg5MCUyRjk1NzIwJTJGYXJ0Y2xWaWV3LmRvJTNGcGFnZSUzRDElMjZzcmNoQ29sdW1uJTNEJTI2c3JjaFdyZCUzRCUyNmJic0NsU2VxJTNEJTI2YmJzT3BlbldyZFNlcSUzRCUyNnJnc0JnbmRlU3RyJTNEJTI2cmdzRW5kZGVTdHIlM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZwYXNzd29yZCUzRCUyNg%3D%3D). 지역산업연구, 44(4), 241-262.
- 위 연구는 한국거래소(KRX) 코스피 200 ESG 지수 편입과 퇴출에 대한 주가반응 분석하였다.
- 기업의 평균초과수익률과 코스피 200 ESG 지수 구성종목편입 유무를 보았을 때, 편입의 경우 유의한 양의 관계를 나타낸 반면, 퇴출은 음의 관계를 나타냈다.
- 본 연구에서는 ESG 성과에 대한 시장의 부정적인 인식 전환과 기업들의 ESG 개선 활동 유도를 기대하였다.

### 황성준. (2022). [기업의 ESG 활동과 주가동조성](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002876301). 전산회계연구, 20(2), 83-101.
- 위의 연구에서는 2018년~2021년의 코스피, 코스닥의 12월 결산기업을 연구표본으로 설정하여 ESG 활동 성과와 시장수익률 및 산업수익률의 변동성의 영향 관계에 대해 실증분석하였다.
- 기업의 ESG 활동은 주가동조성과 유의한 양(＋)의 관련성이 있고, ESG 활동 기업은 개별기업의 고유정보가 주가에 충분히 반영되어 정보효율성이 높았다.
- ESG를 수행하는 기업은 주가에 충분한 정보가 반영된 것으로 보았다.

## 2 분석
## 2-1 활용 데이터
|이름|설명|Method|Source|
|:---:|:---|:---:|:---|
|KCGS ESG Rating|한국ESG기준원 ESG등급 데이터</br>- 기간 : 2011년~2018년|Web Scraping|[KRX 정보데이터시스템](http://data.krx.co.kr/contents/MDC/HARD/hardController/MDCHARD050.cmd#none)|
|KRX KOSPI 200 Index Components|KRX KOSPI 200 지수 구성종목 정보</br>- 기간 : 2010-06-30~2018-06-31</br>- 매년 06월 말일과 12월 말일에 대한 데이터|Download|[KRX 정보데이터시스템](http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010106)|
|KRX KOSPI 200 Index Components</br>Stock Price|한국ESG기준원 ESG등급 데이터</br>- 기간 : 2011년~2018년|API|[FinanceDataReader](https://github.com/financedata-org/FinanceDataReader)|
|DART corpCode|금융감독원 고유번호|API|[금융감독원 고유번호](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019018)|
|DART company|금융감독원 공시정보 기업개황|API|[금융감독원 공시정보 기업개황](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019002)|
|FSC FinaStatInfo|금융위원회 기업재무정보 (요약재무제표)</br>- 기간 : 2011년~2018년|API|[금융위원회 기업 재무정보](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043459)|
|KRX KOSPI 200 Index Price|한국거래소 KOSPI 200 지수 가격 데이터</br>- 기간 : 2011년~2018년|Download|[KRX 정보데이터시스템](http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010105)|
|KRX KOSPI 200 ESG Index Price|한국거래소 KOSPI 200 ESG 지수 가격 데이터</br>- 기간 : 2010-06-31~2022-06-31|Download|[KRX 정보데이터시스템](http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010105)|

- 표본
   - 2011년~2018년 KOSPI200 지수에 구성된 적이 있는 종목(기업)이면서
   - KCGS에서 ESG등급 평가된 적이 있는 종목
   
## 2-2 ESG 등급
|ESG 등급|ESG 등급 인코딩|
|:---|:---|
|S|6|
|A+|5|
|A|4|
|B+|3|
|B|2|
|C|1|
|D|0|



<img src="https://user-images.githubusercontent.com/115917627/218307832-93ad021c-9401-47cd-ac8e-ec5926ec43b1.png" weight="200" height="400">

- 2011년~2018년 기준, ESG종합 등급별 평균 기업체 수 확인
   - 분석한 기간 중 **대다수의 기업체가 B등급으로 약 80%의 비중을 차지**했다.

<img src="https://user-images.githubusercontent.com/115917627/218308608-10ec4755-d8e7-4476-9c89-115eb7e71b31.png" weight="200" height="400">

- 2011년~2018년 기준, ESG종합 등급 추이
   - ESG종합 등급을 받는 기업체 수는 매년 증가 추세를 보이며, **매년 ESG종합 등급에서 B등급을 받은 기업체 수가 많다**는 것을 알 수 있다.

<img src="https://user-images.githubusercontent.com/115917627/218308567-e45b0425-619f-4422-bc94-280c01b528a3.png" weight="200" height="400">

- 2011년~2018년 기준, E(환경) 등급 추이
   - 매년 E(환경) 등급에서 B등급을 받은 기업체 수가 많으며, **2017년 유일하게 S등급을 받은 기업체 1곳이 등장**했다. 

<img src="https://user-images.githubusercontent.com/115917627/218308718-a1d01a03-6f3e-47bc-b6f9-49b5e55a3f71.png" weight="200" height="400">

- 2011년~2018년 기준, S(사회적구조) 등급 추이
   - 매년 E(환경) 등급에서 B등급을 받은 기업체 수가 많으며, **2017년 유일하게 S등급을 받은 기업체 1곳이 등장**했다. 

<img src="https://user-images.githubusercontent.com/115917627/218308719-07b625ee-5867-4247-98bb-e685cd8c71d1.png" weight="200" height="400">

- 2011년~2018년 기준, G(지배구조) 등급 추이
   - 매년 G(지배구조) 등급에서 **B등급을 받은 기업체 수가 많다**. 

## 2-3 KOSPI 200 지수와 KOSPI 200 ESG 지수
<img src="https://user-images.githubusercontent.com/115917627/218308929-01a98bb8-1660-4912-b8b3-50613ff54412.png" weight="200" height="400">

- 연도별 종가 비교 : KOSPI 200 지수와 KOSPI 200 ESG 지수의 종가가 거의 유사하게 나타나는 것을 볼 수 있다. 이는 KOSPI 200 ESG 지수가 KOSPI 200 기업들 중 ESG 등급이 우수한 기업들을 기준으로 산출했기 때문으로 보인다.
 
<img src="https://user-images.githubusercontent.com/115577097/218638003-f22367a5-00fa-4447-900d-eba017741fad.png" weight="200" height="400">

- 연도별 등락률 비교: 두 지수간의 등락률 또한 매우 유사하게 움직이는 것으로 보인다.


## 2-4 연도, ESG 등급별 주가 분석
### 대체로 등급이 높을 때 주가가 높은 것으로 보이는데, 상대적으로 ESG가 관심이 높은 시기인 2017년 이후 더 경향이 큰 것으로 보인다.

- ESG종합 등급

<img src="https://user-images.githubusercontent.com/115917627/218309165-6f93bb8c-2e33-4f6e-8b02-1be560ede67c.png" weight="200" height="300">

- E(환경) 등급

<img src="https://user-images.githubusercontent.com/115917627/218309168-d0b31680-dd63-4aa2-bfb6-753993eb688a.png" weight="200" height="300">

- S(사회적구조) 등급

<img src="https://user-images.githubusercontent.com/115917627/218309173-307b82d8-3d74-416a-914b-b8f354646ce1.png" weight="200" height="300">

- G(지배구조) 등급

<img src="https://user-images.githubusercontent.com/115917627/218309181-8261f541-4663-4f69-8a5b-792586ce4083.png" weight="200" height="300">

## 2-5 연도, ESG 등급별 재무제표 분석
### 매출과 영업이익 등 높은 등급(A+, A)의 경우가 더 높은 것으로 보인다.

- 매출

<img src="https://user-images.githubusercontent.com/115917627/218309407-a236d200-5389-4640-91a3-cb7798e4b272.png" weight="400" height="400">

- 영업이익

<img src="https://user-images.githubusercontent.com/115917627/218309413-3f72c692-8873-462f-bee2-50c33a51add8.png" weight="400" height="400">

### 종목 별로 Min-Max 스케일링 적용
- 하지만, 종목 별로 MinMax 스케일링을 적용한 데이터로 보았을 때, 차이는 미미한 것으로 보여,
위의 경우는 높은 등급에 상대적으로 큰 규모의 회사들이 많이 분포하여 나타난 것으로 보인다.

- 매출

<img src="https://user-images.githubusercontent.com/115917627/218309412-e7c17ec4-b7b0-4a89-9295-569a4ae6b0e1.png" weight="400" height="400">

- 영업이익

<img src="https://user-images.githubusercontent.com/115917627/218309411-aba1d883-4e9e-4bee-b3e2-9976fcf7ac52.png" weight="400" height="400">

## 2-6 연도, ESG 등급별 주가, 재무제표 상관계수

<img src="https://user-images.githubusercontent.com/115917627/218309409-477291d1-1007-487e-8d6c-204c6fc024a7.png" weight="400" height="600">

## 3 결론

## 3-1 분석 결과
- 연도별 ESG종합 등급을 분석했을 때, 매년 기업체 수가 증가하는 것으로 보아 기업들의 ESG 활동에 대한 관심이 커지고 있는 것으로 보인다.
- 연도별, ESG등급별 주가를 분석했을 때, 대체로 높은 ESG등급을 받은 경우에 주가도 높게 나타나는 경향이 있다.
- 연도별, ESG등급별 재무제표를 분석했을 때, ESG등급과 재무제표는 상관성이 없는 것으로 보인다.

## 3-2 한계점
- 주가 데이터에는 각 종목에 대해 일일 주가가 담겨있는 반면, ESG등급은 연 단위로 산출된다. 그래서 두 데이터를 비교하기 위한 기준을 맞추기 어려웠다. 
   -  구체적으로, 주가 데이터의 연평균 가격을 이용할지, ESG등급이 발표된 날을 기준으로 그 날의 주가 데이터(종가)를 이용할지 고민이 되었다.
   -  강사님의 피드백을 받은 후, 각 주가 데이터마다 그 해의 ESG등급을 추가하여 비교하기로 결정했다.
- KOSPI 200으로 선정된 기업 중 일부 기업만 추출해서 시각화를 진행하려고 했는데, 어떤 기준으로 표본을 정해야 하는지 힘들었다. 또한, 너무 적은 표본으로 데이터를 분석하면 의미 없는 데이터 분석 결과가 나올 것이라 판단되어 모든 기업의 연도별 종가, 거래량의 평균을 구해 수치화 한 뒤 전체 결과를 시각화 하기로 결정했다.

## 4 부록

## 4-1 출처

[KRX 정보데이터시스템](https://data.krx.co.kr/contents/MDC/HARD/hardController/MDCHARD050.cmd#none)</br>
[금융감독원 고유번호](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019018)</br>
[금융감독원 공시정보 기업개황](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019002)</br>
[금융위원회 기업 재무정보](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043459)

## 4-2 참고
[기업의 ESG 활동과 주가동조성](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002876301)</br>
[12.코스피 200 ESG 지수의 종목변경에 대한 시장반응](https://www.kyungnam.ac.kr/riim/5339/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGcmlpbSUyRjg5MCUyRjk1NzIwJTJGYXJ0Y2xWaWV3LmRvJTNGcGFnZSUzRDElMjZzcmNoQ29sdW1uJTNEJTI2c3JjaFdyZCUzRCUyNmJic0NsU2VxJTNEJTI2YmJzT3BlbldyZFNlcSUzRCUyNnJnc0JnbmRlU3RyJTNEJTI2cmdzRW5kZGVTdHIlM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZwYXNzd29yZCUzRCUyNg%3D%3D)</br>
[is-your-esg-data-unlocking-long-term-value](https://www.ey.com/en_gl/assurance/is-your-esg-data-unlocking-long-term-value)</br>
[is-your-esg-data-unlocking-long-term-value(PDF)](https://assets.ey.com/content/dam/ey-sites/ey-com/en_gl/topics/assurance/assurance-pdfs/ey-institutional-investor-survey.pdf)</br>
[ESG기준원 ESG평가](http://www.cgs.or.kr/business/esg_tab01.jsp)
