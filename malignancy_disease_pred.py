# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

malignancy_model = pickle.load(open('malignancy_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Malignancy Prediction System',
                          
                          ['Cancer Prediction'],
                          icons=['person'],
                          default_index=0)
    
    
# Malignancy Prediction Page
if (selected == 'Cancer Prediction'):
    
    # page title
    st.title('Malignancy Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        radius = st.text_input('radius_mean')
        
    with col2:
        texture = st.text_input('texture_mean')
        
    with col3:
        perimeter = st.text_input('perimeter_mean')
        
    with col4:
        area_mean = st.text_input('area_mean')
        
    with col5:
        smoothness_mean = st.text_input('smoothness_mean')
        
    with col1:
        compactness_mean = st.text_input('compactness_mean')
        
    with col2:
        concavity_mean = st.text_input('concavity_mean')
        
    with col3:
        concave_points_mean = st.text_input('concave points_mean')
        
    with col4:
        symmetry_mean = st.text_input('symmetry_mean')
        
    with col5:
        fractal_dimension = st.text_input('fractal_dimension_mean')
        
    with col1:
        radius_se = st.text_input('radius_se')
        
    with col2:
        texture_se = st.text_input('texture_se')
        
    with col3:
        perimeter_se = st.text_input('perimeter_se')
        
    with col4:
        area_se = st.text_input('area_se')
        
    with col5:
        smoothness_se = st.text_input('smoothness_se')
        
    with col1:
        compactness_se = st.text_input('compactness_se')
        
    with col2:
        concavity_se = st.text_input('concavity_se')
        
    with col3:
        concave_points = st.text_input('concave points_se')
        
    with col4:
        symmetry_se = st.text_input('symmetry_se')
        
    with col5:
        fractal_dimension_se = st.text_input('fractal_dimension_se')
        
    with col1:
        radius_worst = st.text_input('radius_worst')
        
    with col2:
        texture_worst = st.text_input('texture_worst')

    with col3:
        perimeter_worst = st.text_input('perimeter_worst')

    with col4:
        area_worst = st.text_input('area_worst')

    with col5:
        smoothness_worst = st.text_input('smoothness_worst')

    with col1:
        compactness_worst = st.text_input('compactness_worst')

    with col2:
        concavity_worst = st.text_input('concavity_worst')

    with col3:
        concave_points_worst = st.text_input('concave points_worst')

    with col4:
        symmetry_worst = st.text_input('symmetry_worst')

    with col5:
        fractal_dimension_worst = st.text_input('fractal_dimension_worst')
        
    
    
    # code for Prediction
    malignancy_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Malignancy's Test Result"):
        malignancy_prediction = malignancy_model.predict([[radius,texture,perimeter,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])
        
        if (malignancy_prediction[0] == 'M'):
          malignancy_diagnosis = "The person has Malignancy"
        else:
          malignancy_diagnosis = "The person does not have Malignancy (i.e., Benign)"
        
    st.success(malignancy_diagnosis)
















