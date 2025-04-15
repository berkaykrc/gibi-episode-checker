"""
This module provides functions to search for new episodes on Bitsearch 
and notify the user if there are any.

Functions:
- search_episodes(search_query): Search for new episodes on Bitsearch.
- perform_bitsearch(search_query): Perform a search on Bitsearch for new episodes.
- notify_user(new_episodes): Notify the user about the new episodes.
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()

def search_episodes(search_query):
    """
    Search for new episodes on Bitsearch and notify the user if there are any.

    Args:
        search_query (str): The query to search for episodes.

    Returns:
        None
    """
    return perform_bitsearch(search_query)


def perform_bitsearch(search_query):
    """
    Perform a search on Bitsearch for new episodes.

    Args:
        search_query (str): The query to search for episodes.

    Returns:
        list: A list of new episodes found.
    """
    # Define the base URL and parameters for the API request
    base_url = os.getenv("BASE_URL") + "/search"
    params = {"site": "bitsearch",
              "query": search_query, "limit": 0, "page": 1}

    try:
        # Make the API request
        response = requests.get(base_url, params=params, timeout=55)
    except requests.exceptions.ReadTimeout:
        print("Error: Request timed out.")
        return []
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the new episodes and their magnet links
        new_episodes = [
            {"title": episode["name"], "magnet_link": episode["magnet"]}
            for episode in data["data"]
        ]

        return new_episodes
    print(f"Error: Received status code {response.status_code}")
    print(f"response from server", response.content)
    return []
