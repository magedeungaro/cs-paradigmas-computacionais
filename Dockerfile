FROM python:3.9.17-slim

WORKDIR /app

RUN pip install matplotlib
RUN pip install numpy
RUN pip install pandas