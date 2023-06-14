FROM node:latest
ENV PORT=8080 
WORKDIR /app
COPY index.js /app/
EXPOSE 3030/tcp
EXPOSE 3030/udp
USER 1001
CMD ["node", "index.js"]

