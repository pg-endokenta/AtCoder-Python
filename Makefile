# pythonコードのリント
.PHONY: ruff-check
ruff-check:
	uvx ruff check --fix $(path)

# pythonコードのフォーマット
.PHONY: ruff-format
ruff-format:
	uvx ruff format $(path)

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

make fmt:
	uvx ruff check --fix
	uvx ruff format