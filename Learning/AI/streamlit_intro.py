import streamlit as st

# title
st.title("Intro to streamlit")

# heading
st.header("This is header.")

# sub heading
st.subheader("This is subheader.")

# plain text
st.text("This is simple text.")

# markdown
st.markdown("This is markdown")

#button
st.button("This is button")

# checkbox
st.checkbox("This is checkbox")

# radio
st.radio("Radio",["Option1","Option2","Option3"])

# selectbox
st.selectbox("Select",["Option1","Option2","Option3"])

# multiselect
st.multiselect("Multiselect",["Option1","Option2","Option3"])

# file uploader
st.file_uploader("File uploader")

# color picker
st.color_picker("Color pick")

# date input
st.date_input("Date")

# time input
st.time_input("Time")

# text input
st.text_input("Text input", placeholder="What is your name?")

# number input
st.number_input("Number input", value=00,min_value=0,max_value=100)

# text area
st.text_area("Text area")

# slider
st.slider("Slider", min_value=0, max_value=100, value=0)

# progress bar
# import time
# my_bar = st.progress(0)
# for percentagecomplete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percentagecomplete + 1)

# # spinner
# with st.spinner("Waiting ..."):
#     time.sleep(5)
    
# Column
col1,col2 = st.columns(2)

with col1:
    col1.header("Col1")
    col1.text("Hello world")

with col2:
    col2.header("Col2")
    col2.text("How are you?")

# image 
image = st.file_uploader("File uploader",type=["jpeg","png","jpg"])
if image:
    st.image(image,caption="Image upload",use_column_width=True)

