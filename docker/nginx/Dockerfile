ARG BASE_IMAGE_VERSION
FROM geonode/nginx:${BASE_IMAGE_VERSION}

WORKDIR /etc/nginx/

ADD nginx.conf.envsubst nginx.https.available.conf.envsubst ./
ADD geonode.conf.envsubst ./sites-enabled/

ADD docker-autoreload.sh docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
RUN chmod +x /docker-autoreload.sh
RUN chmod +x /docker-entrypoint.sh

CMD ["nginx", "-g", "daemon off;"]
