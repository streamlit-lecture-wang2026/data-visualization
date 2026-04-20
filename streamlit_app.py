import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import plotly.express as px
from pathlib import Path

# 한글 폰트 등록
폰트_파일 = Path(__file__).resolve().parent / "fonts" / "NanumGothic-Bold.ttf"
if 폰트_파일.exists():
    fm.fontManager.addfont(str(폰트_파일))
    한글_폰트_이름 = fm.FontProperties(fname=str(폰트_파일)).get_name()
    plt.rcParams["font.family"] = 한글_폰트_이름
    plt.rcParams["axes.unicode_minus"] = False
    sns.set_theme(font=한글_폰트_이름, style="whitegrid")
else:
    st.warning("fonts/NanumGothic-Bold.ttf를 찾을 수 없습니다. 한글 폰트가 제대로 표시되지 않을 수 있습니다.")

st.title("🎈 데이터 시각화 예시")
st.write("matplotlib, seaborn, plotly를 사용한 데이터 시각화 예시를 확인해보세요.")

# 예시 1: matplotlib로 선 그래프 만들기
st.header("1. matplotlib 선 그래프")
판매량_월별 = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "판매량": [120, 150, 170, 160, 190, 210],
})
fig, ax = plt.subplots()
ax.plot(판매량_월별["월"], 판매량_월별["판매량"], marker="o", color="#2c7fb8")
ax.set_title("월별 판매량 추이")
ax.set_xlabel("월")
ax.set_ylabel("판매량 (개)")
ax.grid(True, linestyle="--", alpha=0.5)
st.pyplot(fig)

# 예시 2: seaborn으로 막대 그래프 만들기
st.header("2. seaborn 막대 그래프")
제품_판매 = pd.DataFrame({
    "제품": ["A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "판매량": [50, 60, 40, 70, 80, 50, 90, 75, 65],
})
fig2, ax2 = plt.subplots()
sns.barplot(data=제품_판매, x="제품", y="판매량", estimator=np.sum, ci=None, palette="pastel", ax=ax2)
ax2.set_title("제품별 총 판매량")
ax2.set_xlabel("제품")
ax2.set_ylabel("판매량 (개)")
st.pyplot(fig2)

# 예시 3: plotly로 대화형 산점도 만들기
st.header("3. plotly 산점도")
가격_판매 = pd.DataFrame({
    "가격": [10, 20, 30, 40, 50, 60, 70, 80],
    "판매량": [65, 55, 45, 40, 35, 30, 25, 20],
    "카테고리": ["소형", "소형", "중형", "중형", "대형", "대형", "프리미엄", "프리미엄"],
})
fig3 = px.scatter(
    가격_판매,
    x="가격",
    y="판매량",
    color="카테고리",
    size="판매량",
    title="가격 대비 판매량 분석",
    labels={"가격": "가격 (만원)", "판매량": "판매량 (개)", "카테고리": "제품 카테고리"},
)
fig3.update_layout(title_font_size=20)
st.plotly_chart(fig3, use_container_width=True)
