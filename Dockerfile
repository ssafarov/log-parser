FROM python:3

RUN pip install python-csv geoip2 user-agents

RUN mkdir -p /app && mkdir -p /app/log
WORKDIR /app

ADD http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz /app
RUN gunzip ./GeoLite2-Country.mmdb.gz

COPY log/access.log /app/log/
COPY parser.py /app

CMD [ "python", "./parser.py" ]
