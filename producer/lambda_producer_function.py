import json
import os

import requests
import boto3

# Configurações da API
latitude = -23.5062
longitude = -47.4559
TOMORROW_API_KEY = os.getenv("TOMORROW_API_KEY")
BASE_URL = "https://api.tomorrow.io"

url = f"{BASE_URL}/v4/weather/realtime?location={latitude},{longitude}&apikey={TOMORROW_API_KEY}"
headers = {"accept": "application/json"}

# Configurações do Kinesis
STREAM_NAME = "broker"
REGION = "us-east-1"

# Cliente do Kinesis
kinesis_client = boto3.client("kinesis", region_name=REGION)


def lambda_handler(event, context):
    # Faz a requisição à API
    response = requests.get(url, headers=headers)
    weather_data = response.json()
    # Verifica se a resposta contém dados válidos
    if "data" not in weather_data or not weather_data["data"]:
        return {
            "statusCode": 500,
            "body": json.dumps("Erro ao obter dados do tempo"),
        }
    else:
        # Envia os dados para o Kinesis
        kinesis_client.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(weather_data),
            PartitionKey="partition_key",
        )

        return {
            "statusCode": 200,
            "body": json.dumps("Dados enviados ao Kinesis com sucesso"),
        }
