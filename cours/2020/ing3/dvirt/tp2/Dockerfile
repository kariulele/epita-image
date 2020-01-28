FROM golang:alpine
WORKDIR /usr/src/app
COPY resources .
RUN go build -v
EXPOSE 80
CMD ./myapp
