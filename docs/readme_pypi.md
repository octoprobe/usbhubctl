Based on: https://github.com/tiangolo/fastapi/blob/master/.github/workflows/publish.yml

## Prepare

```python
pip install build twine
```

## Test

```python
python -m build
twine upload dist/* -r pypitest
pip install --index-url https://test.pypi.org/simple/ usbhubctl
```

## Upload

```python
python -m build
twine upload dist/* --repository uhubctl-r pypi
```