import streamlit as st
import pandas


data = {
    'series 1': [1,3,4,5,7],
    'series 2': [10, 30, 40, 50, 70]
}

df = pandas.DataFrame(data)
st.title('Our First Streamlit Web App')
st.subheader('Introducing Streamlit in Automate Everything With Python')
st.write('''
This is my first web App
This is a new line
''')
st.write(df)
st.line_chart(df)
st._arrow_area_chart(df)