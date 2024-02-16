PYPI_URL := "http://192.168.0.137:8990/"
PYPI_USER := "test"
PYPI_PW := "iampass"

# 賦值 POETRY 變數
POETRY := $(shell which poetry)
POETRY_HOME := $(HOME)/.poetry

# 如果 POETRY 未定義，安裝 poetry
ifndef POETRY

$(warning "POETRY is not defined.")

.PHONY: pre_init
pre_init: install_poetry init
	@echo "---------------------finish project init------------------------"

.PHONY: install_poetry
install_poetry:
	@echo "install poetry start."
	@echo "---------------------install poetry------------------------"
	@curl -sSL https://install.python-poetry.org | POETRY_HOME=$(POETRY_HOME) python3 -
	@echo "-----------------------------------------------------------"

	@$(eval POETRY := $(POETRY_HOME)/bin/poetry)
	
	@echo "POETRY: $(POETRY)"
	@echo "POETRY_HOME: $(POETRY_HOME)"
	@echo "POETRY is installed"

else

$(info "POETRY is defined.")

.PHONY: pre_init
pre_init: init
	@echo "---------------------finish project init------------------------"

endif

.PHONY: init
init:
	@echo "---------------------start project init------------------------"
	
	@$(POETRY) --version
	@$(POETRY) config virtualenvs.in-project true
	@$(POETRY) config http-basic.myPYPI ${PYPI_USER} ${PYPI_PW}

	@$(POETRY) env use python3
	@$(POETRY) source add --priority=explicit myPYPI ${PYPI_URL}
	@$(POETRY) add --source myPYPI myUtility
	@$(POETRY) install --no-root --no-cache --no-interaction -vvv

.PHONY: docker_build
docker_build: poetry_set
# CICD使用
	poetry env use python3
	poetry install --no-root --no-cache --no-interaction

.PHONY: docker_test
docker_test:
	# sudo docker build -t api_test . --no-cache
	sudo docker build -t api_test .
	sudo docker compose up -d

.PHONY: docker_end
docker_end:
	sudo docker compose down -v

.PHONY: clean
clean:
	@-deactivate

	-find . -type f -name *.pyc -delete
	-find . -type d -name log -delete
	-find . -type d -name __pycache__ -delete
	-find . -type d -name utilities -exec rm -rv {} +

	@-rm -rf .venv
	@-rm -r poetry.lock
