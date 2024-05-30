#
# MLB Tunnel Bot
# Author: Jensen Holm
# April / May 2024
#

import MLBTunnelBot
import datetime
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main() -> None:
    next_iter_start_time = time.time() + (24 * 60 * 60)
    yesterday = datetime.date.today() - datetime.timedelta(days=1)

    try:
        # tweet = MLBTunnelBot.write(yesterday=yesterday)
        # logging.info(f"Successful write for {yesterday}\n{tweet}")

        MLBTunnelBot._overlay_pitch_video(video_directory="./videos1/")

    except Exception as e:
        logging.error(f"Error for {yesterday} due to exception: {e.__class__} -> {e}")

    finally:
    # time.sleep(next_iter_start_time - time.time())
        return


if __name__ == "__main__":
    # while True:
    main()
