FROM node:latest

WORKDIR /usr/src/app

EXPOSE 5000

COPY package.json .

RUN npm install

COPY . .

CMD ["npm", "start"]
