FROM nginx:alpine

WORKDIR /usr/src/system/

RUN mkdir -p certs
COPY ./system/02-nginx/certs/nginx.key ./certs
COPY ./system/02-nginx/certs/nginx.crt ./certs

RUN rm /etc/nginx/conf.d/default.conf
COPY ./system/02-nginx/backend.conf /etc/nginx/conf.d/default.conf
