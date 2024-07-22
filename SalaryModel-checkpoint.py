import pickle
import streamlit as st
import numpy as np
model = pickle.load(open('salarypredict.pkl','rb'))
def mymodel():
    st.title('Experience-Salary Prediction')
    exp = st.number_input('Enter the year(s) of experience: ')
    pred = st.button('Predict')
    if pred:
        sal = model.predict([[exp]])
        newsal = sal[0]
        newsalrd = np.round(newsal,2)
        st.write('The salary would be: ',*newsalrd)
mymodel()
