FROM python:3.6.5-alpine

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./as-set-to-prefixes.py" ]
