import streamlit as st
import pickle as pk


#importing the knn model
pickle1 = open('knn.pkl', 'rb')
knn_classifier = pk.load(pickle1)

#importing the rfc model
pickle2 = open('rfc.pkl', 'rb')
rfc_classifier = pk.load(pickle2)

#importing the svm model
pickle3 = open('svc.pkl', 'rb')
svc_classifier = pk.load(pickle3)

features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',  'BMI', 'DiabetesPedigreeFunction', 'Age']
#Creating a model that performs knn classification on user input
def knn_model(Pregnancies, Glucose, BloodPressure, SkinThickness,  BMI, DiabetesPedigreeFunction, Age):
    features = [[Pregnancies, Glucose, BloodPressure, SkinThickness, BMI, DiabetesPedigreeFunction, Age]]
    
    prediction = knn_classifier.predict(features)
    return prediction
    

#Creating a model that performs random forest classification on user input
def  rfc_model(Pregnancies, Glucose, BloodPressure, SkinThickness,  BMI, DiabetesPedigreeFunction, Age):
    features = [[Pregnancies, Glucose, BloodPressure, SkinThickness, BMI, DiabetesPedigreeFunction, Age]]
    
    prediction = rfc_classifier.predict(features)
    return prediction

#Creating a model that performs support vector classification on user input
def  svc_model(Pregnancies, Glucose, BloodPressure, SkinThickness,  BMI, DiabetesPedigreeFunction, Age):
    features = [[Pregnancies, Glucose, BloodPressure, SkinThickness, BMI, DiabetesPedigreeFunction, Age]]
    
    prediction = rfc_classifier.predict(features)
    return prediction


def fancy_result(text, font_size=24):
    res = f'<span style="color:#ff0000; font-size: {font_size}px;">{text}</span>'
    st.markdown(res, unsafe_allow_html=True )

#Heading
def main():
    st.title('DIABETES PREDICTION')
    st.image('diabetes_image.jpg')
    st.write("""
        ## Fill the form below
    """)
    
    
    model = st.sidebar.selectbox('Select model', ['KNN', 'Random Forest', 'Support Vector'])

    #accepting the features from the user
    Pregnancies = st.number_input('Number of pregnancies', min_value=0, max_value=15, value=1)
    Glucose = st.number_input('Glucose level', min_value=1, max_value=1000, value=10, step=10)
    BloodPressure = st.number_input('BloodPressure', min_value=1, max_value=1000, value=10, step=5)
    SkinThickness = st.number_input('Skin Thickness', min_value=1, max_value=100, value=10, step=5)
    BMI = st.number_input('BMI', min_value=1., max_value=1000., value=10., format='%.2f', step=1.)
    DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0., max_value=10., value=0., step=.1, format='%.2f')
    Age = st.number_input('Age', min_value=0, max_value=200, value=30)

     

    st.write("""
        #### Model used: {} 
    """.format(model))
    st.write()

#Function to display output
    def result(outcome):
            if outcome == 1:
                return fancy_result('You have been diagnosed with Diabetes🤒')
                
            else:
                return st.write("""
        ### You have not been diagnosed with diabetes
    """)

    if st.button('Predict'):
        if model == 'KNN':
            outcome = knn_model(Pregnancies, Glucose, BloodPressure, SkinThickness, BMI, DiabetesPedigreeFunction, Age)
            st.success(outcome)
            result(outcome)
            
        elif model == 'Random Forest':
            outcome = rfc_model(Pregnancies, Glucose, BloodPressure, SkinThickness, BMI, DiabetesPedigreeFunction, Age)
            st.success(outcome)
            result(outcome)
        else:
            outcome = svc_model(Pregnancies, Glucose, BloodPressure, SkinThickness, BMI, DiabetesPedigreeFunction, Age)
            st.success(outcome)
            result(outcome)
            
        
if __name__ == '__main__':
    main()

