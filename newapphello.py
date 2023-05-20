# simple app to test streamlit 

import streamlit as st


st.title("Hello World!")
st.header("This is a header")
st.subheader("This is a subheader click here : https://www.youtube.com/")

st.write("simple test for streamlit")
if st.button("Click Me"):
	st.write("You clicked me!")
	st.balloons()


st.sidebar.header("This is a sidebar")

# create a button in the sidebar
button = st.sidebar.button(label="Press me please")

if button:
	st.sidebar.write("Hello there")
	st.sidebar.balloons()
	

# create 2 columns first with 2/3
col1, col2 = st.columns([3,1])

col1.header("This is column 1")
col1.write("This is column 1")
col2.header("This is column 2")
col2.write("This is column 2")

option=st.selectbox('how would you like to be contacted?',
('email','home phone','mobile phone')
)
st.write('you selected',option)




