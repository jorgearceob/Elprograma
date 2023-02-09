
import streamlit as st
import pandas as pd
import numpy as np
import tkinter as tk

st.title('El programa')

#st.write("EL PROGRAMA")

#st.checkbox('yes')
#st.button('Click')

type_of_x = st.radio('Pick your exercise',['Push','Pull'])
#muscle_group = st.selectbox ('Pick your group', ['Legs','Arms', 'Shoulders', 'Chest','Back'])

if type_of_x == "Push":
    p_legs = st.selectbox ('Pick your leg exercise',
                                   ['Front Squat','Leg extension', 'Sissy Squat'])
    text_input1 = st.number_input('Peso pierna')

    p_upper = st.selectbox ('Pick your upper exercise',
                                   ['Close grip bench press','Military press','Bench press'])
    text_input2 = st.number_input('Peso ejercicio 1')

    p_upper_2 = st.selectbox ('Pick your second upper exercise',
                                   ['Incline press', 'Tricep extension','Rope press down'])
    text_input3 = st.number_input('Peso ejercicio 2')

    P_upper_3 = st.selectbox ('Pick your third upper exercise',
                                   ['Lateral rise','Peck deck'])
    text_input4 = st.number_input('Peso ejercicio 3')

    #st.write("You selected option", muscle_group)

else:
    p_legs = st.selectbox ('Pick your leg exercise',
                                   ['Deadlift','Glute bridge', 'Squat',])
    text_input1 = st.number_input('Peso pierna')

    p_upper = st.selectbox ('Pick your upper exercise',
                                   ['Pull ups','Seal row'])
    text_input2 = st.number_input('Peso ejercicio 1')

    p_upper_2 = st.selectbox ('Pick your second upper exercise',
                                   ['Rear delts','Seated row','Pull ups'])
    text_input3 = st.number_input('Peso ejercicio 2')

    P_upper_3 = st.selectbox ('Pick your third upper exercise',
                                   ['Standing barbell curl','Incline dumbbell curl','Cable curl'])
    text_input4 = st.number_input('Peso ejercicio 3')

    #st.write("Select something")

data = {
        "Exercise": [p_legs,p_upper,p_upper_2,P_upper_3], 
        "Peso": [text_input1,text_input2,text_input3,text_input4]
        }

df=pd.DataFrame(data)

if st.button("Save"):
    file_name = "data.csv"
    df.to_csv(file_name, index=False, mode='a', header=False)
    st.success("DataFrame saved to CSV file.") 
    # Clear the text inputs
    text_input1 = ""
    text_input2 = ""
    text_input3 = ""
    text_input4 = ""
    #st.clear_cache()


    





#st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
#st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
#st.slider('Pick a number', 0,300)
#st.number_input('Pick a number', 0,300)
#st.text_input('Email address')
#st.date_input('Travelling date')
#st.time_input('School time')
#st.text_area('Description')
#st.file_uploader('Upload a photo')
#st.color_picker('Choose your favorite color')


