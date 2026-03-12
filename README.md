# 🌦️ App de Previsão Climática (Estrutura de Dados em Python)

Projeto final para a disciplina de **Estrutura de Dados Aplicada ao Mundo Real**.
Este projeto consome dados da [OpenWeatherMap API](https://openweathermap.org/api), armazena em estruturas de dados específicas (Dicionários Hash e Listas Dinâmicas), processa esses dados para extrair estatísticas (médias, máximas, mínimas, e ordenação) e gera um relatório estruturado em formato texto e CSV.

---

## 🚀 Como Executar o Projeto

### 1. Pré-Requisitos
Certifique-se de ter o [Python](https://www.python.org/downloads/) (versão 3.6 ou superior) instalado em sua máquina. Opcionalmente, crie um ambiente virtual (venv).

### 2. Instalação das Dependências
O projeto utiliza a biblioteca `requests` para consumir a API. Instale-a via terminal:
```bash
pip install requests
```

### 3. Rodando o Script
O ponto de entrada do projeto é o aquivo `main.py`. Execute:
```bash
python main.py
```

### 4. Chave da API (API Key)
Ao rodar o projeto pela primeira vez, ele solicitará uma **API Key** do OpenWeatherMap.
* **Não tem uma chave?** Crie uma conta gratuita em [OpenWeatherMap Sign Up](https://home.openweathermap.org/users/sign_up), vá na aba "My API Keys", copie a chave gerada e cole no terminal quando solicitado. *(Obs: Novas chaves podem levar até 10 minutos para serem ativadas pelo serviço).*

---

## 🧠 Arquitetura e Estruturas de Dados Escolhidas

Conforme exigido pelos requisitos, este projeto foca na escolha consciente das **Estruturas de Dados**. A documentação das nossas escolhas se encontra nos arquivos fonte (ver `src/data_structures.py`), mas aqui está o resumo:

### 1. Dicionários (Tabela Hash Nativa)
* **Classe:** `DicionarioCidades`
* **Por que?** O Dicionário em Python é suportado nativamente por uma Tabela Hash. Escolhemos essa estrutura para armazenar as cidades processadas porque ela permite uma busca em complexidade de tempo **O(1)**. Se quisermos saber instantaneamente a previsão do Rio de Janeiro, basta acessar a chave `dicionario["Rio de Janeiro"]` sem precisar iterar/percorrer outras cidades da lista.

### 2. Listas (Vetor Dinâmico)
* **Classe:** `ListaPrevisoes`
* **Por que?** A API climática retorna previsões temporais em série (por exemplo, de 3 em 3 horas pelos próximos 5 dias). Para armazenar isso, criamos uma abstração em cima das Listas (Vetores). Vetores permitem acesso rápido e sequencial na memória e são ideais para quando precisamos percorrer todos os itens do dia para calcular médias de temperatura ou filtrar picos máximos e mínimos.

---

## 🔄 Diagrama de Fluxo e Estruturas

> Um dos requisitos do projeto é apresentar o fluxo e diagrama de estruturas. Aqui está o mapa visual de como os dados transitam no nosso software, da *API* até a *Entrega de Valor*:

```mermaid
graph TD;
    A[OpenWeatherMap API] -->|Requisicao GET HTTP via 'requests'| B(api_client.py)
    B -->|Retorna JSON bruto| C{data_structures.py}
    
    C -->|Instancia| D[ListaPrevisoes]
    D -->|O(1) Append| E[Armazena Historico de Dias e Horas]
    E -->|Associa a Chave| F[DicionarioCidades]
    
    F -->|Indexa| G((Tabela Hash: 'Sao Paulo' -> ListaPrevisoes\n 'Rio' -> ListaPrevisoes ...))
    
    G -. Busca Rápida O(1) .-> H[data_processor.py]
    
    H -->|Algoritmo 1| I[Agrupar por Dia]
    H -->|Algoritmo 2| J[Estatisticas Basicas (Média, Max, Min)]
    H -->|Algoritmo 3| K[Ordencao (Cidades mais quentes via Timsort)]
    
    I --> L[report_generator.py]
    J --> L
    K --> L
    
    L -->|Entrega de Valor| M[(relatorio_clima.txt e .csv)]
```

---

## 🛠️ Entregas e Funcionalidades Implementadas

* **Consumo de API Real**: Tratamento de erros de conexão (códigos 401 e 404) e lógica de tentativas (Retry Logic) embutidos no cliente.
* **Manipulação de Dados**:
    * Busca instantânea por cidade.
    * Ordenamento do objeto em memória para geração do "Ranking de Cidades Quentes".
    * Agrupamento temporal com quebras de data.
* **Entrega Concreta de Valor**: O final do processamento não apenas joga prints no terminal, mas cria artefatos concretos (`.csv` voltado a dados e `.txt` voltado à leitura humana).

*(Fim do Arquivo)*
