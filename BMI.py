import streamlit as st
import pickle
import numpy as np


st.title("BMI Calculator")
st.header("Welcome to Health Insights")
st.write("Please enter your height and weight to calculate your BMI.")


weight_measure=st.radio("Select your weight measure:", ("Kilograms", "Pounds"))
weight=st.number_input("Weight ",  min_value=0.1)

height_measure=st.radio("Select your height measure:", ("Centimeters", "Inches"))
height=st.number_input("Height",  min_value=0.1)


if weight_measure == "Kilograms" and height_measure == "Centimeters":
    height_m = height / 100
    weight_kg = weight

elif weight_measure == "Kilograms" and height_measure == "Inches":
    height_m = height / 39.37
    weight_kg = weight

elif weight_measure == "Pounds" and height_measure == "Inches":
    height_m = height / 39.37
    weight_kg = weight / 2.205

elif weight_measure == "Pounds" and height_measure == "Centimeters":
    height_m = height / 100
    weight_kg = weight / 2.205

BMI = weight_kg / (height_m ** 2)


if st.button("Calculate BMI"):
    if BMI<18:
        st.write("Your BMI : ", BMI)
        st.error("You're underweight")
        gain=(-18.5*(height_m**2))+weight_kg
        st.write("You need to gain " + str(round(abs(gain), 2)) + " kgs")
    if 18<BMI<25:
        st.write("Your BMI : ", BMI)
        st.success("Your weight is normal")
    if 25<BMI<30:
        st.write("Your BMI : ", BMI)
        st.warning("You're overweight")
        gain=(24.5*(height_m**2))-weight_kg
        st.write("You need to lose " + str(round(abs(gain), 2)) + " kgs")
    if 30<BMI:
        st.write("Your BMI : ", BMI)
        st.error("You're obese")
        gain=(24.5*(height_m**2))-weight_kg
        st.write("You need to lose " + str(round(abs(gain), 2)) + " kgs")
    