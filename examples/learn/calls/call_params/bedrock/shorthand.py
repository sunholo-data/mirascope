from mirascope.core import bedrock


@bedrock.call(
    "anthropic.claude-3-haiku-20240307-v1:0",
    call_params={"inferenceConfig": {"maxTokens": 512}},
)
def recommend_book(genre: str) -> str:
    return f"Recommend a {genre} book"


response = recommend_book("fantasy")
print(response.content)
