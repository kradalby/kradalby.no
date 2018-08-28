FROM node:7 as lessbuilder
WORKDIR /app

RUN npm install -g less

ADD theme2/static/css css
ADD theme2/static/less less
RUN lessc -x less/style.less style.min.css

FROM python:3.7.0 as builder
WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .
COPY --from=lessbuilder /app/style.min.css /app/theme2/static/css
RUN make html



FROM nginx:alpine 
COPY --from=builder /app/output /usr/share/nginx/html
