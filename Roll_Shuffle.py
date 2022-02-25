import streamlit as st
import numpy as np
import pandas as pd
import random

roll_list = ["TOP","JG","MID","ADC","SUP"]

st.title("LOL自動ロール振り分け")
st.write("""
    ### 今んとこフルパでしか対応してない
     """)
players = st.text_area("1人ずつ改行してプレイヤー入力しやがれ",height=140)

if st.button("振り分け"):
    try:     
        player_list = []
        player_list=players.splitlines()
        random.shuffle(player_list)

        roll_table = pd.DataFrame({
            "Roll" : roll_list,
            "Player" : player_list
        })

        col_list=st.columns(5)
        for i in range(5):
            col_list[i].metric(label=roll_list[i],value=player_list[i])
            
    except:
        st.write("人数おかしい")