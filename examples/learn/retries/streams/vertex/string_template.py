from mirascope.core import vertex, prompt_template
from tenacity import retry, stop_after_attempt, wait_exponential


@vertex.call("gemini-1.5-flash", stream=True)
@prompt_template("Recommend a {genre} book")
def recommend_book(genre: str): ...


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
)
def stream():
    for chunk, _ in recommend_book("fantasy"):
        print(chunk.content, end="", flush=True)


stream()
