set -euox pipefail

# python -m pytest -m 'not live' tests

python -m pytest --cov --cov-report=lcov:lcov.info --cov-report=term -m 'not live' tests ${@}
