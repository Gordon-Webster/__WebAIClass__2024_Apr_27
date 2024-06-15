import streamlit as st


#text formatting
st.title('這是一個測試page')
st.write('## Hello! **_World_**')#markdown
st.markdown('### Step 1')
st.subheader('sub head')
st.divider()
st.code('''
    for rec in result.records:
        print(rec)
        '''
        )


#next, layout