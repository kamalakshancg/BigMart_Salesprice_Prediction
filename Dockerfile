FROM python
RUN python3 install pip
RUN pip install flask
RUN pip install -r requirements.txt
COPY . /admin
WORKDIR /admin
EXPOSE 4000
CMD ["python","app.py"]