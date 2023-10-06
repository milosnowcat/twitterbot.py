import requests

URL = "https://api.quotable.io/random?tags=technology"

def get_quote():
    """
    The function `get_quote` sends a GET request to a specified URL, retrieves JSON data, extracts a
    quote and its author from the data, and returns them as a tuple.
    :return: a quote and its author.
    """
    response = requests.get(URL)
    data = response.json()
    quote = data["content"]
    author = data["author"]
    return quote, author