import anthropic
import os
import json
import random

KEYWORDS = [
    ("성장", "자기계발"), ("감사", "마음챙김"), ("도전", "용기"),
    ("행복", "일상"), ("관계", "인간관계"), ("긍정", "멘탈"),
    ("꿈", "목표"), ("변화", "새로운시작"), ("사랑", "진심"),
    ("회복력", "극복"), ("현재", "마음챙김"), ("노력", "성실"),
]

STYLES = [
    {"tone": "따뜻하고 공감하는", "structure": "짧은 통찰 + 행동 제안"},
    {"tone": "깊고 사색적인", "structure": "질문으로 시작 + 메시지"},
    {"tone": "밝고 에너지 넘치는", "structure": "선언적 문장 + 격려"},
    {"tone": "잔잔하고 위로하는", "structure": "현실 공감 + 희망 제시"},
]

def generate_quote_content():
    client = anthropic.Anthropic(api_key=os.environ["CLAUDE_API_KEY"])
    keyword, category = random.choice(KEYWORDS)
    style = random.choice(STYLES)

    prompt = (
        "당신은 페이스북에서 인생조언과 감성 명언으로 큰 공감을 얻는 콘텐츠 크리에이터입니다.\n\n"
        "오늘의 주제: " + keyword + "\n"
        "카테고리: " + category + "\n"
        "글쓰기 톤: " + style["tone"] + "\n"
        "구성 방식: " + style["structure"] + "\n\n"
        "다음 조건을 지켜 페이스북 포스트를 작성해주세요:\n"
        "- 한국어로 작성, 총 5~8줄\n"
        "- 이모지 2~3개 자연스럽게 포함\n"
        "- 마지막 줄은 저장하거나 공유하고 싶게 만드는 한 문장\n"
        "- 광고나 홍보 느낌 없이, 진심 어린 글처럼\n"
        "- 해시태그 3~5개 마지막에 추가\n\n"
        "그리고 위 한국어 내용을 자연스러운 영어로도 번역해주세요 (text_en):\n"
        "- 직역 말고 영어 원어민이 쓸 법한 자연스러운 표현으로\n"
        "- 이모지는 동일하게 유지\n\n"
        "JSON으로 반환:\n"
        '{"text": "전체 내용 (해시태그 포함)", "text_en": "English version"}'
    )

    try:
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        raw = message.content[0].text.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        return json.loads(raw)
    except Exception as e:
        print(f"Error generating content: {e}")
        return {
            "text": "오늘 하루도 수고했어요 ✨\n작은 것에도 감사할 줄 아는 사람이\n결국 가장 행복한 사람입니다.\n\n#좋은글 #오늘의명언 #힘내요 #감성글 #공감",
            "text_en": "You've worked hard today ✨\nThe person who can find gratitude in small things\nis ultimately the happiest.\n\n#goodwords #dailyquote #keepgoing #motivation #empathy"
        }
