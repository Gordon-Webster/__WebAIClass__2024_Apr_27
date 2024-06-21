import streamlit as st
import time


# Just add it after st.sidebar:
# a = st.sidebar.radio('Choose a method:',['State','Callback'])

#with notation

with st.sidebar:
    st.radio('Choose a method:',['Session State','Callback'])

#     # Group multiple widgets:
# with st.form(key='my_form'):
#     ht = st.text_input('Height')
#     wt = st.text_input('Weight')
    
#     # checkbox_val = st.checkbox('Form checkbox')
    

#     st.form_submit_button('Calculate') 


if 'sum' not in st.session_state:
    st.session_state.sum = ''

col1,col2 = st.columns(2)

with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('add')

col2.title('BMI Status:')
if isinstance(st.session_state.sum, float):
    col2.title(f'{st.session_state.sum:.2f}')
# The value of st.session_state.sum is updated at the end of the script rerun,
# so the displayed value at the top in col2 does not show the new sum. Trigger
# a second rerun when the form is submitted to update the value above.
st.session_state.sum = a + b
if submit:
    st.rerun()