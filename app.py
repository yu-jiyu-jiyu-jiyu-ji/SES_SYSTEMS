import streamlit as st
import pandas as pd

# ページレイアウト設定
st.set_page_config(layout="wide")

# サイドバー：検索条件
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

# メイン：タブ切り替え
tab1, tab2 = st.tabs(["案件情報", "人材情報"])

# 仮データ
案件データ = pd.DataFrame([
    {"件名": "案件A", "送信者": "abc@example.com", "受信日時": "2025-06-01", "単価": "80万円", "年齢": 35, "商深": 1, "個人": "有", "外国籍": "無"},
    {"件名": "案件B", "送信者": "def@example.com", "受信日時": "2025-06-02", "単価": "90万円", "年齢": 28, "商深": 2, "個人": "無", "外国籍": "有"},
])

人材データ = pd.DataFrame([
    {"件名": "エンジニアX", "送信者": "xyz@example.com", "受信日時": "2025-06-03", "単価": "75万円", "年齢": 40, "商深": 1, "個人": "有", "外国籍": "無"},
    {"件名": "エンジニアY", "送信者": "uvw@example.com", "受信日時": "2025-06-04", "単価": "70万円", "年齢": 32, "商深": 2, "個人": "無", "外国籍": "有"},
])

# 表示切り替えとソート可能テーブル
with tab1:
    st.markdown("### 各種情報（案件）")
    st.dataframe(案件データ, use_container_width=True)

with tab2:
    st.markdown("### 各種情報（人材）")
    st.dataframe(人材データ, use_container_width=True)
