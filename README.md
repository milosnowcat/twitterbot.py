# twitterbot.py
 Twitter Bot

## Installation of the TwitterBot.py Project

This project allows you to post random technology-related quotes on Twitter using a Twitter bot. To get started with this project, follow the installation steps below.

### Prerequisites

Before using the project, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. Clone the GitHub repository containing the TwitterBot.py project to your local machine using the following command:

   ```bash
   git clone https://github.com/milosnowcat/twitterbot.py.git
   ```

2. Navigate to the `twitterbot.py` directory:

   ```bash
   cd twitterbot.py
   ```

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your Twitter API credentials as follows:

   ```plaintext
   Api_Key=YOUR_API_KEY
   Api_Secret=YOUR_API_SECRET
   Access_Token=YOUR_ACCESS_TOKEN
   Access_Token_Secret=YOUR_ACCESS_TOKEN_SECRET
   ```

   Replace `YOUR_API_KEY`, `YOUR_API_SECRET`, `YOUR_ACCESS_TOKEN`, and `YOUR_ACCESS_TOKEN_SECRET` with your actual Twitter API credentials.

5. Run the `main.py` script to start the Twitter bot:

   ```bash
   python main.py
   ```

6. The script will retrieve a random technology-related quote using the Quotable API and post it as a tweet on your Twitter account.

7. To stop the script, press `Ctrl + C` in your terminal.

That's it! You have successfully installed and used the TwitterBot.py project to post random technology-related quotes on Twitter using your Twitter bot.

---

## Using the TwitterBot.py Project

The TwitterBot.py project allows you to post random technology-related quotes on Twitter using a Twitter bot. Follow these steps to use the project.

### Setting up Twitter API Credentials

1. Ensure you have followed the installation steps mentioned in the "Installation of the TwitterBot.py Project" section.

2. Create a `.env` file in the project directory and add your Twitter API credentials as shown in the installation steps.

### Running the Twitter Bot

1. Run the `main.py` script to start the Twitter bot:

   ```bash
   python main.py
   ```

2. The script will retrieve a random technology-related quote from the Quotable API and post it as a tweet on your Twitter account.

3. The tweet will include the quote and its author in the format: "quote ~ author."

4. To stop the script, press `Ctrl + C` in your terminal.

That's it! You have successfully used the TwitterBot.py project to post random technology-related quotes on Twitter using your Twitter bot and API credentials.
