import streamlit as st

#check cookies in front end aka session in back end
if 'robert' not in st.session_state:
    st.session_state['robert'] = 30


st.session_state['robert']
st.session_state.robert = 50
st.session_state.robert