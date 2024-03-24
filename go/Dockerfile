#build stage
FROM golang:alpine AS builder
RUN apk add --no-cache git
WORKDIR /go/src/app
COPY . .

#final stage
FROM alpine:latest
RUN apk --no-cache add ca-certificates
ENTRYPOINT /app
LABEL Name=dockerapptemplate Version=0.0.1
EXPOSE 3000
