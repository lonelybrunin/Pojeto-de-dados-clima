"""
Módulo responsável por formatar e gravar saída de dados.
Cumpre a Etapa 4: Entrega de Valor (Relatório Estruturado).
"""

from .data_processor import DataProcessor

class ReportGenerator:
    @staticmethod
    def gerar_relatorio_txt(dicionario_cidades, caminho_arquivo="relatorio_clima.txt"):
        """Gera um relatório descritivo simples e o salva em formato TXT."""
        
        cidades = dicionario_cidades.listar_todas()
        
        if not cidades:
            print("Nenhuma cidade para gerar relatório.")
            return
            
        with open(caminho_arquivo, "w", encoding="utf-8") as file:
            file.write("====================================================\n")
            file.write("    RELATÓRIO CLIMÁTICO (Previsão 5 Dias)           \n")
            file.write("====================================================\n\n")
            
            # 1. Ranking de cidades por média de temperatura
            file.write("--- 1. RANKING DAS CIDADES (Mais quente para mais fria) ---\n")
            ranking = DataProcessor.ordenar_cidades_por_temperatura(dicionario_cidades)
            for idx, c in enumerate(ranking, 1):
                file.write(f"{idx}. {c['cidade']} - Média: {c['media']}°C\n")
            file.write("\n")
            
            # 2. Resumo Detalhado por Cidade 
            file.write("--- 2. DETALHES POR CIDADE ---\n")
            for cidade in cidades:
                file.write(f"\n>> Cidade: {cidade.upper()} <<\n")
                
                lista_previsoes = dicionario_cidades.buscar(cidade)
                stats = DataProcessor.calcular_estatisticas_basicas(lista_previsoes)
                
                file.write(f"  * Média Geral: {stats['media']}°C\n")
                file.write(f"  * Máxima Prevista: {stats['maxima']}°C\n")
                file.write(f"  * Mínima Prevista: {stats['minima']}°C\n")
                
                # Aproveitando Filtragem / Agrupamento por Dia
                dias_agrupados = DataProcessor.agrupar_por_dia(lista_previsoes)
                file.write(f"  * Previsão por dia:\n")
                for dia, temps in dias_agrupados.items():
                    media_dia = round(sum(temps)/len(temps), 2)
                    file.write(f"      - {dia}: Média de {media_dia}°C\n")
                    
            file.write("\n====================================================\n")
            file.write("            Relatório gerado com sucesso!             \n")
            file.write("====================================================\n")
            
        print(f"Relatório exportado com sucesso para: {caminho_arquivo}")
        
    @staticmethod
    def gerar_relatorio_csv(dicionario_cidades, caminho_arquivo="relatorio_clima.csv"):
        """Opcional: Exportar os mesmos dados brutos para Excel/DS."""
        import csv
        
        cidades = dicionario_cidades.listar_todas()
        
        with open(caminho_arquivo, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Cidade", "Data", "Temperatura", "Descricao"])
            
            for cidade in cidades:
                lista = dicionario_cidades.buscar(cidade)
                for item in lista.obter_todas():
                    writer.writerow([cidade, item["dia"], item["temperatura"], item["descricao"]])
                    
        print(f"Dados exportados com sucesso para: {caminho_arquivo}")
