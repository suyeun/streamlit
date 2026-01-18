import streamlit as st
from llm import get_ai_response

st.set_page_config(page_title="소득세 챗봇", page_icon=":robot_face:")

st.title("소득세 챗봇")
st.caption("소득세에 관련된 모든것을 답해드립니다.!")

if 'message_list' not in st.session_state:
    st.session_state.message_list = []


for mseeage in st.session_state.message_list:
    with st.chat_message(mseeage["role"]):
        st.write(mseeage["content"])



if user_question := st.chat_input("소득세에 관련된 궁금한 내용들을 말씀해주세요."):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("AI가 답변을 생성중입니다...."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})

