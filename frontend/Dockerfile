FROM node:latest as build 

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json ./

RUN npm ci

COPY ./ ./ 

RUN npm run build



FROM nginx:stable-alpine as prod

COPY --from=build /app/build