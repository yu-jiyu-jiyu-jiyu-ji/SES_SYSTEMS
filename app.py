import streamlit as st

# ページ設定
st.set_page_config(layout="wide")

# サイドバー（メニュー）
menu = st.sidebar.radio("表示切替", ["案件情報", "人材情報"])

# 左側：検索パネル
with st.sidebar:
    st.markdown("### テキスト")
    件名 = st.text_input("件名")
    受信日時 = st.text_input("受信日時")
    単価 = st.text_input("単価")
    年齢 = st.text_input("年齢")
    商深 = st.text_input("商深")

    col1, col2 = st.columns(2)
    with col1:
        個人 = st.radio("個人", ["有", "無"], index=0)
    with col2:
        外国籍 = st.radio("外国籍", ["有", "無"], index=0)

    if st.button("検索"):
        st.success("検索処理を実行しました（仮）")

# メインエリア
st.markdown("### 各種情報")

# テーブル表示エリア（仮データ）
import pandas as pd

# 仮のデータ（必要に応じて置き換え）
df = pd.DataFrame([
    {"件名": "案件A", "送信者": "sender1@mail.com", "受信日時": "2025-06-09",
     "単価": "70万円", "年齢": 35, "商深": 2, "個人": "有", "外国籍": "無"},
    {"件名": "案件B", "送信者": "sender2@mail.com", "受信日時": "2025-06-08",
     "単価": "85万円", "年齢": 28, "商深": 1, "個人": "無", "外国籍": "有"}
])

st.dataframe(df, use_container_width=True)
