import streamlit as st 
import os
import speech_recognition as sr
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
from Slang import *
from Virustotal import *

def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    if file_hashing(uploaded_file.name):
        st.warning("바이러스가 존재합니다 다른 파일을 이용해주세요.",icon="🚨")
        return False
    else:
        return st.success("Success File : {} in {}".format(file.name, directory))
   
st.write(
   """ 
   # 👨‍🏫PreMento
   **:blue[인공지능 발표 교정시스템입니다.]**   
   **발표를 진행할 때 :red[긴장감]이나 :red[두려움]을 느끼는 사용자에게 도움이 되는 서비스입니다.**
   #### 🛠️ 제공 되는 기능은 다음과 같습니다.
   - 맞춤법 및 반복단어 검사  
   - 어색한 단어, 비속어 검사   
   - 음성 파일과 입력한 대본의 정확도 측정   
   - 입력한 파일의 수치화된 데이터 제공   
   """
)
st.write("#### 📁파일업로드")
uploaded_files = st.file_uploader(".wav파일을 업로드해주세요", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    save_uploaded_file('temp',uploaded_file)

if st.button("결과 확인!"):
    r  = sr.Recognizer()
    with sr.AudioFile("temp/"+ uploaded_file.name) as source:
        audio = r.record(source, duration=120)
    origin_text = r.recognize_google(audio_data = audio, language='ko-KR')
    text_list = origin_text.split()  # 텍스트를 빈칸 기준으로 자라서 배열로 만들기
    awkward_score = slang_filter(text_list=text_list)
    slang_score =  fuck_lang_filter(text_list=text_list)

    st.write("#### 📝결과화면")
    data = pd.DataFrame({
        '어색한 단어 점수': [awkward_score,0,0],
        '비속어 단어 점수' : [0,slang_score,0],
        '정확도 점수' : [0,0,55] 
    })
    st.bar_chart(data)
    st.area_chart(data)
    st.write(data)


#script = "사람들이 많이 말하지 않는 치포의 진실을 좀 알려 드리겠습니다 진실을 알고 싶으면 요런 문서 들여다 보시면 됩니다 오픈 AI가 공개한 테크니컬 리포트 인데요 관련한 세부 내용들을 100페이지 정도로 정리 한 거예요 요거 읽어보시면 GPT 충격적인 내용들이 많이 담겨 있습니다 사람들이 얘기 많이 안 하는 단점들도 많이 적혀있고요 이거 읽으면서 재밌고 흥미로웠던 내용들이었기에 정리해드리자면 보시면 변호사시험을 30% 여성적으로 동거했다고 호들갑을 떨고 있는데 실제로 암기력과 읽기능력이 많이 필요한 문제들은 굉장히 잘 푸는 편히 근데 영어 작문 시험 이라든지 아니면 리트코드 상금 문제들 이런 것들은 아직 많이 어려워합니다 이런 식으로 문장생성 실력이 많이 필요한 문제들은 좀 어려워 하기 때문에 사람의 수학이랑 글쓰기 코딩능력 이런 것들은 완전히 대체 당하기까지 시간이 좀 더 필요한 거 같고요 그리고 이번 주 PT 보는 생각보다 최근 내용들을 많이 알지 못해 이전 버전 인체 집이랑 똑같이 2021 전에 데이터들로 학습을 진행했기 때문에 최근 내용들은 잘 몰라요 특히 개발자들이 입장에선 최신 기술 트렌드 같은 거 많이 아는 것도 중요한데 그런 점들은 GPT한테 도움을 많이 못 받을 것 같아서 좀 아쉽긴 한데 근데 쥐포는 이런 문제들을 고민할 필요가 없습니다 6만 2천 토크까지 입력할 수 있는 괴물 모델을 만들어 버렸기 때문에 그러니까 대충 A4 용지 50 전까지의 지시문을 한 번에 입력할 수 있다는 거예요 그래서 최신 라이브러리나 설명서 같은 거를 안 추려서 여기다가 이렇게 집어 넣어 버리면 최신 프레임업 도예가 문제없이 학습하고 바로 답변이 가능할 것 같습니다 GPT 이미지를 넣으면 이미지를 분석해 준다는 걸 보고 역 사람들이 많이 흥분하고 있습니다 근데 정확히 욕을 읽어보시면 차트 인포그래픽 그리고 다이어그램 이런 이미지들을 해석하는게 기존 모델들보다 뛰어난 뿐이고요 영화나 티비 쇼 아니면 현실사진 같은 걸 해석하는 그럼 테스트 같은 건 기존 모델보다 비슷하구나 낮은 수치를 기록하고 있습니다 그래서 현실 이미지를 해석"
#script_list = script.split()
#print("대본 일치성 점수: ", Consistency(text_list,script_list))