# pythonコードのリント
.PHONY: ruff-check
ruff-check:
	ruff check --fix $(path)

# pythonコードのフォーマット
.PHONY: ruff-format
ruff-format:
	ruff format $(path)

# pythonコードのフォーマットとリント
.PHONY: ruff
ruff:
	@make ruff-check path=$(path)
	@make ruff-format path=$(path)


.PHONY: mypy
mypy:
	mypy --strict $(path)

.PHONY: check
check:
	@make ruff path=$(path)
	@make mypy path=$(path)
