"""
Módulo responsável por consumir a API de dados climáticos reais.
Cumpre a etapa 1: Consumo de Dados via API.
"""

import requests
import time
from .data_structures import ListaPrevisoes

class WeatherAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        # Usaremos o endpoint da previsão de 5 dias/3 horas
        self.base_url = "https://api.openweathermap.org/data/2.5/forecast"

    def buscar_previsao_cidade(self, nome_cidade, num_tentativas=3):
        """
        Busca a previsão do tempo para uma cidade, retornando
        uma instância da nossa classe ListaPrevisoes.
        Tem logica de retry em caso de erro na requisicao.
        """
        if self.api_key == "MOCKED_KEY":
            return self._gerar_dados_mock(nome_cidade)

        params = {
            "q": nome_cidade,
            "appid": self.api_key,
            "units": "metric", # Temperaturas em Celsius
            "lang": "pt_br"     # Descrições em Português
        }
        
        tentativa_atual = 1
        
        while tentativa_atual <= num_tentativas:
            try:
                response = requests.get(self.base_url, params=params, timeout=10)
                
                # Trata erros ou ausência de dados
                if response.status_code == 401:
                    print(f"Erro [API]: Chave de API inválida! ({self.api_key})")
                    return None
                    
                if response.status_code == 404:
                    print(f"Erro [API]: Cidade '{nome_cidade}' não encontrada.")
                    return None
                    
                response.raise_for_status() # Lança erro para status 5xx
                
                # Se tudo OK, converte os dados JSON para a nossa Estrutura de Lista
                dados_json = response.json()
                lista_hist = ListaPrevisoes()
                
                for item in dados_json.get("list", []):
                    dt_txt = item.get("dt_txt")
                    temp = item.get("main", {}).get("temp")
                    desc = item.get("weather", [{}])[0].get("description", "Sem info")
                    
                    lista_hist.adicionar_previsao(dt_txt, temp, desc)
                
                return lista_hist

            except requests.exceptions.RequestException as e:
                print(f"Erro [Conexão] ao buscar '{nome_cidade}': {e}. Tentativa {tentativa_atual}/{num_tentativas}")
                time.sleep(2) # Espera antes do retry
                tentativa_atual += 1
                
        print(f"Erro [API]: Falha ao buscar dados para '{nome_cidade}' após {num_tentativas} tentativas.")
        return None

    def _gerar_dados_mock(self, nome_cidade):
        """Metodo Oculto para popular dados fakes na ListaPrevisoes, evitando a exigencia de API Key."""
        from datetime import datetime, timedelta
        import random
        
        lista_hist = ListaPrevisoes()
        base_date = datetime.now()
        temps_base = [19.0, 21.5, 25.0, 27.5, 28.0, 26.0, 22.0, 20.0]
        descricoes = ["Ensolarado", "Parcialmente nublado", "Céu limpo", "Chuva leve"]
        
        for dia in range(5):
            for i, t in enumerate(temps_base):
                dt = base_date + timedelta(days=dia, hours=i*3)
                dt_str = dt.strftime("%Y-%m-%d %H:%M:00")
                temp_final = round(t + random.uniform(-2.0, 2.0), 2)
                desc = random.choice(descricoes)
                lista_hist.adicionar_previsao(dt_str, temp_final, desc)
                
        print(f" -> Retornando dados simulados (Mock) para {nome_cidade}...")
        return lista_hist
