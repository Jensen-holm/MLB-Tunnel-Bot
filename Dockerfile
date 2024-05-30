FROM python:3.9

# environment variables
ARG CONSUMER_KEY
ARG CONSUMER_SECRET
ARG ACCESS_TOKEN
ARG ACCESS_TOKEN_SECRET
ARG CLIENT_ID
ARG CLIENT_SECRET
ARG BEARER_TOKEN

ENV CONSUMER_KEY=$CONSUMER_KEY
ENV CONSUMER_SECRET=$CONSUMER_SECRET
ENV ACCESS_TOKEN=$ACCESS_TOKEN
ENV ACCESS_TOKEN_SECRET=$ACCESS_TOKEN_SECRET
ENV CLIENT_ID=$CLIENT_ID
ENV CLIENT_SECRET=$CLIENT_SECRET
ENV BEARER_TOKEN=$BEARER_TOKEN

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt . 

RUN pip install pip==21.1.1

RUN pip install numpy==1.26.4

RUN pip install lap==0.4.0

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
