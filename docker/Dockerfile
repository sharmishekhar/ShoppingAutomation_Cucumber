FROM mcr.microsoft.com/playwright/python:v1.44.0

WORKDIR /tests

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest", "-n", "4"]