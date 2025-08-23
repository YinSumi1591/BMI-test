import streamlit as st
import io
import requests
from pathlib import Path


# ChatGPT
def askAI(question):
    from openai import OpenAI
    client = OpenAI(api_key="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")
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # หรือ gpt-4o / o1-mini / o1-preview
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}] #จะถามไร
        , max_tokens=200
    )
    return response.choices[0].message.content



st.set_page_config(page_title='BODY MASS UNDEX : Web Application',page_icon='🏋️')
st.header('*สวัสดีฮับ*')
st.header('**มาลองดูกันว่า BMI ของคุณจะเท่าไหร่กัน**')
st.markdown("---")

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
st.error("อ้วนระดับ 2 (อันที่เป็นสีส้ม)")
st.error("อ้วนระดับ 3")

kg=st.number_input("น้ำหนัก(kg): ")
cm=st.number_input("ส่วนสูง(cm):")

if st.button('คำนวณ'):
    if kg != 0 and cm !=0:
        bmi = kg / (cm/100)** 2
        tt = f'ค่า BMI ของคุณคือ {bmi:.2f}'
        if bmi < 18.90:
            st.info(tt)
            st.image('BMI-Underweight.png')
        elif bmi < 23:
            st.success(tt)
            st.image('BMI-Normal.png')
        elif bmi < 25:
            st.warning(tt)
            st.image('BMI-Overweight.png')
        elif bmi < 30:
            st.error(tt)
            st.image('BMI-Obese.png')
        else:
            st.error(tt)
            st.image('BMI-Extremely Obese.png')
    else: st.error("PLEASE! go type your bmi numbers before press 'Button' here.")



    q=st.empty()
    q.write("รอผลวิเคราะสักครู่.....")
    question = f"บอกวิธีแก้คนที่มี BMI={bmi} ประมาณนี้"
    q.write(askAI(question))
