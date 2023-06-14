FROM nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
WORKDIR /www/data
COPY index.html /www/data
WORKDIR /tmp/logs
EXPOSE 8080

