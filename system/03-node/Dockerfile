FROM node:lts-alpine as build-stage
WORKDIR /usr/src/frontend
COPY ./frontend/package*.json ./
RUN npm install
COPY ./frontend/ .
EXPOSE 8080
RUN npm run build