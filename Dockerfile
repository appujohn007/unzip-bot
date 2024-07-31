FROM python:3.11 

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3-pip zstd p7zip-full gcc git ffmpeg wget && \
    wget https://www.7-zip.org/a/7z2107-linux-x64.tar.xz && \
    tar -xf 7z2107-linux-x64.tar.xz && \
    mv 7zz /usr/bin/7zz && \
    python3 -m venv /venv && \
    apt-get clean

ENV PATH="/venv/bin:$PATH"

RUN pip3 install -U pip setuptools wheel && \
    mkdir /app

WORKDIR /app

RUN pip3 install -U -r needs.txt

COPY .env /app/.env

CMD ["/bin/bash", "start.sh"]
