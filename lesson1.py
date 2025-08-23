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
        else:
            st.error(tt)
            st.image('BMI-Extremely Obese.png')
            word="มึงอ้วนเกินไปแล้ววว"

        API_URL = "https://api-voice.botnoi.ai/openapi/v1/generate_audio"
        API_TOKEN = "SGsxeUd1wXuiu2UnLlakaNJHd4bbynSj"

        generate_btn = st.button("Generate Voice")

        if generate_btn:
            payload = {
                "text": if bmi < 18.90: "ผอมเกินไป"
                        elif bmi < 23: "ปกติ"
                        elif bmi < 25:"อ้วนนิดๆ"
                        elif bmi < 30: "อ้วนไปหน่อย"
                        else: "มึงอ้วนเกินไปแล้ววว",
                "speaker": speaker_id,
                "volume": 1,
                "speed": 1,
                "type_media": "mp3",
                "save_file": "true",
                "language": "th",                    
                "page": "user"
            }
            headers = {
                 "accept": "application/json",
                 "Content-Type": "application/json",
                 "botnoi-token": API_TOKEN
            }
            try:
                res = requests.post(API_URL, json=payload, headers=headers, timeout=30)
                res.raise_for_status()
                data = res.json()
                st.write("API Response:", data)

                # ดึง URL ไฟล์เสียง
                audio_url = (
                data.get("url")
                or data.get("audio_url")
                or (data.get("data") or {}).get("url")
                )

                if audio_url:
                    audio_bytes = requests.get(audio_url, timeout=30).content
                    out_path = Path("botnoi_voice.mp3")
                    out_path.write_bytes(audio_bytes)
                    st.success(f"✅ บันทึกเสียงเรียบร้อย → {out_path.resolve()}")
                    st.audio(audio_bytes, format="audio/mp3")
                else:
                    st.error("ไม่พบลิงก์ไฟล์เสียงใน response")

            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
            
    else: st.error("PLEASE! go type your bmi numbers before press 'Button' here.")



# ChatGPT
client = OpenAI(api_key="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")
response = client.chat.completions.create(
    model="gpt-4o-mini",  # หรือ gpt-4o / o1-mini / o1-preview
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "บอกวิธีแก้คนที่ BMI = {bmi} นี้"} #จะถามไร]
    , max_tokens=200)]
print(response.choices[0].message.content)
