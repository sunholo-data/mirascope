from mirascope.core import anthropic


@anthropic.call("claude-3-5-sonnet-20240620", response_model=list[str])
def extract_book(texts: list[str]) -> str:
    return f"Extract book titles from {texts}"


book = extract_book(
    [
        "The Name of the Wind by Patrick Rothfuss",
        "Mistborn: The Final Empire by Brandon Sanderson",
    ]
)
print(book)
# Output: ["The Name of the Wind", "Mistborn: The Final Empire"]
