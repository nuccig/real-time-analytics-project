# 🌐 Real-Time Analytics Project

## 📋 Descrição
Sistema de análise em tempo real de dados meteorológicos utilizando arquitetura serverless na AWS para coleta, processamento e alertas automatizados baseados em condições climáticas.

## 🚀 Tecnologias Utilizadas
- **AWS Lambda** - Processamento serverless
- **Amazon Kinesis** - Streaming de dados
- **Amazon SNS** - Sistema de notificações
- **AWS Glue** - ETL e catalogação
- **Tomorrow.io API** - Dados meteorológicos
- **Python 3.x** - Linguagem principal

## 📁 Estrutura do Projeto
```
├── producer/
│   ├── lambda_producer_function.py    # Lambda producer de dados
│   └── lambda_function_producer.zip   # Package deployado
├── consumer/
│   ├── consumer_realtime.py           # Consumer em tempo real
│   ├── consumer_batch.py              # Consumer em lote
│   └── consumer_etl_glue.py           # Consumer para ETL
└── LICENSE
```

## ⚡ Funcionalidades
### Producer (Coleta de Dados)
- **Integração com Tomorrow.io API** para dados meteorológicos
- **Localização configurável** (latitude/longitude)
- **Envio automático** para Kinesis Data Stream
- **Tratamento de erros** e validação de dados

### Consumer Real-Time
- **Processamento em tempo real** via Kinesis
- **Sistema de alertas** baseado em thresholds:
  - Probabilidade de precipitação > 10%
  - Velocidade do vento > 10 km/h
  - Rajadas de vento > 10 km/h
  - Intensidade da chuva > 10mm/h
- **Notificações via SNS** para alertas críticos

### Consumer Batch
- **Processamento em lote** para análises históricas
- **Agregações temporais** de dados meteorológicos
- **Persistência para data lake**

### Consumer ETL
- **Transformações de dados** com AWS Glue
- **Catalogação automática** no Data Catalog
- **Preparação para analytics**

## 🔧 Instalação e Execução
### Pré-requisitos
```bash
# Configurar credenciais AWS
aws configure

# Configurar variáveis de ambiente
export TOMORROW_API_KEY="your_api_key"
export PRECIPITATION_PROBABILITY="10"
export WIND_SPEED="10"
export WIND_GUST="10"
export RAIN_INTENSITY="10"
```

### Deploy do Producer
```bash
# Zipar função Lambda
zip lambda_function_producer.zip lambda_producer_function.py

# Deploy via AWS CLI ou Console
aws lambda create-function --function-name weather-producer
```

### Configuração do Consumer
```bash
# Criar tópico SNS
aws sns create-topic --name snsalerta

# Configurar trigger do Kinesis
aws lambda create-event-source-mapping --event-source-arn arn:aws:kinesis:region:account:stream/broker
```

## 🛠️ Arquitetura do Sistema

![image](https://github.com/user-attachments/assets/8659e4f2-c1fd-4536-96aa-6d4309f089b8)

### Fluxo de Dados
1. **Lambda Producer** coleta dados da API Tomorrow.io
2. **Kinesis Data Stream** recebe e distribui dados
3. **Lambda Consumers** processam dados em paralelo:
   - Real-time: Alertas imediatos
   - Batch: Processamento histórico
   - ETL: Transformações para analytics

### Configurações de Alerta
- **SNS Topic**: `snsalerta`
- **Kinesis Stream**: `broker`
- **Região**: `us-east-1`
- **Partition Key**: Baseada em localização

## 📊 Métricas Monitoradas
### Dados Coletados
- **Temperatura atual**
- **Probabilidade de precipitação**
- **Velocidade e direção do vento**
- **Intensidade da chuva**
- **Umidade relativa**
- **Pressão atmosférica**

### Thresholds de Alerta
Configuráveis via variáveis de ambiente para adaptação a diferentes cenários.

## 📦 Dependências Principais
- boto3 (AWS SDK)
- requests (HTTP client)
- json (data processing)

## 🎯 Casos de Uso
- **Alertas meteorológicos** para operações críticas
- **Monitoramento agrícola** automatizado
- **Gestão de frotas** baseada em condições climáticas
- **Análise de tendências** meteorológicas
- **Dashboard em tempo real** de condições climáticas

## 🔒 Segurança
- **IAM Roles** com permissões mínimas necessárias
- **API Keys** gerenciadas via AWS Secrets Manager
- **Encryption** em trânsito e repouso
- **VPC endpoints** para comunicação interna AWS
