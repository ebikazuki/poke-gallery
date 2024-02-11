import streamlit as st
import os
import random
import unicodedata
from jaconv import kata2hira


# 画像のパスを取得
image_paths = [f for f in os.listdir("./image") if f.endswith(".png")]

# セッションステートの設定
if "image_index" not in st.session_state:
    st.session_state.image_index = random.randint(0, len(image_paths) - 1)

# Streamlit layoutの中央に配置するための設定
col1, col2, col3 = st.columns([1,2,1])

with col2:

    # 正解の名前を表示
    correct_name = kata2hira(os.path.splitext(image_paths[st.session_state.image_index])[0])
    st.markdown(f"""
    <div style="text-align: center; font-size: 32px;">
        {correct_name}
    </div>
""", unsafe_allow_html=True)
    
    # 画像を表示
    st.image(os.path.join("./image", image_paths[st.session_state.image_index]), use_column_width=True)
    
    if st.button("つぎへ"):  
        st.session_state.image_index = (st.session_state.image_index + 1) % len(image_paths)
        st.experimental_rerun()
