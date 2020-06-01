FROM python:3.8-alpine
LABEL maintainer="Ary Kleinerman"
RUN apk update && apk upgrade && \
    apk add --virtual .build-deps --no-cache gcc musl-dev make file libffi-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir Flask && \
    pip install --no-cache-dir gevent
RUN apk del .build-deps && \
    rm -rf /var/cache/apk/* /root/.cache /tmp/*
COPY hello.py /app/hello.py
COPY tests.py /app/tests.py
WORKDIR /app
EXPOSE 8080
CMD ["python", "./hello.py"]
