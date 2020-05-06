FROM gliderlabs/alpine:3.4

ADD fetch_ip_info.py /

COPY . /opt/fetch_ip_info
WORKDIR /opt/fetch_ip_info

RUN \
apk add --update \
py-pip \
&& pip install --upgrade pip \
&& pip install requests && pip install fire

CMD [ "python", "fetch_ip_info.py" ]
