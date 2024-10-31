# DataStreamETL

### Refactor code with black format

pip install pre-commit autoflake isort black

pre-commit install --config .pre-commit-config.yaml

autoflake -r . --in-place --remove-all-unused-imports --ignore-init-module-imports && isort . --profile black && black .

git config blame.ignoreRevsFile .git-blame-ignore-revs
