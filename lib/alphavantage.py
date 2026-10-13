import os

from dotenv import load_dotenv  # pip install python-dotenv


# Load environment variables from .env file
#
def get_api_credentials():
    # Access the credentials
    load_dotenv()
    api_key = os.getenv("ALPHA_API_KEY")
    if not api_key:
        raise ValueError("ALPHA_API_KEY environment variable not set.")

    return api_key
