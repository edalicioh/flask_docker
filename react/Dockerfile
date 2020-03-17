FROM node:12.2.0-alpine

MAINTAINER Edalicio Hazen "edalicio@outlook.com"

WORKDIR /usr/src/app

ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY ./package.json /usr/src/app/package.json
RUN npm install react-scripts -g --silent
RUN chown -R node:node . && chmod -R 755 .
USER node
RUN npm install --silent
RUN npm cache clean --force

CMD ["npm", "run", "start"]