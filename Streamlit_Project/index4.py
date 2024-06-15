#EMPTY container
import streamlit as st
import time

# with st.empty():
#     for seconds in range(60):
#         st.write(f"{seconds} seconds have passed")
#         time.sleep(1)
    
#     st.write("😜 1 minute over!")

placeholder = st.empty()
with placeholder:
    for seconds in range(10):
        st.write(f'{seconds} seconds have passed')
        time.sleep(1)

    st.write('1 minutes over!')

time.sleep(5)
placeholder.empty()
