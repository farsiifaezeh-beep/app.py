import streamlit as st
import pandas as pd
import plotly.express as px

# تنظیمات صفحه
st.set_page_config(page_title="داشبورد شاخص و موانع استان یزد", layout="wide")
st.title("داشبورد شاخص و موانع کسب‌وکار استان یزد")

# --- بارگذاری CSV ها ---
index_df = pd.read_csv("index_scores.csv")
barriers_df = pd.read_csv("barriers.csv")

# --- بخش ۱: شاخص کل ---
st.header("شاخص کل استان")
st.dataframe(index_df)

# نمودار تغییرات شاخص کل
index_chart = px.bar(
    index_df,
    x='شاخص',
    y='مقدار / نمره',
    text='مقدار / نمره',
    title="نمره شاخص کل و تغییرات"
)
st.plotly_chart(index_chart, use_container_width=True)

# --- بخش ۲: موانع کسب‌وکار ---
st.header("موانع کسب‌وکار")
st.dataframe(barriers_df)

# نمودار میله‌ای افقی مؤلفه‌ها
barriers_chart = px.bar(
    barriers_df,
    x='نمره در استان یزد (تابستان 1403)',
    y='مؤلفه (مانع کسب و کار)',
    orientation='h',
    text='نمره در استان یزد (تابستان 1403)',
    title="موانع کسب‌وکار - نمره استان یزد"
)
st.plotly_chart(barriers_chart, use_container_width=True)
