FROM python:3.11.3-slim-buster  
EXPOSE 5000


WORKDIR /api

# copy requirements.txt to workdir
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy source code and move inside
COPY . .
WORKDIR /api/app


CMD ["flask", "run", "--host=0.0.0.0"]
