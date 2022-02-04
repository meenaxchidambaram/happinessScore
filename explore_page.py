import sklearn
import turtle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv('NetFLixDATASET - Sheet1 (3).csv')
    data=data[["Country","Continent","GrossNationalIncome","AlcoholConsumptionRate","HappinessScore"]]
    return data 

df=load_data()

def explore():
    st.title("Explore Visualizations:")

    st.write("Mean Alcohol Consumption Rate in each Continent ")
    data=df.groupby(["Continent"])["AlcoholConsumptionRate"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("Mean Alcohol Consumption Rate based on HappinessScore ")
    data=df.groupby(["HappinessScore"])["AlcoholConsumptionRate"].mean().sort_values(ascending=True)
    st.line_chart(data)

    st.write("Mean Happiness Score in each Continent ")
    data=df.groupby(["Continent"])["HappinessScore"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    