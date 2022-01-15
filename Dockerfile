FROM python:3.7-buster
COPY . /admin
WORKDIR /admin
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python","app.py"]
