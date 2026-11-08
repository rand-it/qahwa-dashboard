import streamlit as st
import pandas as pd

df = pd.read_csv("cafe_sales.csv")

st.title("Qahwa Corner Sales Dashboard")

branch = st.selectbox("Branch", ["All"] + sorted(df["branch"].unique()))
if branch != "All":
    df = df[df["branch"] == branch]

st.metric("Total revenue (SAR)", f"{df['total_sar'].sum():,}")

st.subheader("Revenue by product")
st.bar_chart(df.groupby("product")["total_sar"].sum())
