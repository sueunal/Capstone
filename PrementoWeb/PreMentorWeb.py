import streamlit as st
import os
import pandas as pd

from PreMentorModule.Slang import *
from PreMentorModule.Virustotal import *

def intro():
    import streamlit as st
    st.write("##### 👈 다음 페이지로 이동하시려면 버튼을 눌러주세요")
    st.write("# 👨‍🏫PreMentor")
    st.markdown(
        """ 
        
        **:blue[인공지능 발표 교정시스템입니다.]**   
        **발표를 진행할 때 :red[긴장감]이나 :red[두려움]을 느끼는 사용자에게 도움이 되는 서비스입니다.**
        #### 🛠️ 제공 되는 기능은 다음과 같습니다.
        - 맞춤법 및 반복단어 검사  
        - 어색한 단어, 비속어 검사   
        - 음성 파일과 입력한 대본의 정확도 측정   
        - 입력한 파일의 수치화된 데이터 제공   
        """
    )
    st.write("----")
    st.write("### 발표의 중요성💡")
    

def PresentationScript():
    import streamlit as st
    from hanspell import spell_checker

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
            return st.success("파일 업로드가  완료 되었습니다. : {}".format(file.name),icon="🔥")

    st.write("# 📑 대본 파일 업로드 페이지 입니다.")
    st.markdown("""
        대본 파일을 업로드 하여 맞춤법을 교정하고 대본과 실제 발표했을 때 차이를 확인하세요.   
        대학교 2학년 7월부터 다음에 1월에 거쳐 다 지키 스크린은 거의 죽음만은 생각하면서 알았다 
        그 사이 20살 생일을 맞이해 찜 한 그 비념 일은 아무런 의미가 없었다   
        그러나 날 속에서 그는 스스로 생명을 끊는 것이 무엇보다도 자연스럽고 합리적이라고 생각했다 그런데 왜 마지막 한걸음에 내리지 못했는지 지금은 지금도 그는 이유를 잘 모른다 그때라면 삶과 죽음의 가루는 가면은 문지방을 넘어서는 이따위 날달걀 하나 드릴 기능 것보다 간다 했는데
   """)
    st.write("#### 📑 대본 파일업로드")
    uploaded_files = st.file_uploader(".txt 파일을 업로드해주세요", accept_multiple_files=True)
    if st.button("평가 시작하기!"):
        with st.spinner('처리중입니다..\n잠시만 기다려주세요 '):
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                save_uploaded_file('temp',uploaded_file)

        f = open("temp/"+uploaded_file.name,'r')
        line = f.readline()
        re_texted =  spell_checker.check(line)
        st.write("### ⛏ ️교정전 대본")
        st.markdown(re_texted.original)
        st.write("### ⚙️ 교정된 대본")
        st.markdown(re_texted.checked)
        f.close()


def plotting_demo():
    import streamlit as st
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
            return st.success("파일 업로드가  완료 되었습니다. : {}".format(file.name),icon="🔥") 

    st.write("# 🎤음성 파일 검사 페이지 입니다.")
    st.markdown(
        """
        **자신의 발표 음성파일을 업로드 하여 :red[어색한 단어, 부적절한 단어, 비속어] 등을 검사하여 점수를 부여합니다.   
        점수는 어색한 단어, 부적절한 단어, 비속어를 포함하는 단어가 나올 때마다 5점 감점하는 형식으로 진행됩니다.   
        :green[지극히 주관적으로 진행되는 것이니 점수에 크게 동요하지 않으셔도 됩니다.]**
"""
    )
    st.markdown("""
        ### 🧾점수 부여 기준
        - 부적절한 단어 : 5점 감점
        - 어색한 단어 : 5점 감점
        - 비속어 : 30점 감점
                """)
    st.write("#### 📁 음성 파일업로드")
    uploaded_files = st.file_uploader(".wav파일을 업로드해주세요", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        save_uploaded_file('voice_temp',uploaded_file)

    if st.button("평가 시작하기!"):
        with st.spinner('처리중입니다..\n잠시만 기다려주세요 '):
            r  = sr.Recognizer()
            with sr.AudioFile("temp/"+ uploaded_file.name) as source:
                audio = r.record(source, duration=120)
                origin_text = r.recognize_google(audio_data = audio, language='ko-KR')
                text_list = origin_text.split()  # 텍스트를 빈칸 기준으로 자라서 배열로 만들기
                awkward_score = slang_filter(text_list=text_list)
                slang_score =  fuck_lang_filter(text_list=text_list)
                data = pd.DataFrame({
                    '어색한 단어 점수': [awkward_score,0,0],
                    '비속어 단어 점수' : [0,slang_score,0],
                    '정확도 점수' : [0,0,55] 
                })

        st.write("#### 📝결과화면")
        st.bar_chart(data)
    


def AIPosture():
    import streamlit as st
    import pandas as pd
    import altair as alt

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write(
        """
        This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
"""
    )

    @st.cache_data
    def get_UN_data():
        AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
        return df.set_index("Region")

    try:
        df = get_UN_data()
        countries = st.multiselect(
            "Choose countries", list(df.index), ["China", "United States of America"]
        )
        if not countries:
            st.error("Please select at least one country.")
        else:
            data = df.loc[countries]
            data /= 1000000.0
            st.write("### Gross Agricultural Production ($B)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                    color="Region:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )
page_names_to_funcs = {
    "PreMentor Introduce": intro,
    "Voice Simulation": plotting_demo,
    "Presentation Script":PresentationScript,
    "AI Posture": AIPosture
}

demo_name = st.sidebar.selectbox("Choose a Presentaion Test Page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()