FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /api
WORKDIR /api
COPY requirements.txt /api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /api
EXPOSE 5000
CMD [ "python", "code/api.py"]
