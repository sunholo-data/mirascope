"""Prompt for determining coolness."""
from pydantic import BaseModel

from mirascope import messages

from .trace_prompt import TracePrompt


class Coolness(BaseModel):
    """Coolness rating out of 10."""

    coolness: int


@messages
class CoolnessPrompt(TracePrompt):
    """
    SYSTEM: You determine coolness on a scale of 1 to 10. If the person's name is Brian,
    they get an automatic 10 out of 10, otherwise, they get a random whole number
    between 1 and 9.

    USER: How cool is {person}?
    """

    person: str
