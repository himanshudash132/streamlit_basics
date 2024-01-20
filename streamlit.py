import streamlit as st 
import time as t
import pandas as pd
import numpy as np
# streamlit run streamlit.py

st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")

# title - It is used to add the title of an app
st.title("Welcome to HimanshuDash website")

# Header
st.header("Machine Learning")

# sub Header
st.subheader("Machine Learning")

# To give Info
st.info("Information details of a user")

# Warning Message
st.warning("warning message")

# write
st.write("Name")
st.write(range(50))

# error
st.error("error message")

# success Message
st.success("success message")

# markdown
st.markdown("# Himanshu")
st.markdown("## Himanshu")
st.markdown("### Himanshu")
st.markdown(":moon:")

# text Message
st.text("Smart learner")

# caption Message
st.caption("Caption is here")

# display Mathematical equations
st.latex(r''' a+b x^2+c''')

# widget

# checkbox
st.checkbox("Login")

# button
st.button("click")

# Radio widget
st.radio("Pick your gender",["Male","Female","other"])

# multiselect
st.selectbox("Pick your dept",["Ml","dp","security"])

# multiselect
st.multiselect("Pick your dept",["Ml","dp","security"])

# select_slider
st.select_slider("Rating",["Bad","Good","Excellent","Outstanding"])

# slider
st.slider("Enter your number",0,100)

# number_input
st.number_input("Enter your number",0,100)

# text_input
st.text_input("Enter your email Address")

# date_input
st.date_input("Date")

# time_input
st.time_input("time")

# text_area
st.text_area("Enter anything")

# file_uploader
st.file_uploader("file uploader")

# color_picker
st.color_picker("color")

# progress
st.progress(2)

with st.spinner("just wait"):
     t.sleep(1)

# balloons
st.balloons()     

# sidebar
st.title("wow")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("Password")
st.sidebar.button("submit")
st.sidebar.radio("profession",["Student","Working","Othets"])


# Data visualization
data=pd.DataFrame(np.random.rand(50,2),columns=["x","y"])
st.title("Bar chart")
st.bar_chart(data)
st.title("line chart")
st.line_chart(data)
st.title("Area chart")
st.area_chart(data)
