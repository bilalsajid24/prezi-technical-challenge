FROM node:19

WORKDIR /app

COPY package.json .

COPY package-lock.json .

RUN npm install

EXPOSE 3000

CMD ["npm", "run", "dev"]
