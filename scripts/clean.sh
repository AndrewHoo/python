#!/bin/bash
rm -rf .pytest_cache dist constraints.txt pytest .coverage html ruff .ruff_cache
find . -path ./.venv -prune -o -name '__pycache__' -exec rm -rf {} +;
