FROM prefect:3-latest

WORKDIR /app

COPY ./ /app

RUN pip install .
RUN pip install simple_salesforce

ENV PYTHONPATH=/app/src:$PYTHONPATH