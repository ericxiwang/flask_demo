FROM python:3.11

LABEL maintainer="Eric Wang <gowest.wang@gmail.com>"

COPY ./app /opt/app
WORKDIR /opt
RUN yes | pip install -r /opt/app/requirements.txt
ENV PYTHONPATH=/opt/app

EXPOSE 8088/tcp
EXPOSE 8088/udp

CMD ["gunicorn", "--bind", "0.0.0.0:8088", "app.__init__:create_app()"]