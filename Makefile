dev_setup:
	pipenv install --dev

static_analysis:
	pipenv run mypy --strict .
	pipenv run black --check .

auto_format:
	pipenv run black .

test:
	pipenv run pytest