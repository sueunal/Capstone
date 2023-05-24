import speech_recognition as sr

def slang_filter(text_list):
        lang_score = 100
        slang = 5
        for i in text_list:
                if i[-1] == '요': # 필터링 할 문자
                        print('어색한 단어가 발견 되었습니다.')
                        lang_score = lang_score - slang
        return lang_score

def fuck_lang_filter(text_list):
        slang = 5
        lang_score = 100
        for i in text_list:
                if i == '존나' or i == '아씨' or i == '미친': # 필터링 할 문자
                        print('비속어가 발견 되었습니다.')
                        lang_score = lang_score - slang
        return lang_score

def Consistency(text_list, script_list):
      text_score = 100 # 초기 점수 100점에서 틀릴 때마다 -5하는 방식
      for i in range(len(text_list)):
        if text_list[i] != script_list[i]: # 대본일치성 비교 
                text_score = text_score - 5
        else:
               continue # 대본이 일치하면 계속 교교
      return text_score
#r  = sr.Recognizer()
#with sr.AudioFile("audio.wav") as source:
        #audio = r.record(source, duration=120)

#text = r.recognize_google(audio_data = audio, language='ko-KR')
#text_list = text.split()  # 텍스트를 빈칸 기준으로 자라서 배열로 만들기
#script = "사람들이 많이 말하지 않는 치포의 진실을 좀 알려 드리겠습니다 진실을 알고 싶으면 요런 문서 들여다 보시면 됩니다 오픈 AI가 공개한 테크니컬 리포트 인데요 관련한 세부 내용들을 100페이지 정도로 정리 한 거예요 요거 읽어보시면 GPT 충격적인 내용들이 많이 담겨 있습니다 사람들이 얘기 많이 안 하는 단점들도 많이 적혀있고요 이거 읽으면서 재밌고 흥미로웠던 내용들이었기에 정리해드리자면 보시면 변호사시험을 30% 여성적으로 동거했다고 호들갑을 떨고 있는데 실제로 암기력과 읽기능력이 많이 필요한 문제들은 굉장히 잘 푸는 편히 근데 영어 작문 시험 이라든지 아니면 리트코드 상금 문제들 이런 것들은 아직 많이 어려워합니다 이런 식으로 문장생성 실력이 많이 필요한 문제들은 좀 어려워 하기 때문에 사람의 수학이랑 글쓰기 코딩능력 이런 것들은 완전히 대체 당하기까지 시간이 좀 더 필요한 거 같고요 그리고 이번 주 PT 보는 생각보다 최근 내용들을 많이 알지 못해 이전 버전 인체 집이랑 똑같이 2021 전에 데이터들로 학습을 진행했기 때문에 최근 내용들은 잘 몰라요 특히 개발자들이 입장에선 최신 기술 트렌드 같은 거 많이 아는 것도 중요한데 그런 점들은 GPT한테 도움을 많이 못 받을 것 같아서 좀 아쉽긴 한데 근데 쥐포는 이런 문제들을 고민할 필요가 없습니다 6만 2천 토크까지 입력할 수 있는 괴물 모델을 만들어 버렸기 때문에 그러니까 대충 A4 용지 50 전까지의 지시문을 한 번에 입력할 수 있다는 거예요 그래서 최신 라이브러리나 설명서 같은 거를 안 추려서 여기다가 이렇게 집어 넣어 버리면 최신 프레임업 도예가 문제없이 학습하고 바로 답변이 가능할 것 같습니다 GPT 이미지를 넣으면 이미지를 분석해 준다는 걸 보고 역 사람들이 많이 흥분하고 있습니다 근데 정확히 욕을 읽어보시면 차트 인포그래픽 그리고 다이어그램 이런 이미지들을 해석하는게 기존 모델들보다 뛰어난 뿐이고요 영화나 티비 쇼 아니면 현실사진 같은 걸 해석하는 그럼 테스트 같은 건 기존 모델보다 비슷하구나 낮은 수치를 기록하고 있습니다 그래서 현실 이미지를 해석"
#script_list = script.split()

#print("부적절한 단어 점수: ", slang_filter(text_list, lang_score))
#print("비속어 단어 점수: ", fuck_lang_filter(text_list, lang_score))
#print("대본 일치성 점수: ", Consistency(text_list,script_list))