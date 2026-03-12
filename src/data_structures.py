"""
Módulo responsável pelas estruturas de dados usadas no projeto.

Requisito do Projeto: Persistência com Estruturas de Dados
Para demonstrar o conhecimento, vamos criar classes que encapsulam
as estruturas nativas do Python, justificando o porquê de cada uma.

1. Dicionários (Tabelas Hash Nativa)
    - Justificativa: Acesso O(1) por chave. Excelente para buscar
      os dados climáticos de uma cidade específica pelo nome.
2. Listas (Vetores)
    - Justificativa: Acesso sequencial e ordenado. Excelente para 
      armazenar o histórico de previsões de uma cidade ao longo dos dias.
"""

class DicionarioCidades:
    """Encapsula um dicionário para busca rápida de cidades."""
    
    def __init__(self):
        # O dicionário mapeia o nome da cidade para os dados dela
        self.dados = {}
    
    def inserir(self, nome_cidade, dados_previsao):
        """Insere ou atualiza os dados de uma cidade."""
        self.dados[nome_cidade] = dados_previsao
        
    def buscar(self, nome_cidade):
        """Busca os dados de uma cidade em tempo O(1)."""
        return self.dados.get(nome_cidade)
    
    def listar_todas(self):
        """Retorna uma lista com os nomes de todas as cidades cadastradas."""
        return list(self.dados.keys())

class ListaPrevisoes:
    """Encapsula uma lista para armazenar o histórico de temperaturas."""
    
    def __init__(self):
        # A lista armazenará dicionários com a temperatura de cada dia/hora
        self.previsoes = []
        
    def adicionar_previsao(self, dia, temperatura, descricao):
        """Adiciona uma nova medição no fim da lista (O(1) amortizado)."""
        self.previsoes.append({
            "dia": dia,
            "temperatura": temperatura,
            "descricao": descricao
        })
        
    def obter_todas(self):
        """Retorna a lista completa de ordenação temporal."""
        return self.previsoes
    
    def esta_vazia(self):
        return len(self.previsoes) == 0
