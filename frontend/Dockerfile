FROM node:16
WORKDIR /app
COPY package*.json ./
RUN npm install -g vite
RUN npm install
RUN chmod +x node_modules/.bin/*
COPY . .
EXPOSE 5001
CMD ["vite"]