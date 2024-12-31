FROM i5sbx7ps.mirror.aliyuncs.com/library/python:3.10-bullseye

RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|http://mirrors.aliyun.com/ubuntu/|g' /etc/apt/sources.list

RUN apt update && apt install -y portaudio19-dev libgl1-mesa-glx
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD uwsgi --ini uwsgi.ini

COPY . /app
WORKDIR /app

RUN python3 manage.py collectstatic --noinput
