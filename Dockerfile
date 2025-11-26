# docker build -t test-docker .
# docker run test-docker

FROM python:3.12
WORKDIR /app
copy . .
CMD ["python", "main.py"]