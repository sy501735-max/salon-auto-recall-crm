"""
hashtag_generator.py
주제 및 시즌에 맞는 인스타그램 해시태그 자동 생성
"""

# 시술별 해시태그
SERVICE_TAGS = {
    "펌": ["#펌", "#웨이브펌", "#볼륨매직", "#헤어펌", "#파마", "#웨이브헤어"],
    "염색": ["#염색", "#헤어컬러", "#퍼스널컬러", "#블리치", "#헤어염색", "#컬러"],
    "커트": ["#커트", "#헤어커트", "#스타일링", "#단발", "#레이어드컷", "#사이드컷"],
    "두피케어": ["#두피케어", "#탈모케어", "#두피클리닉", "#두피관리", "#건강한머리카락"],
    "클리닉": ["#헤어클리닉", "#모발케어", "#손상모발", "#영양트리트먼트", "#딥클리닉"],
}

# 계절별 해시태그
SEASON_TAGS = {
    "봄": ["#봄헤어", "#봄스타일", "#봄염색", "#봄트렌드"],
    "여름": ["#여름헤어", "#여름스타일", "#습기잡기", "#청량한"],
    "가을": ["#가을헤어", "#가을염색", "#웜톤", "#쿨톤"],
    "겨울": ["#겨울헤어", "#겨울스타일", "#건조모발케어"],
    "사계절": [],
}

# 공통 해시태그
COMMON_TAGS = [
    "#헤어살롱", "#미용실", "#헤어디자이너", "#헤어스타일",
    "#뷰티", "#살롱", "#헤어", "#오늘의헤어",
]


class HashtagGenerator:
    """주제/시즌 기반 최적 해시태그 세트 생성"""

    def __init__(self, max_tags: int = 20):
        self.max_tags = max_tags

    def generate(self, topic: str, season: str = "", custom_tags: list = None) -> list[str]:
        tags = []

        # 시술 태그
        for key, service_tags in SERVICE_TAGS.items():
            if key in topic:
                tags.extend(service_tags)
                break

        # 시즌 태그
        if season in SEASON_TAGS:
            tags.extend(SEASON_TAGS[season])

        # 공통 태그
        tags.extend(COMMON_TAGS)

        # 커스텀 태그
        if custom_tags:
            tags.extend(custom_tags)

        # 중복 제거 + 최대 개수 제한
        seen = set()
        unique_tags = []
        for tag in tags:
            if tag not in seen:
                seen.add(tag)
                unique_tags.append(tag)

        return unique_tags[: self.max_tags]

    def format(self, tags: list[str]) -> str:
        """해시태그 문자열로 포매팅"""
        return " ".join(tags)
