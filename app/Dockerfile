FROM python:3.11

LABEL maintainer="Eric Wang <gowest.wang@gmail.com>"

COPY ./app /opt/app
WORKDIR /opt/app
RUN yes | pip install -r requirements.txt
ENV PYTHONPATH=/opt/app

EXPOSE 8088/tcp
EXPOSE 8088/udp

CMD ["gunicorn", "--bind", "0.0.0.0:8088", "__init__:app"]