import streamlit as st
import pandas as pd
import joblib
import numpy as np
from xgboost import XGBClassifier

# Loading .joblib file
model = joblib.load('kiva_model_xgb.joblib')


def repayment_term_16_mos_and_above_value(repayment_term_16_mos_and_above_choice):
    if repayment_term_16_mos_and_above_choice == 'Yes':
        repayment_term_16_mos_and_above = 1
    else:
        repayment_term_16_mos_and_above = 0

    return repayment_term_16_mos_and_above

def partner_covers_currency_loss_value(partner_covers_currency_loss_choice):
    if partner_covers_currency_loss_choice == 'Yes':
        partner_covers_currency_loss = 1
    else:
        partner_covers_currency_loss = 0

    return partner_covers_currency_loss

def with_image_value(with_image_choice):
    if with_image_choice == 'Yes':
        with_image = 1
    else:
        with_image = 0

    return with_image

def with_video_value(with_video_choice):
    if with_video_choice == 'Yes':
        with_video = 1
    else:
        with_video = 0

    return with_video

def repayment_interval_value(repayment_interval_choice):
    if repayment_interval_choice == 'Irregular':
        repayment_interval_irregular = 1
        repayment_interval_monthly = 0
    else:
        repayment_interval_irregular = 0
        repayment_interval_monthly = 1

    return repayment_interval_irregular, repayment_interval_monthly

def sector_name_values(sector_name_choice):
    if sector_name_choice == 'Arts':
        sector_name_Arts = 1
        sector_name_Construction, sector_name_Education, sector_name_Health, sector_name_Housing, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Retail, sector_name_Services = 0, 0, 0, 0, 0, 0, 0, 0
    elif sector_name_choice == 'Construction':
        sector_name_Construction = 1
        sector_name_Arts, sector_name_Education, sector_name_Health, sector_name_Housing, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Retail, sector_name_Services = 0, 0, 0, 0, 0, 0, 0, 0
    elif sector_name_choice == 'Education':
        sector_name_Education = 1
        sector_name_Arts, sector_name_Construction, sector_name_Health, sector_name_Housing, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Retail, sector_name_Services = 0, 0, 0, 0, 0, 0, 0, 0
    elif sector_name_choice == 'Health':
        sector_name_Health = 1
        sector_name_Arts, sector_name_Construction, sector_name_Education, sector_name_Housing, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Retail, sector_name_Services = 0, 0, 0, 0, 0, 0, 0, 0
    elif sector_name_choice == 'Housing':
        sector_name_Housing = 1
        sector_name_Arts, sector_name_Construction, sector_name_Education, sector_name_Health, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Retail, sector_name_Services = 0, 0, 0, 0, 0, 0, 0, 0
    elif sector_name_choice == 'Manufacturing':
        sector_name_Manufacturing = 1
        sector_name_Arts, sector_name_Construction, sector_name_Education, sector_name_Health, sector_name_Housing, sector_name_Personal_Use, sector_name_Retail, sector_name_Services = 0, 0, 0, 0, 0, 0, 0, 0
    elif sector_name_choice == 'Personal Use':
        sector_name_Personal_Use = 1
        sector_name_Arts, sector_name_Construction, sector_name_Education, sector_name_Health, sector_name_Housing, sector_name_Manufacturing, sector_name_Retail, sector_name_Services = 0, 0, 0, 0, 0, 0, 0, 0
    elif sector_name_choice == 'Retail':
        sector_name_Retail = 1
        sector_name_Arts, sector_name_Construction, sector_name_Education, sector_name_Health, sector_name_Housing, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Services = 0, 0, 0, 0, 0, 0, 0, 0
    elif sector_name_choice == 'Services':
        sector_name_Services = 1
        sector_name_Arts, sector_name_Construction, sector_name_Education, sector_name_Health, sector_name_Housing, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Retail = 0, 0, 0, 0, 0, 0, 0, 0

    return sector_name_Arts, sector_name_Construction, sector_name_Education, sector_name_Health, sector_name_Housing, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Retail, sector_name_Services

def prediction_value(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):

    prediction = model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]])
    
    if prediction[0] == 1:
        prediction_text = 'The loan is funded'
    else:
        prediction_text = 'The loan is not funded'
    
    return prediction_text
    

def main():
    # Streamlit app title
    st.title('KIVA Loan Predictor')

            # "loan_amount",
            # "repayment_term_16_mos_and_above",
            # "partner_covers_currency_loss",
            # "with_image",
            # "with_video",
            # "repayment_interval_irregular",
            # "repayment_interval_monthly",
            # 'sector_name_Arts', 'sector_name_Construction',
            # 'sector_name_Education',
            # 'sector_name_Health', 'sector_name_Housing', 'sector_name_Manufacturing',
            # 'sector_name_Personal_Use', 'sector_name_Retail', 'sector_name_Services'

    # User inputs
    loan_amount = st.number_input(label = 'Enter loan amount:')
    repayment_term_16_mos_and_above_choice = st.selectbox('Is the repayment 16 months and above?:', ['Yes', 'No'])
    partner_covers_currency_loss_choice = st.selectbox('Does partner cover currency loss?:', ['Yes', 'No'])
    with_image_choice = st.selectbox('Do they have an image uploaded with the loan?:', ['Yes', 'No'])
    with_video_choice = st.selectbox('Do they have a video uploaded with the loan?:', ['Yes', 'No'])
    repayment_interval_choice = st.selectbox('What is the repayment interval?:', ['Irregular', 'Monthly'])
    sector_name_choice = st.selectbox('What sector is the loan a part of?:', ['Arts', 'Construction', 'Education', 'Health', 'Housing', 'Manufacturing', 'Personal Use', 'Retail', 'Services'])

    # Giving categorical variables a value based on user's input
    repayment_term_16_mos_and_above = repayment_term_16_mos_and_above_value(repayment_term_16_mos_and_above_choice)
    partner_covers_currency_loss = partner_covers_currency_loss_value(partner_covers_currency_loss_choice)
    with_image = with_image_value(with_image_choice)
    with_video = with_video_value(with_video_choice)
    repayment_interval_irregular, repayment_interval_monthly = repayment_interval_value(repayment_interval_choice)
    sector_name_Arts, sector_name_Construction, sector_name_Education, sector_name_Health, sector_name_Housing, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Retail, sector_name_Services = sector_name_values(sector_name_choice)

    # Getting prediction
    prediction_text = prediction_value(loan_amount, repayment_term_16_mos_and_above, partner_covers_currency_loss, with_image, with_video, repayment_interval_irregular, repayment_interval_monthly, sector_name_Arts, sector_name_Construction, sector_name_Education, sector_name_Health, sector_name_Housing, sector_name_Manufacturing, sector_name_Personal_Use, sector_name_Retail, sector_name_Services)
    st.text(prediction_text)

if __name__ == "__main__":
    main()
