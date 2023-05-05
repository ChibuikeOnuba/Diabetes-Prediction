import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')

def heading(text, font_size):
    res = f'<span style="color:#FFFFFF; font-size: {font_size}px;"><b>{text}</b></span>'
    st.markdown(res, unsafe_allow_html=True)
    
    
def head(text):
    res = f'<span style="color:#3030FF; font-size: 25px;"><b>{text}</b></span>'
    st.markdown(res, unsafe_allow_html=True)
     
heading('EXPLORE DATASET', 40)
    

head('VIEW')
st.write()

if 'type' not in st.session_state or 'rows' not in st.session_state:
    st.session_state['rows'] = 5

increment = st.button('Add row')
if increment:
    st.session_state['rows'] += 1
    
decrement = st.button('Delete row')
if decrement:
    st.session_state['rows'] -= 1
st.table(df.head(st.session_state['rows']))    

types = {'Categorical':['Outcome'], 
         'Numerical':['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',  'BMI', 'DiabetesPedigreeFunction', 'Age']}


head('ANALYSIS')

type_of_analysis = st.radio('What type of analysis', ['Numerical','Categorical'])

column = st.selectbox('Select a column',types [type_of_analysis])


if type_of_analysis == 'Numerical':
    st.write(df[column].describe()) 
    fig =  plt.figure(figsize=(8, 4))
    sns.boxplot(data= df, x='Outcome', y=df[column]) #type of plot
    plt.title('AVERAGE {} BY OUTCOME'.format(column).upper(), color='red') #title of the plot
    st.pyplot(fig) #display plot on streamlit
    

if type_of_analysis == "Categorical":
    dist = pd.DataFrame(df[column].value_counts())
    st.bar_chart(dist)
    
    