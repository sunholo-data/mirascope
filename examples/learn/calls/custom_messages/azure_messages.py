from azure.ai.inference.models import UserMessage
from mirascope.core import azure


@azure.call("gpt-4o-mini")
def recommend_book(genre: str) -> azure.AzureDynamicConfig:
    return {"messages": [UserMessage(content=f"Recommend a {genre} book")]}


print(recommend_book("fantasy"))
