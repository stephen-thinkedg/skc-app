FROM skcthinkedg/skc-zesty:latest

MAINTAINER Stephen K Conklin <stephen@thinkedg.com>

RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip3 install Flask==0.11.1 redis==2.10.5

RUN useradd -ms /bin/bash admin
USER admin

WORKDIR /app


CMD ["python3", "app.py"] 
