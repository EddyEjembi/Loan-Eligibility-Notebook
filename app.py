import streamlit as st
import numpy as np
import pickle as pkl
import pandas as pd

st.title('LOAN ELIGIBILITY PREDICTOR...')

def make_prediction():
    co_income = 0
    #Gender
    status = st.radio('Select Gender: ', ('Male', 'Female'))
    if (status == 'Male'):
        gender = 1
    else:
        gender = 0

    #Education
    edu = st.radio('Please select your level of education: ', ('Graduate', 'Not Graduate'))
    if (edu == 'Graduate'):
        education = 1
    else:
        education = 0

    #Self Employed
    sef = st.radio('Self Employed?', ('Yes', 'No'))
    if (sef == 'Yes'):
        selfemployed = 1
    else:
        selfemployed = 0

    #Income
    income = st.number_input('What is your income?', min_value=0)


    #Married
    mar = st.radio('Are you married? ', ('No', 'Yes'))
    if (mar == 'Yes'):
        married = 1
        co_income = st.number_input('What is your spouse income?', min_value=0)
    else:
        married = 0

    #Dependents
    dep = st.selectbox('Your number of Dependents', ('0', '1', '2', '3+'))
    if (dep == '1'):
        dependent = 1
    elif (dep == '2'):
        dependent = 2
    else:
        dependent = 3

    #Loan Amount
    loanAmount = st.number_input('Enter the loan amount', min_value=0)

    #Property Area
    prop = st.radio('What area is the property located?', ('Urban', 'Semi-Urban', 'Rural'))
    if (prop == 'Urban'):
        propertyArea = 0
    elif (prop == 'Semi-Urban'):
        propertyArea = 1
    else:
        propertyArea = 2

    #Loan Amount Term
    loanTerm = st.number_input('Term of loan (in days.)', min_value=0)

    model = pkl.load(open('Loan_Eligibility_Model.pkl', 'rb'))
    prediction = model.predict([[gender,married,dependent,education,selfemployed,income,co_income,loanAmount,loanTerm,1.0,propertyArea]])
    return prediction

def main():
    page = st.sidebar.radio('Page', ('Home', 'About'))
    rate = st.sidebar.slider('Please rate this app', 1,5)
    st.sidebar.text('You rated: {}'.format(rate))
    if (page == 'Home'):
        name = st.text_input('Please enter your name in full', '')
        if name:
            result = make_prediction()
            if (st.button('Result')):
                if (result == [1]):
                    st.success('Congratulations... You are eligible for loan\n You can proceed to the next stage.')
                else:
                    st.warning('Sorry... You are not eligible for this loan \n Try working on increasing your portfolio')
    elif (page == 'About'):
        st.subheader('About Page')
        st.write('This application was built using data from a housing company that lends money to their customers to \
                  purchase properties. The main aim is to predict if a person is eligible for a loan or not. The prediction model \
                  was built using python and jupyter notebook. You can find the link to the gitub repository \
                  here: https://github.com/EddyEjembi/Loan-Eligibility-Notebook.git. The web app is \
                  built with streamlit.')
        st.write('Please NOTE that this is just for learning purpose and the data was gotten from kaggle.')


if __name__ =='__main__':
    main()