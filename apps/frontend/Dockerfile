FROM node:22-alpine

WORKDIR /app

COPY . /app
RUN npm install

ENTRYPOINT [ "npm", "run", "dev", "--", "--host" ]