FROM node:14

WORKDIR /frontend

COPY ./package.json /frontend/package.json
RUN npm install

COPY . /frontend

CMD ["node", "app.js"]
