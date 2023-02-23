FROM python:3.8.9-buster
MAINTAINER GeoNode development team

RUN mkdir -p /usr/src/mad_geonode3

# Enable postgresql-client-11.2
RUN apt-get install -y ca-certificates 
RUN wget --no-check-certificate --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
# RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list
RUN chmod 1777 /tmp
# RUN mount | grep /tmp

# This section is borrowed from the official Django image but adds GDAL and others
RUN apt-get update && apt-get install -y \
        gcc \
        zip \
        gettext \
        postgresql-client-11 libpq-dev \
        sqlite3 spatialite-bin libsqlite3-mod-spatialite \
                python3-gdal python3-psycopg2 python3-ldap \
                python3-pil python3-lxml python3-pylibmc \
                python3-dev libgdal-dev \
                libxml2 libxml2-dev libxslt1-dev zlib1g-dev libjpeg-dev \
                libmemcached-dev libsasl2-dev \
                libldap2-dev libsasl2-dev \
                uwsgi uwsgi-plugin-python3 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*


# RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8B48AD6246925553
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7638D0442B90D010
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CBF8D6FD518E17E1
RUN apt-get update && apt-get install -y geoip-bin

# add bower and grunt command
COPY . /usr/src/mad_geonode3/
WORKDIR /usr/src/mad_geonode3

RUN apt-get update && apt-get -y install cron
COPY monitoring-cron /etc/cron.d/monitoring-cron
RUN chmod 0644 /etc/cron.d/monitoring-cron
RUN crontab /etc/cron.d/monitoring-cron
RUN touch /var/log/cron.log
RUN service cron start

COPY wait-for-databases.sh /usr/bin/wait-for-databases
RUN chmod +x /usr/bin/wait-for-databases
RUN chmod +x /usr/src/mad_geonode3/tasks.py \
    && chmod +x /usr/src/mad_geonode3/entrypoint.sh

# Install pip packages
RUN pip install pip==20.1.1 \
    && pip install --upgrade --no-cache-dir --src /usr/src -r requirements.txt \
    && pip install pygdal==$(gdal-config --version).* \
    && pip install flower==0.9.4

RUN pip install --upgrade -e .

# Install "geonode-contribs" apps
RUN cd /usr/src; git clone https://github.com/GeoNode/geonode-contribs.git -b master
# Install logstash and centralized dashboard dependencies
RUN cd /usr/src/geonode-contribs/geonode-logstash; pip install --upgrade -e . \
	cd /usr/src/geonode-contribs/ldap; pip install --upgrade -e .

ENTRYPOINT service cron restart && /usr/src/mad_geonode3/entrypoint.sh
