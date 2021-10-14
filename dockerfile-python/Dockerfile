FROM python:3.8
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
WORKDIR /usr/src/app
COPY . .
CMD ["python3"]
ENTRYPOINT ["python3"]
