"""
This script checks for new episodes on Fridays after midnight using the Bitsearch API.
If new episodes are found, it sends a notification to the user using the notifier module.

"""

import asyncio

import bitsearch
import notifier


def check_new_episodes(search_query):
    """
    Check for new episodes on Fridays after midnight and send a notification if new episodes found.
    :param search_query: The search query to use for finding new episodes.
    """

    # Episodes typically air on Fridays, but allow searching any day
    if True:
        # Search for new episodes on Bitsearch
        new_episodes = list(bitsearch.search_episodes(search_query))
        # Check if there are new episodes
        if new_episodes:
            for i, episode in enumerate(new_episodes):
                print(f"{i + 1}. {episode['title']}")
            while True:
                try:
                    selection = int(
                        input("Enter the number of the episode you want to watch: "))
                    if 1 <= selection <= len(new_episodes):
                        selected_episode = new_episodes[selection-1]
                        break
                    print("Invalid selection. Please enter a number between 1 and", len(
                        new_episodes))
                except ValueError:
                    print("Invalid selection. Please enter a number")
            asyncio.run(notifier.send_telegram_notification(selected_episode))
            print("New episodes found! Notification sent.")
        else:
            print("No new episodes found.")


if __name__ == "__main__":
    while True:
        query = input("Enter the search query: ")
        if query.lower() in ["exit", "q", "quit", "stop", "end"]:
            break
        check_new_episodes(search_query=query)
