dev_setup:
	pipenv install --dev

static_analysis:
	pipenv run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	pipenv run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	pipenv run mypy --strict .
	pipenv run black --check .

auto_format:
	pipenv run black .

test:
	pipenv run pytest