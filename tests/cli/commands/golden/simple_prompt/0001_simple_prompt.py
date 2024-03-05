"""A prompt for recommending movies of a particular genre."""

from mirascope import BasePrompt

prev_revision_id = None
revision_id = "0001"


class MovieRecommendationPrompt(BasePrompt):
    """Please recommend a list of movies in the {genre} category."""

    genre: str
