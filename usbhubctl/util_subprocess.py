import logging
import pathlib
import subprocess
import time

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent

logger = logging.getLogger(__file__)


def subprocess_run(args: list[str]) -> str:
    begin_s = time.monotonic()
    proc = subprocess.run(
        args,
        check=False,
        capture_output=True,
        text=True,
        cwd=str(DIRECTORY_OF_THIS_FILE),
    )

    logger.info(
        f"{args}: returncode={proc.returncode}, duration={time.monotonic()-begin_s:0.3f}s"
    )
    logger.debug(f"  stdout: {proc.stdout}")
    logger.debug(f"  stderr: {proc.stderr}")

    if proc.returncode != 0:
        logger.warning(f"{args}: Failed: returncode={proc.returncode}: {proc.stderr}")
        raise ValueError(f"{args}: {proc.stderr}")

    return proc.stdout
