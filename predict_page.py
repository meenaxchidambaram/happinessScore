import streamlit as st
import pickle 
import numpy as np 

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data1=pickle.load(file)
    return data1

data1=load_model()
rg=data1["model"]
le=data1["le"]

def show_predict_page():
    st.title("Happiness Score Prediction")
    st.write("Prediction based on Alcohol Consumption and Annual Income($)")
    st.write("Fill in the following details and know you're happiness score!")
 
    continents={
        "South America", 
        "Oceania", 
        "Europe", 
        "North America",
        "Asia",
        'Africa'
    }

    continent=st.selectbox("Continent: ", continents) 
    alcrate=st.slider("Alcohol Consumption Rate: ",1.0,10.0,0.2)
    income=st.number_input("Annual Income($): ")

    ok=st.button("Calculate Happiness Score")

    if ok:
        X=np.array([[continent,income,alcrate]])
        X[:,0]=le.transform(X[:,0])
        X=X.astype(float)

        hs=rg.predict(X)
        st.subheader("The estimated happiness score is {:.2f}".format(hs[0])+"/10")


