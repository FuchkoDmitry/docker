FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt  

EXPOSE 5000

CMD gunicorn -b 0.0.0.0:5000 stocks_products.wsgi
