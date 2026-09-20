#!/bin/bash

mkdir -p ruff/report-ruff
ruff check --output-format json > ruff/ruff.json || ruff_exit=$?
ciqar -r ruff:ruff/ruff.json -s src -o ruff/report-ruff
ruff check --output-format=github --output-file=ruff/ruff.md
script -q ruff/report-ruff/output.txt -c "ruff check"
cat ruff/report-ruff/output.txt | ansi2html > ruff/report-ruff/index.html
exit $ruff_exit