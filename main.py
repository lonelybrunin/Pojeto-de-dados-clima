"""
Módulo Principal - Orquestração do Projeto.
Aqui combinamos as chamadas da API, armazenamento e geração do Relatório.
"""

import sys
import os
from src.api_client import WeatherAPIClient
from src.data_structures import DicionarioCidades
from src.report_generator import ReportGenerator

# Define as cidades alvo para a pesquisa
CIDADES_ALVO = ["Belo Horizonte"]

def carregar_chave_api():
    """
    Retorna uma chave Mock para não bloquear o terminal com inputs.
    """
    return "MOCKED_KEY"

def main():
    print("Iniciando processamento de dados climáticos...\n")
    
    # 1. Configurar Cliente da API
    api_key = carregar_chave_api()
    if not api_key:
        print("Erro: Chave de API não informada encerrando programa.")
        sys.exit(1)
        
    client = WeatherAPIClient(api_key)
    
    # 2. Instanciar nossa Estrutura Principal de Pesquisa Rápida (Dicionário Hash)
    cidades_clima_db = DicionarioCidades()
    
    # 3. Consumir a API para cada cidade e persistir na Estrutura de Dados
    print("------------------------------------------")
    for cidade in CIDADES_ALVO:
        print(f"Buscando previsão para {cidade}...")
        lista_dados = client.buscar_previsao_cidade(cidade)
        
        if lista_dados and not lista_dados.esta_vazia():
            # Inserção no dicionário (Busca O(1) futura)
            cidades_clima_db.inserir(cidade, lista_dados)
        else:
            print(f" -> Cuidado: Omitindo {cidade} por falta de dados.")
    print("------------------------------------------\n")

    # Verifica se pelo menos uma cidade teve successo
    if not cidades_clima_db.listar_todas():
        print("Erro Crítico: Falha ao obter dados para todas as cidades.")
        sys.exit(1)
        
    # 4. Geração dos Relatórios (Consumindo Dados via DataProcessor)
    print("Processamento finalizado. Gerando relatórios...\n")
    
    ReportGenerator.gerar_relatorio_txt(cidades_clima_db, "relatorio_clima.txt")
    ReportGenerator.gerar_relatorio_csv(cidades_clima_db, "relatorio_clima.csv")
    
    print("\nProcesso concluído com sucesso!")

if __name__ == "__main__":
    main()
