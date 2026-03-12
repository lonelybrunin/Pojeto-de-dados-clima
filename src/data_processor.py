"""
Módulo reponsável por analisar os dados climáticos.
Cumpre a Etapa 3 do projeto: Manipulação de Dados.
Opera sobre as estruturas criadas no módulo data_structures.
"""

from .data_structures import ListaPrevisoes

class DataProcessor:

    @staticmethod
    def agrupar_por_dia(lista_previsoes):
        """
        Recebe uma ListaPrevisoes e retorna um dicionário (chave=dia, valor=Lista de temperaturas do dia)
        Demonstra a operação obrigatória: Agrupamento.
        """
        previsoes_brutas = lista_previsoes.obter_todas()
        dias_agrupados = {}
        
        for item in previsoes_brutas:
            # item["dia"] -> formato '2023-10-31 15:00:00'
            data_apenas = item["dia"].split(" ")[0]
            temperatura = item["temperatura"]
            
            if data_apenas not in dias_agrupados:
                dias_agrupados[data_apenas] = []
                
            dias_agrupados[data_apenas].append(temperatura)
            
        return dias_agrupados
        
    @staticmethod
    def calcular_estatisticas_basicas(lista_previsoes):
        """
        Calcula a Média, Mínima e Máxima temperatura de todos os dias.
        Demonstra Análises Avançadas (Identificação Mín/Max e Média).
        """
        previsoes = lista_previsoes.obter_todas()
        
        if not previsoes:
            return {"media": 0, "maxima": 0, "minima": 0}
            
        temperaturas = [item["temperatura"] for item in previsoes]
        
        media = sum(temperaturas) / len(temperaturas)
        maxima = max(temperaturas)
        minima = min(temperaturas)
        
        return {
            "media": round(media, 2),
            "maxima": maxima,
            "minima": minima
        }

    @staticmethod
    def ordenar_cidades_por_temperatura(dicionario_cidades):
        """
        Recebe o DicionarioCidades, calcula a média de cada uma, 
        e retorna uma lista ordenada (da mais quente para mais fria).
        Demonstra: Ordenação.
        """
        cidades_nomes = dicionario_cidades.listar_todas()
        medias_cidades = []
        
        for nome in cidades_nomes:
            lista_previsoes = dicionario_cidades.buscar(nome) # Busca O(1)
            stats = DataProcessor.calcular_estatisticas_basicas(lista_previsoes)
            
            medias_cidades.append({
                "cidade": nome, 
                "media": stats["media"]
            })
            
        # Ordenação descendente (do mais quente pro mais frio) usando lambda Timsort
        medias_cidades.sort(key=lambda x: x["media"], reverse=True)
        return medias_cidades

