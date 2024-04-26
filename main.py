# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

st.title('인공지능시인')

content = st.text_input('시의 주제를 제시해주세요')

if st.button('시 작성 요청하기'):
    with st.spinner('Wait for it...'):
        result = chat_model.invoke(content + '에 대한 시를 써줘')
        st.write(result)
    
# st.title('_Streamlit_ is :blue[cool] :sunglasses:')

# from langchain_openai import OpenAI
# llm = OpenAI()
# result = llm.invoke('내가 좋아하는 동물은는?')
# print(result)


# import streamlit as st
# from langchain_openai import ChatOpenAI
# from langchain_community.llms import CTransformers

# chat_model = ChatOpenAI()
# llm = CTransformers(
#     model="llama-2-7b-chat.ggmlv3.q3_K_S.bin",
#     model_type = "llama"
# )
# st.title('인공지능 시인')

# content = st.text_input('시의 주제를 제시해 주세요')

# if st.button('시 작성 요청하기'):
#     with st.spinner('시 작성 중....'):
#         result = llm.invoke(content + "에 대한 시를 써줘")
#        st.write(result)