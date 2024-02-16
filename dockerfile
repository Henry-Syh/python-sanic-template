FROM 192.168.0.137:9002/python/python-with-poetry:latest as builder
WORKDIR $PYSETUP_PATH

COPY pyproject.toml Makefile $PYSETUP_PATH
RUN make

COPY app /project/app
# COPY docs /project/docs
COPY config.toml /project/

WORKDIR /project

EXPOSE 8001
CMD sanic \
		app.app \
		--host=0.0.0.0 \
		--port=8001 \
		--fast
