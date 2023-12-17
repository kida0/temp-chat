import streamlit as st
from langchain.prompts import PromptTemplate
from datetime import datetime

st.title("Hello world!")
st.subheader("Welcome to Streamlit")
st.markdown("""
#### I love it
""")

# write
st.write("write option -----")
st.write([1, 2, 3, 4])
st.write({"x": 1})
st.write(PromptTemplate)

p = PromptTemplate.from_template("xxxx")
st.write(p)

st.selectbox("Choose your mode", ("GPT-3", "GPT-4"))


# 데이터를 변경하면 전체 파일이 실행됨
today = datetime.today().strftime("%H:%M:%S")
st.title(today)

model = st.selectbox(
    "Choose your model",
    (
        "GPT-3",
        "GPT-4",
    ),
)
st.write(model)

name = st.text_input("What is your name?")
st.write(name)

# slider의 값을 변경하면 모든 코드가 재실행 -> 위의 datetime이 바뀌는 모습 확인 가능
value = st.slider("temperature", min_value=0.1, max_value=1.0)
st.write(value)


if model == "GPT-3":
    st.write("cheap")
else:
    st.write("not cheap")
    name = st.slider("temp", min_value=0.1, max_value=1.0)
    st.write(name) 




st.title("title")

with st.sidebar:
    st.title("sidebar title")   # st.sidebar.title("")
    st.text_input("xxx")        # st.sidebar.text_input("")
    
tab_one, tab_two, tab_three = st.tabs(["A", "b", "C"])
with tab_one:
    st.write("A")
    
with tab_two:
    st.write("B")
    
with tab_three:
    st.write("C")    