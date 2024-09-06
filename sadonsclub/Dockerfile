FROM python:3.11-slim

WORKDIR /usr/src/sadonsclub

RUN apt-get update && apt-get install -y netcat-openbsd

ENV PYTHONBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN sed -i 's/\r$//g' /usr/src/sadonsclub/entrypoint.sh
RUN chmod +x /usr/src/sadonsclub/entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]