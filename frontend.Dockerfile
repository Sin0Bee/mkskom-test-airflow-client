# этап сборки (build stage)
FROM node:lts-alpine as build-stage
WORKDIR /frontend
COPY . /frontend
RUN npm install
RUN npm run build

# этап production (production-stage)
FROM nginx:stable-alpine as production-stage
WORKDIR /frontend/.nginx
COPY --from=build-stage ./frontend/dist /usr/share/nginx/html
COPY --from=build-stage ./frontend/.nginx/nginx.conf /etc/nginx/sites-enabled/default
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]