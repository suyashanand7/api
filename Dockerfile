FROM python:3.6-alpine

WORKDIR /app

COPY . /app

RUN pip install -r req.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]

