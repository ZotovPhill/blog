FROM node:lts-alpine as build-stage

RUN mkdir -p /usr/src/frontend
WORKDIR /usr/src/frontend

COPY ./frontend/package*.json ./
RUN npm install

COPY ./frontend/ /usr/src/frontend

RUN npm run build

#========== NGINX =============#

FROM nginx:alpine

WORKDIR /usr/src/system/

RUN mkdir -p certs
COPY ./system/02-nginx/certs/nginx.key ./certs
COPY ./system/02-nginx/certs/nginx.crt ./certs

COPY --from=build-stage /usr/src/frontend/dist /usr/share/nginx/html

RUN rm /etc/nginx/nginx.conf
COPY ./system/03-node/frontend.conf /etc/nginx/nginx.conf

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
