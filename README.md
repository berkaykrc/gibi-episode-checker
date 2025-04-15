# gibi-episode-checker

This project is a Python script that searches for new episodes on Bitsearch every Friday after midnight and notifies the user. It consists of the following files:

- `src/main.py`: This file is the entry point of the script. It contains the main logic to search for new episodes on Bitsearch every Friday after midnight. It uses the `bitsearch.py` module to perform the search and the `notifier.py` module to send notifications.

- `src/bitsearch.py`: This file contains a function `search_episodes` that performs the search on Bitsearch. It takes the necessary parameters such as the search query and returns a list of new episodes found.

- `src/notifier.py`: This file contains a function `send_notification` that sends a notification to the user. It takes the necessary parameters such as the episode details and uses a notification service (e.g., email, push notification) to notify the user.

- `tests/test_bitsearch.py`: This file contains unit tests for the `bitsearch.py` module. It tests the `search_episodes` function to ensure it returns the expected results.

- `tests/test_notifier.py`: This file contains unit tests for the `notifier.py` module. It tests the `send_notification` function to ensure it sends the notification correctly.

- `.gitignore`: This file specifies which files and directories should be ignored by version control (e.g., temporary files, dependencies).

- `requirements.txt`: This file lists the dependencies required by the project. You can use this file to install the necessary packages using a package manager like pip.

Please refer to the individual files for more information on their implementation.

## Setup

To set up the project, follow these steps:

1. Clone the repository.

2. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

3. Configure the notification service in the `notifier.py` file. Replace the placeholder code with the actual code to send notifications using your preferred service.

4. Run the script `main.py` to start searching for new episodes on Bitsearch every Friday after midnight.

Feel free to customize the project according to your needs. Happy coding!