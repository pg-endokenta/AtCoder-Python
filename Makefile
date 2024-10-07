# pythonコードのリント
.PHONY: ruff-check
ruff-check:
	ruff check --fix .

# pythonコードのフォーマット
.PHONY: ruff-format
ruff-format:
	ruff format .

# pythonコードのフォーマットとリント
.PHONY: ruff
ruff:
	@make ruff-check
	@make ruff-format