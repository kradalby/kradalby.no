FROM python:3.7.0 as builder
WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .
RUN make html


FROM nginx:alpine 
COPY --from=builder /app/output /usr/share/nginx/html
