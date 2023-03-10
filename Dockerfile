FROM python-3.8.5-alpine

ENV PYTHONBUFFERED=1

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
