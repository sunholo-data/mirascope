from mirascope.core import mistral
from tenacity import retry, stop_after_attempt, wait_exponential


@mistral.call("mistral-large-latest", stream=True)
def recommend_book(genre: str) -> str:
    return f"Recommend a {genre} book"


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
)
def stream():
    for chunk, _ in recommend_book("fantasy"):
        print(chunk.content, end="", flush=True)


stream()
