FROM python:3.8.2-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install gcc python3-dev musl-dev curl libffi-dev wget ca-certificates -y

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
Run apt-get install postgresql postgresql-contrib -y
RUN pip install --upgrade pip setuptools

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pillow

COPY example /usr/src/app/
COPY entrypoint.sh /usr/src/app

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
