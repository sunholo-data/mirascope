from mirascope.core import BaseMessageParam, openai


@openai.call("gpt-4o-mini", call_params={"max_tokens": 512})
def recommend_book(genre: str) -> list[BaseMessageParam]:
    return [BaseMessageParam(role="user", content=f"Recommend a {genre} book")]


print(recommend_book("fantasy"))
