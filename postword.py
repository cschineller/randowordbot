import logging
from config import create_api
from randowords import generate
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def postWord(api):
    logger.info("Generating random word")
    tweet = generate()
    api.update_status(tweet)
def main():
    api = create_api()
    while True:
        postWord(api)
        logger.info("Waiting...")
        time.sleep(600)

if __name__ == "__main__":
    main()