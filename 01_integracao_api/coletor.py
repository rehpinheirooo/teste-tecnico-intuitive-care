import pandas as pd
import requests
import zipfile
import io
import os

# --- CONFIGURAÇÕES ATUALIZADAS (O MAPA NOVO) ---
URL_BASE = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"

# Agora usamos o que você descobriu no site!
CAMINHOS_TESTE = [
    "2025/1T2025.zip",
    "2025/2T2025.zip",
    "2025/3T2025.zip"
]
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

def baixar_e_limpar():
    lista_de_tabelas = []
    
    print("🕵️ Investigando os arquivos no servidor da ANS...")

    for caminho in CAMINHOS_TESTE:
        url_completa = f"{URL_BASE}{caminho}"
        print(f"🔗 Tentando acessar: {url_completa}")
        
        try:
            # O 'stream=True' ajuda a não travar a memória com arquivos grandes
            resposta = requests.get(url_completa, headers=HEADERS, timeout=30, stream=True)
            
            if resposta.status_code == 200:
                print(f"✅ Arquivo encontrado! Baixando...")
                
                with zipfile.ZipFile(io.BytesIO(resposta.content)) as meu_zip:
                    arquivos_no_zip = meu_zip.namelist()
                    print(f"   📂 Arquivos encontrados dentro do ZIP: {arquivos_no_zip}")
                    
                    for nome_arquivo in arquivos_no_zip:
                        # Vamos aceitar arquivos que terminem em .csv e ignorar maiúsculas/minúsculas
                        if nome_arquivo.lower().endswith('.csv'):
                            print(f"   🎯 Lendo arquivo: {nome_arquivo}")
                            with meu_zip.open(nome_arquivo) as f:
                                # Usamos low_memory=False para evitar avisos bobos do Python
                                df = pd.read_csv(f, sep=';', encoding='latin-1', low_memory=False)
                                df.columns = [c.upper().strip() for c in df.columns]
                                df['FONTE_ARQUIVO'] = caminho
                                lista_de_tabelas.append(df)
            else:
                print(f"   ❌ Não encontrado (Erro {resposta.status_code}). Tentando o próximo...")
                
        except Exception as e:
            print(f"   💥 Erro técnico: {e}")

    if lista_de_tabelas:
        print("\n🧹 Iniciando limpeza e consolidação...")
        df_final = pd.concat(lista_de_tabelas, ignore_index=True)
        
        # Filtro: O teste pede apenas Despesas com Eventos/Sinistros
        # Geralmente na ANS isso é identificado pela conta contábil ou nome da conta
        # Aqui vamos salvar o bruto primeiro para você ver se funcionou
        
        os.makedirs("01_integracao_api", exist_ok=True)
        caminho_csv = "01_integracao_api/consolidado_despesas.csv"
        df_final.to_csv(caminho_csv, index=False, sep=';', encoding='utf-8')
        
        print(f"✨ SUCESSO! O arquivo foi gerado em: {caminho_csv}")
        print(f"📊 Total de linhas processadas: {len(df_final)}")
    else:
        print("\n⚠️ ALERTA: O site da ANS pode estar fora do ar ou mudou os links novamente.")
        print("💡 Dica: Tente abrir este link no seu navegador para ver se o arquivo baixa manualmente:")
        print(f"{URL_BASE}2024/1T/1T2024.zip")

if __name__ == "__main__":
    baixar_e_limpar()