FROM python:3.6

ARG MY_KEY
ENV MY_KEY=$MY_KEY

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

CMD ["app.py"]