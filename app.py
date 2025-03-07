import requests
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.title("Student Exam Performance Indicator")

gender = st.selectbox("Gender",['male','female'])
race = st.selectbox("Race or Ethnicity",['group A','group B', 'group C', 'group D', 'group E'])
parental_education = st.selectbox("Parental Level of Education",["associate's degree","high school", "master's degree", "some college", "some high school"])
lunch_type = st.selectbox("Lunch Type",['standard','free/reduced'])
test_preparation_course = st.selectbox("test_preparation_course", ["none", "completed"])


writing_score = st.slider("Writing Score out of 100", min_value=0, max_value=100)
reading_score = st.slider("Reading Score out of 100", min_value=0, max_value=100)



if st.button("Predict your score"):
    data=CustomData(
        gender=gender,
        race_ethnicity=race,
        parental_level_of_education=parental_education,
        lunch=lunch_type,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score

    )
    pred_df = data.get_data_as_data_frame()
    print(pred_df)
    print("Before Prediction")

    predict_pipeline = PredictPipeline()
    print("Mid Prediction")
    results = predict_pipeline.predict(pred_df)
    print("After Prediction")

    result_html = f"""
    <div style="
        background-color: #f0f8ff;
        border: 2px solid #6495ed;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        text-align: center;
        font-size: 18px;
        color: #00008b;
    ">
        <strong>The predicted score is: {results[0]}</strong>
    </div>
    """
    st.markdown(result_html, unsafe_allow_html=True)