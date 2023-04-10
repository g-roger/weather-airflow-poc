# Extração de dados climáticos (airflow)

Este é um fluxo de trabalho em Airflow para extrair dados meteorológicos da cidade de São Paulo usando a API da Visual Crossing.

## Fluxo de trabalho

1. O fluxo de trabalho começa com a criação de uma pasta para armazenar os dados extraídos.
2. A extração de dados é realizada pela execução de uma função em Python que usa a API da Visual Crossing para obter dados meteorológicos para a cidade de São Paulo para a semana que termina na data especificada.
Os dados extraídos são salvos em arquivos CSV separados por categoria de dados.

## Como executar

1. Para executar este fluxo de trabalho, você precisa configurar o ambiente de execução do Airflow e garantir que as dependências estejam instaladas. Em seguida, salve o código em um arquivo .py e coloque-o em uma pasta em que o Airflow possa acessá-lo (dentro de /dags).
2. Em seguida, inicie o servidor web do Airflow e ative o fluxo de trabalho na interface do usuário do Airflow. O fluxo de trabalho será executado automaticamente no intervalo especificado e os dados serão extraídos e salvos em arquivos CSV na pasta especificada.
      - export AIRFLOW_HOME=~/Documents/weather-airflow-poc
      - aiflow standalone (Para execução do airflow)
      
