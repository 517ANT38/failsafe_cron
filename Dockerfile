
FROM python:3.12 as builder

COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.12-slim

ENV PATH=/root/.local:$PATH
ENV DATA_FOLDER=/data
ENV LOG_FOLDER=/var/log

WORKDIR /failsafe_cron
COPY --from=builder /root/.local /root/.local
COPY app app
COPY main.py .
COPY --chmod=0755 scripts/create_cmd.sh .

RUN apt-get update && apt-get -y install cron
RUN mkfifo --mode 0666 /var/log/cron.log
RUN mkdir /data

CMD  ./create_cmd.sh && cron && tail -f /var/log/cron.log
