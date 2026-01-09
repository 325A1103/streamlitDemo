import streamlit as st

import random
st.title("はじめてのStreamlitアプリ")
st.write("## Hello, World!")
st.title("🎯 Hit & Blowゲーム")

# --- 初期化 ---
if "answer" not in st.session_state:
    st.session_state.answer = random.sample("012345", 4)
    st.session_state.history = []
    st.session_state.giveup = False

# --- 入力 ---
guess = st.text_input("重複なしの4桁(０～５)数字を入力してください")

# --- ボタンUI ---
col1, col2 = st.columns(2)

with col1:
    judge = st.button("判定")

with col2:
    giveup = st.button("🏳️ ギブアップ")

# --- ギブアップ処理 ---
if giveup:
    st.session_state.giveup = True

# --- ギブアップ後の画面 ---
if st.session_state.giveup:
    st.error("ギブアップしました…")
    st.image("images/giveup.jpg", caption="また挑戦しよう！", use_container_width=True)
    st.write("正解は 👉", "".join(st.session_state.answer))

    if st.button("🔄 もう一度"):
        st.session_state.clear()

    st.stop()

# --- 判定処理 ---
if judge:
    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
        st.warning("4桁の重複しない数字を入力してください")
    else:
        hit = sum(a == b for a, b in zip(guess, st.session_state.answer))
        blow = sum(g in st.session_state.answer for g in guess) - hit

        st.session_state.history.append(
            {"guess": guess, "hit": hit, "blow": blow}
        )

        # --- 正解時 ---
        if hit == 4:
            st.success("🎉 正解！")
            st.image("images/seikai.png", caption="クリア！", use_container_width=True)
            st.write("答え:", "".join(st.session_state.answer))

            if st.button("🔄 もう一度"):
                st.session_state.answer = random.sample("012345", 4)
                st.session_state.history = []
                st.session_state.giveup = False


            st.stop()

# --- 履歴表示 ---
st.write("----------------------------------")
st.subheader("📝履歴")
for h in st.session_state.history:
    st.write(f"{h['guess']} → Hit: {h['hit']} / Blow: {h['blow']}")