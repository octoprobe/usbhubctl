set -euox pipefail

ruff check --config pyproject.toml --fix usbhubctl tests || true

python -m mypy --config-file pyproject.toml usbhubctl tests || true

python -m pylint usbhubctl tests || true
