"""
social_post_builder.py
콘텐츠 + 해시태그를 조합하여 완성된 SNS 포스트를 만듭니다.
"""

from datetime import datetime
from .hashtag_generator import HashtagGenerator


class SocialPostBuilder:
    """인스타그램/SNS용 완성 포스트 빌더"""

    def __init__(self, salon_name: str = "살롱"):
        self.salon_name = salon_name
        self.hashtag_gen = HashtagGenerator(max_tags=20)

    def build_single(self, post_data: dict) -> dict:
        """단일 포스트 완성본 생성"""
        tags = self.hashtag_gen.generate(
            topic=post_data.get("topic", ""),
            season=post_data.get("season", ""),
        )

        caption = (
            f"{post_data['hook']}\n\n"
            f"{post_data['body']}\n\n"
            f"{post_data['cta']}\n\n"
            f"{'─' * 20}\n"
            f"{self.hashtag_gen.format(tags)}"
        )

        return {
            **post_data,
            "hashtags": tags,
            "caption": caption,
            "char_count": len(caption),
            "platform": "instagram",
        }

    def build(self, posts: list[dict]) -> list[dict]:
        """포스트 목록 일괄 완성"""
        return [self.build_single(p) for p in posts]

    def to_markdown(self, posts: list[dict]) -> str:
        """완성된 포스트를 Markdown 형식으로 출력"""
        lines = [
            "# SNS 포스트 예시",
            f"\n> 생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"> 총 {len(posts)}개 포스트\n",
            "---\n",
        ]

        for i, post in enumerate(posts, 1):
            lines += [
                f"## 포스트 {i}: {post.get('topic', '')} ({post.get('season', '')})",
                f"- 타겟: {post.get('target', '전체')}",
                f"- 글자수: {post.get('char_count', 0)}자\n",
                "**캡션:**\n",
                f"```\n{post['caption']}\n```\n",
                "---\n",
            ]

        return "\n".join(lines)
