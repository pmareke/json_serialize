.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: test-good
test-good: ## Run good tests
	poetry run pytest --approvaltests-use-reporter='PythonNative' tests/test_deployment_good.py

.PHONY: test-bad
test-bad: ## Run good bad
	poetry run pytest --approvaltests-use-reporter='PythonNative' tests/test_deployment_bad.py

.PHONE: test
test: test-good test-bad ## Run all tests
