from turtle import *
import sklearn
import streamlit as st
from tkinter import *


from predict_page import show_predict_page
from explore_page import explore

pages=st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))

if pages=="Predict":
    show_predict_page()
elif pages=="Explore":
    explore()
