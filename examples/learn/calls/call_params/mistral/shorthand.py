from mirascope.core import mistral


@mistral.call("mistral-large-latest", call_params={"max_tokens": 512})
def recommend_book(genre: str) -> str:
    return f"Recommend a {genre} book"


print(recommend_book("fantasy"))
