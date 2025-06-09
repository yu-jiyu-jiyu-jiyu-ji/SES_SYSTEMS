import streamlit as st

st.title("こんにちは！")
st.write("これはStreamlitで作ったアプリです。")


# import streamlit as st

st.title("案件・人材検索システム")
st.write("ようこそ！ここではメールから抽出した情報を検索できます。")

name = st.text_input("氏名または案件名を入力")
if st.button("検索"):
    st.write(f"検索結果: {name} に関連する情報は見つかりませんでした（仮）")
