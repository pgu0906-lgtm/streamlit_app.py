import streamlit as st
st.write("Hello World")
import streamlit as st
import base64
from openai import OpenAI

st.title("gpt-5-mini + gpt-image-1-mini 웹 앱")

# ---------------------------
# 공통: OpenAI API Key 입력
# ---------------------------
api_key = st.text_input("OpenAI API Key를 입력하세요", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None
    st.info("먼저 OpenAI API Key를 입력하세요.")

# ---------------------------
# 4. 텍스트 질문 → gpt-5-mini
# ---------------------------
st.header("4. gpt-5-mini 텍스트 응답")

user_question = st.text_area(
    "질문을 입력하세요",
    placeholder="예) 인공지능이 뭐예요?"
)

if st.button("GPT에게 물어보기"):
    if client is None:
        st.error("OpenAI API Key를 입력해야 합니다.")
    elif not user_question.strip():
        st.error("질문을 입력하세요.")
    else:
        with st.spinner("응답 생성 중..."):
            try:
                response = client.responses.create(
                    model="gpt-5-mini",
                    input=user_question
                )
                # 텍스트 응답
                answer = response.output_text

                st.subheader("GPT의 답변")
                st.write(answer)
            except Exception as e:
                st.error(f"에러 발생: {e}")

# ---------------------------
# 5. 프롬프트 → gpt-image-1-mini
# ---------------------------
st.markdown("---")
st.header("5. gpt-image-1-mini 이미지 생성")

image_prompt = st.text_area(
    "이미지 프롬프트를 입력하세요",
    placeholder="예) 파란 하늘 아래 초록 들판에서 책 읽는 고양이 일러스트"
)

if st.button("이미지 생성하기"):
    if client is None:
        st.error("OpenAI API Key를 입력해야 합니다.")
    elif not image_prompt.strip():
        st.warning("이미지 프롬프트를 먼저 입력하세요.")
    else:
        with st.spinner("이미지 생성 중..."):
            try:
                img = client.images.generate(
                    model="gpt-image-1-mini",
                    prompt=image_prompt
                )

                # b64_json → 이미지 바이트로 디코딩
                image_bytes = base64.b64decode(img.data[0].b64_json)

                st.subheader("생성된 이미지")
                st.image(image_bytes)
            except Exception as e:
                st.error(f"이미지 생성 중 에러 발생: {e}")






