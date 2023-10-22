import streamlit as st

st.title("title") # タイトル
st.header("header") # ヘッダー
st.write("write") # 表示
st.markdown("# markdown") # マークダウンで表示
st.text("text") # テキスト表示

st.sidebar.text_input("text input")
st.sidebar.text_area("text area")
st.sidebar.slider("slider", 0, 100, 50)
st.sidebar.file_uploader("Choose file")