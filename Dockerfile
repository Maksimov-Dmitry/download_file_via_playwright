FROM mcr.microsoft.com/playwright:v1.15.0-focal as base
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

FROM base as tests
CMD ["pytest", "./tests/"]

FROM base as prod
CMD [ "python", "./src/main.py" ]