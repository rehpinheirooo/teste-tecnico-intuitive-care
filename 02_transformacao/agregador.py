import pandas as pd
import os

def calcular_estatisticas():
    print("📊 Iniciando Missão 3: Cálculos Estatísticos...")

    caminho_entrada = "02_transformacao/consolidado_final.csv"
    if not os.path.exists(caminho_entrada):
        print("❌ Erro: Arquivo consolidado_final.csv não encontrado!")
        return

    # 1. Carregar os dados
    df = pd.read_csv(caminho_entrada, sep=';')

    # 2. Agrupar por Operadora e calcular Média e Desvio Padrão
    # O "groupby" é como se você separasse as notas fiscais por "pilhas" de cada empresa
    print("🧮 Calculando médias e variações por operadora...")
    
    resumo = df.groupby(['RegistroANS', 'RazaoSocial']).agg({
        'ValorDespesas': ['mean', 'std', 'count']
    }).reset_index()

    # Ajustar os nomes das colunas para ficarem bonitos
    resumo.columns = ['RegistroANS', 'RazaoSocial', 'Media_Despesas', 'Desvio_Padrao', 'Qtd_Registros']

    # 3. Tratar valores nulos (Se só tem 1 registro, o desvio padrão é zero)
    resumo['Desvio_Padrao'] = resumo['Desvio_Padrao'].fillna(0)

    # 4. Salvar o arquivo final de análise
    caminho_saida = "02_transformacao/estatisticas_operadoras.csv"
    resumo.to_csv(caminho_saida, index=False, sep=';', encoding='utf-8')

    print(f"✅ Missão 3 concluída! Arquivo gerado: {caminho_saida}")
    print(f"📈 Calculamos dados de {len(resumo)} operadoras diferentes.")

if __name__ == "__main__":
    calcular_estatisticas()