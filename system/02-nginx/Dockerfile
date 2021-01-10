FROM nginx:1.19.0-alpine

RUN apk add --update --no-cache nginx

WORKDIR /usr/src/system/

COPY ./system/wait-for.sh .
RUN chmod +x ./wait-for.sh

RUN mkdir certs
COPY ./system/02-nginx/certs/nginx.key ./certs
COPY ./system/02-nginx/certs/nginx.crt ./certs

RUN rm /etc/nginx/conf.d/default.conf
COPY ./system/02-nginx/nginx.conf /etc/nginx/conf.d/default.conf
