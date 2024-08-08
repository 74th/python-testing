import asyncio
import time
from logging import getLogger, DEBUG, root, StreamHandler, Formatter
from typing import Coroutine

handler = StreamHandler()
handler.setFormatter(Formatter("%(asctime)s: %(message)s"))
root.addHandler(handler)
root.setLevel(DEBUG)

logger = getLogger(__name__)


def main():
    logger.info("start program")

    asyncio.run(run())

    logger.info("end program")


async def run() -> list[int]:
    tasks: list[Coroutine] = []
    for i in range(100):
        tasks.append(run_task(i))

    return await asyncio.gather(*tasks)


async def run_task(no: int) -> int:
    loop = asyncio.get_event_loop()

    logger.info(" start %d", no)

    def sleep():
        logger.info(" sleep start %d", no)
        time.sleep(0.5)
        logger.info(" sleep end %d", no)

    # None にしても、default の ThreadPoolExecutor で実行される
    # ただし、このThreadPoolExecutor は32+コア数っぽい
    await loop.run_in_executor(None, sleep)
    logger.info(" end %d", no)

    return no


if __name__ == "__main__":
    main()
