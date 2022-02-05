from turtle import *
import sklearn
import streamlit as st
from tkinter import *


from predict_page import show_predict_page
from explore_page import explore

page=st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))

if page=="Predict":
    show_predict_page()
elif page=="Explore":
    explore()
