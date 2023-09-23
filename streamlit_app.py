import os
import streamlit as st
import replicate
import pandas

# App title
st.set_page_config(page_title="blissful 🎈: Powered by 🦙💬 Llama 2 Chatbot")

with st.sidebar:
    st.title('blissful 🎈: Powered by 🦙💬 Llama 2 Chatbot')
    
    """
    Replicate API creds
    """
    # If replicate API token already provided
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    os.environ['REPLICATE_API_TOKEN'] = replicate_api