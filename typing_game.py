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
    # 画像を表示
    st.image(os.path.join("./images", image_paths[st.session_state.image_index]), use_column_width=True)

    # 正解の名前を表示
    correct_name = kata2hira(os.path.splitext(image_paths[st.session_state.image_index])[0])
    st.write(f"{correct_name}")

    # ユーザーの入力を取得（ラベルを空に）
    typed_name = st.text_input("", key=f"img_name_{st.session_state.image_index}")

    if typed_name:  # 空でない場合のみ評価
        # print(typed_name.encode('utf-8'))
        # print(correct_name.decode())
        typed_name = unicodedata.normalize("NFKC", typed_name)
        correct_name = unicodedata.normalize("NFKC", correct_name)
        if typed_name in correct_name:
            # 次の画像へ
            st.success("正解！")
            st.session_state.image_index = (st.session_state.image_index + 1) % len(image_paths)
            # st.image(os.path.join("./images",image_paths[st.session_state.image_index]))
            st.experimental_rerun()
        else:
            st.error("不正解。もう一度試してください。")
