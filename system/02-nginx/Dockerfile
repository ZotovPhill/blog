FROM nginx:1.19.0-alpine

RUN apk add --update --no-cache nginx

WORKDIR /usr/src/

COPY certs ./system
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
