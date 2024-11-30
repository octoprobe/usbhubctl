import logging
import os
import pathlib
import shutil
import subprocess
import time

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent

logger = logging.getLogger(__file__)


def assert_root_and_s_bit(program: str) -> pathlib.Path:
    """
    Assert the file belongs to root.
    Assert that the setuid bit is set.
    """
    filename = pathlib.Path(shutil.which(program))

    assert filename.is_file(), f"{filename} does not exist or is not a file!"

    file_stat = os.stat(filename)
    # Check if the file is owned by root (UID 0)
    belongs_to_root = file_stat.st_uid == 0
    # Check if the setuid bit is set (0o4000)
    has_setuid_bit_set = file_stat.st_mode & 0o4000

    success = has_setuid_bit_set and belongs_to_root
    if success:
        return filename

    raise subprocess.SubprocessError(
        f"{filename} must be owned by root and have the setuid bit set! Call:\nsudo chown root:root {filename}\nsudo chmod a+s {filename}"
    )


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
