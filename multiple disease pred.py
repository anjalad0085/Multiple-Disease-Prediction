import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from joblib import load


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/priya/OneDrive/Desktop/multiple disease system/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/priya/OneDrive/Desktop/multiple disease system/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/priya/OneDrive/Desktop/multiple disease system/saved models/parkinsons_model.sav', 'rb'))

svm_model = load('C:/Users/priya/OneDrive/Desktop/multiple disease system/saved models/svm_model.joblib')



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Lung Cancer Prediction'],
                          icons=['activity','heart','person','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    try:
        age = float(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = float(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)


    except ValueError:
        st.error("Please enter valid numeric values for all input fields.")
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
# Lung Cancer Prediction Page
if (selected == 'Lung Cancer Prediction'):
    # Page title
    st.title('Lung Cancer Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.selectbox('Gender', ['Male', 'Female'])
        age = st.slider('Age', 0, 100)
        smoking = st.selectbox('Smoking', ['No', 'Yes'])
        yellow_fingers = st.selectbox('Yellow Fingers', ['No', 'Yes'])
    
    with col2:
        anxiety = st.selectbox('Anxiety', ['No', 'Yes'])
        peer_pressure = st.selectbox('Peer Pressure', ['No', 'Yes'])
        chronic_disease = st.selectbox('Chronic Disease', ['No', 'Yes'])
        fatigue = st.selectbox('Fatigue', ['No', 'Yes'])
    
    with col3:
        allergy = st.selectbox('Allergy', ['No', 'Yes'])
        wheezing = st.selectbox('Wheezing', ['No', 'Yes'])
        alcohol_consuming = st.selectbox('Alcohol Consuming', ['No', 'Yes'])
        coughing = st.selectbox('Coughing', ['No', 'Yes'])
    
    shortness_of_breath = st.selectbox('Shortness of Breath', ['No', 'Yes'])
    swallowing_difficulty = st.selectbox('Swallowing Difficulty', ['No', 'Yes'])
    chest_pain = st.selectbox('Chest Pain', ['No', 'Yes'])
    
    # Code for Prediction
    lung_cancer_diagnosis = ''
    
    # Convert user input to the format used during training
    gender = 0 if gender == 'Male' else 1
    smoking = 2 if smoking == 'Yes' else 1
    yellow_fingers = 2 if yellow_fingers == 'Yes' else 1
    anxiety = 2 if anxiety == 'Yes' else 1
    peer_pressure = 2 if peer_pressure == 'Yes' else 1
    chronic_disease = 2 if chronic_disease == 'Yes' else 1
    fatigue = 2 if fatigue == 'Yes' else 1
    allergy = 2 if allergy == 'Yes' else 1
    wheezing = 2 if wheezing == 'Yes' else 1
    alcohol_consuming = 2 if alcohol_consuming == 'Yes' else 1
    coughing = 2 if coughing == 'Yes' else 1
    shortness_of_breath = 2 if shortness_of_breath == 'Yes' else 1
    swallowing_difficulty = 2 if swallowing_difficulty == 'Yes' else 1
    chest_pain = 2 if chest_pain == 'Yes' else 1
    
    # Creating a button for Prediction
    if st.button('Lung Cancer Test Result'):
        lung_cancer_input = [gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease,
                             fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath,
                             swallowing_difficulty, chest_pain]
        lung_cancer_prediction = svm_model.predict([lung_cancer_input])
        
        if lung_cancer_prediction[0] == 1:
            lung_cancer_diagnosis = 'The model predicts lung cancer.'
        else:
            lung_cancer_diagnosis = 'The model predicts no lung cancer.'
        
    st.success(lung_cancer_diagnosis)


        

     