# 4. Contextlib Context Managers

## Why this is Python-specific
`contextlib.contextmanager` lets you build `with`-compatible lifecycle behavior from a small generator-style function.

## Source
- [feature_04_contextlib_magic.py](../../src/csharp_to_python_learning/python_only_features/feature_04_contextlib_magic.py)

## Run
```bash
uv run src/csharp_to_python_learning/python_only_features/feature_04_contextlib_magic.py
```

## Expected output
- `start:deploy`
- `inside`
- `end:deploy`
