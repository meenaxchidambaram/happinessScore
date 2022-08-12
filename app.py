from turtle import *
import sklearn
import streamlit as st
from tkinter import *


from predict_page import show_predict_page
from explore_page import explore

pages1=st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))

if pages1=="Predict":
    show_predict_page()
elif pages1=="Explore":
    explore()
