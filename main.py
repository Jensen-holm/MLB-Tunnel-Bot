#
# MLB Tunnel Bot
# Author: Jensen Holm
# April / May 2024
#

import MLBTunnelBot
import datetime


def main(_retries: int = 5) -> None:
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    try:
        _ = MLBTunnelBot.write(yesterday=yesterday)
        print(f"{datetime.datetime.now()} => Success !!")
    except Exception:
        if _retries:
            main(_retries=_retries - 1)


if __name__ == "__main__":
    main()
