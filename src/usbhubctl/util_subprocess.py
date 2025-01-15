import logging
import os
import pathlib
import shutil
import subprocess
import time

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent

logger = logging.getLogger(__file__)


def subprocess_run(args: list[str], timeout_s: float = 10.0) -> str:
    args_text = " ".join(args)

    begin_s = time.monotonic()
    proc = subprocess.run(
        args,
        check=False,
        capture_output=True,
        text=True,
        cwd=str(DIRECTORY_OF_THIS_FILE),
        timeout=timeout_s,
    )

    logger.debug(f"EXEC {args_text}")
    logger.debug(f"  returncode={proc.returncode}")
    logger.debug(f"  duration={time.monotonic()-begin_s:0.3f}s")
    logger.debug(f"  stdout: {proc.stdout}")
    logger.debug(f"  stderr: {proc.stderr}")

    if proc.returncode != 0:
        logger.warning(f"{args_text}: Failed: returncode={proc.returncode}")
        logger.warning(f"STDERR: {proc.stderr}")
        logger.warning(f"STDOUT: {proc.stdout}")
        raise ValueError(
            f"{args_text}:\n\nstderr: {proc.stderr}\n\nstdout: {proc.stdout}"
        )

    return proc.stdout
