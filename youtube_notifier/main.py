import schedule
import time
import logging
from logging.handlers import RotatingFileHandler
from youtube_api import check_live_stream
from email_utils import send_email


def main():
    live_streams = check_live_stream()
    if live_streams:
        stream_title = live_streams[0]['snippet']['title']
        send_email('YouTube Live Stream Alert', f'{stream_title} is live now!')
    else:
        logging.info("No live streams detected or an error occurred.")


if __name__ == '__main__':
    handler = RotatingFileHandler(
        "yt-livestream-bot.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            handler,
            logging.StreamHandler()
        ]
    )

    schedule.every(90).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
