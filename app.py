import streamlit as st
import joblib 

# load jobib model
model_nb = joblib.load('spam-ham')

st.title('Spam Ham Classiffier')
ip = st.text_input('Enter your text : ')
op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
