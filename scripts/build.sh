#!/bin/bash

# https://packaging.python.org/en/latest/specifications/version-specifiers/
# https://hatch.pypa.io/latest/version/
# https://semver.org

pre=
if [ -n "${pre}" ]; then
    pre=a${pre}
fi

post=
if [ -n "${post}" ]; then
    post=.post${post}
fi

dev=
if [ -n "${dev}" ]; then
    dev=.dev${dev}
fi

buildId=
if [ -z "${buildId}" ]; then
    buildId=${USER}.${NAME}
fi

branch=
if [ -z "${branch}" ]; then
    branch=$(git rev-parse --abbrev-ref HEAD)
fi

commit=
if [ -z "${commit}" ]; then
    commit=$(git rev-parse HEAD)
fi

local=+${buildId}.${branch}.${commit}

date=$(date +%Y%m%d%H%M%S)
sed -i -E "s/version = \"(.*\..*\..*)\"/version = \"\1.${date}${pre}${post}${dev}${local}\"/" pyproject.toml

pip freeze > constraints.txt
sed -i "s/constraints.txt//" .gitignore
pip install build
python -m build

git restore .gitignore pyproject.toml || true
