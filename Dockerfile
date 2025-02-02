FROM mcr.microsoft.com/playwright:focal

RUN apt-get update && apt-get install -y python3-pip
COPY . .
RUN pip3 install gevent
RUN pip3 install Flask
RUN pip3 install TikTokApi
RUN python -m playwright install

CMD ["python3", "app.py"]
