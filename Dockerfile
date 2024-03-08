FROM python:3.12 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt
FROM python:3.12-slim
WORKDIR /code
COPY --from=builder /root/.local /root/.local
COPY ./1.py .
ENV PATH=/root/.local:$PATH
CMD [ "python", "-u", "./1.py" ]
