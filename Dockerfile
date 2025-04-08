FROM python:3.8.5-alpine3.12

WORKDIR /usr/src/app

RUN apk add --no-cache curl gcc musl-dev libffi-dev

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]
