import streamlit as st
import io
import requests
from pathlib import Path

st.set_page_config(page_title='BODY MASS UNDEX : Web Application',page_icon='🏋️')
st.header('*สวัสดีฮับ*')
st.header('**มาลองดูกันว่า BMI ของคุณจะเท่าไหร่กัน**')

st.image('BMI.jpg')

col1,col2 = st.columns(2)
with col1:
    if st.button('ฟังเพลง Murder Drone - Bite Me'):
        st.video('https://youtu.be/D7_2_j6-VfQ')
with col2:
    if st.button('ฟัง meme (Warning:Brainrot)'):
        st.video('https://www.youtube.com/shorts/5fOIjOgqmvw?feature=share')

st.info("ผอม")
st.success("ปกติ")
st.warning("อ้วนระดับ 1")
st.error("อ้วนระดับ 2 (อันที่เป็นสีีส้ม)")
st.error("อ้วนระดับ 3")

kg=st.number_input("น้ำหนัก(kg): ")
cm=st.number_input("ส่วนสูง(cm):")

if st.button('คำนวณ'):
    bmi = kg / (cm/100)** 2
    tt = f'ค่า BMI ของคุณคือ {bmi:.2f}'
    if bmi < 18.90:
        st.info(tt)
        st.image('BMI-Underweight.png')
        word="ผอมเกินไป"
    elif bmi < 23:
        st.success(tt)
        st.image('BMI-Normal.png')
        word="ปกติ"
    elif bmi < 25:
        st.warning(tt)
        st.image('BMI-Overweight.png')
        word="อ้วนนิดๆ"
    elif bmi < 30:
        st.error(tt)
        st.image('BMI-Obese.png')
        word="อ้วนไปหน่อย"
    elif bmi < 35:
        st.error(tt)
        st.image('BMI-Extremely Obese.png')
        word="มึงอ้วนเกินไปแล้ววว"
    elif kg = 0 or cm = 0:
        st.error("PLEASE! go type your bmi numbers before press 'Button' here.")

    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    st.audio(mp3_fp, format='audio/mp3')
