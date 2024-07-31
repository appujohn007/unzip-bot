FROM ubuntu:latest

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3-pip zstd p7zip-full p7zip-rar gcc git ffmpeg && \
    python3 -m venv /venv && \
    apt-get clean
ENV PATH="/venv/bin:$PATH"
RUN pip3 install -U pip setuptools wheel && \
    mkdir /app
WORKDIR /app
RUN pip3 install -U -r needs.txt
COPY .env /app/.env
CMD ["/bin/bash", "start.sh"]
