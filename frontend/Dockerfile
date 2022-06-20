FROM node:lts-alpine

WORKDIR /usr/src/frontend
COPY . .

RUN apk update && apk upgrade && yarn --ignore-engines
CMD yarn start