# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:18:30 2024

@author: bishn
"""

import streamlit as st

st.image("360_F_304685223_ttVGVAkC5JlfgEOTO8KYbN4tjnRqM715.jpg")

#Title section
st.title(" Welcome to streamlit -This is Title-")

#Header section
st.header("machine learning")

#subheader
st.subheader("Linear regression")

#To give information

st.info("information details of user")

# warning maggege
st.warning("come one time")

#Error msg

st.error("wrong password")

#sucess messge

st.success("Congrates you have done good Job")

#write function ( can write code and text also)

st.write("Jai Shree Ram")
st.write("if 50>30 print greater")

#markdown
st.markdown("# Testing markdown")
st.markdown("## Testing markdown 2 ")
st.markdown(":smile:") # Emoji print

#text
st.text("leaning streamlit")

# to write caption

st.caption("Caption is here")

# to display mathmatics equations
st.latex(r''''a+ax+b''')
         
         
### widget ###

#check box
st.checkbox('login')

#button
st.button('click')

#radio button

st.radio("pick your gender",["Male","Female","Other"])

#selectbox
st.selectbox("pick your course",["Azure","Gcp","Aws"])

#Multiselect
st.multiselect("choose the department",["content","marketing","IT"])

#select slider

st.select_slider("Rating",["bad","good","Excelent","outstanding"])

#slider
st.slider("Enter your number",0,30)

#number input

st.number_input("pick your number", 0, 100)

#text input
st.text_input("enter you email")

#dateinput

st.date_input("Opening cermoney")

#st.time_input
st.time_input("whats the timing")

#text area for more than one line

st.text_area("white here")

#upload files

st.file_uploader("upload your file")

st.color_picker("color")

#progress

st.progress(90)

# spinner - it just show the messge while exicuting the process. ( temeporaray msg)

import time as t
with st.spinner("Just weight"):
    t.sleep(2)
    
#baloons

st.balloons()

#sidebar

st.sidebar.title("Welcome to here")

st.sidebar.text_input("your mail id")
st.sidebar.button("submit")
st.sidebar.radio("Student",["1st class","2nd Class"])

# Data Visualization

import pandas as pd
import numpy as np



data = pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.title("bar chart")
st.bar_chart(data)
st.title("line chart")
st.line_chart(data)

st.title("area chart")
st.area_chart(data)