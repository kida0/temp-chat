import time
import streamlit as st

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="🐹"
)
st.title("DocumentGPT")

# with st.chat_message("human"):
#     st.write("Hellooo")
    
# with st.chat_message("ai"):
#     st.write("how are you")
    
# with st.status("Embedding_file...", expanded=True) as status:
#     time.sleep(2)
#     st.write("Getting the file")
#     time.sleep(2)
#     st.write("Embedding the file")
#     time.sleep(2)
#     st.write("Caching the file")
#     status.update(label="Error", state="error")
    
# 이렇게 사용하면 코드가 처음부터 모두 실행되며 해당 부분도 빈 리스트가 됨
messages = []

# data flow에서 데이터를 보존하는 구역
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# st.write(st.session_state["messages"])

def send_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state["messages"].append({"message": message, "role": role})
        
for message in st.session_state["messages"]:
    send_message(message["message"], message["role"], save=False)
        
message = st.chat_input("Send a message to ai")
if message:
    send_message(message, "human")
    time.sleep(2)
    send_message(f"You said: {message}", "ai")
    
    with st.sidebar:
        st.write(st.session_state)