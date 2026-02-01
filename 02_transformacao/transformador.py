import pandas as pd
import os

def transformar_dados():
    print("🧹 Iniciando a Missão 2: Limpeza e Validação...")
    
    caminho_entrada = "01_integracao_api/consolidado_despesas.csv"
    if not os.path.exists(caminho_entrada):
        print("❌ Erro: Arquivo consolidado não encontrado!")
        return

    # 1. LER OS DADOS
    df = pd.read_csv(caminho_entrada, sep=';', dtype={'CD_CONTA_CONTABIL': str}, low_memory=False)

    # 2. CONVERTER VALOR PARA NÚMERO (O CONSERTO!)
    print("🔢 Convertendo textos em números...")
    # Se o valor vier como "100,50", trocamos a vírgula por ponto e avisamos que é número
    df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].astype(str).str.replace(',', '.')
    df['VL_SALDO_FINAL'] = pd.to_numeric(df['VL_SALDO_FINAL'], errors='coerce').fillna(0)

    # 3. FILTRAR POR EVENTOS/SINISTROS (CONTA 411)
    print("🔍 Filtrando despesas assistenciais (Sinistros)...")
    df = df[df['CD_CONTA_CONTABIL'].str.startswith('411', na=False)]

    # 4. REMOVER ZERADOS E NEGATIVOS (Agora funciona!)
    df = df[df['VL_SALDO_FINAL'] > 0]
    
    # 5. AJUSTAR DATAS E COLUNAS
    print("📅 Organizando datas e colunas...")
    df_final = df.rename(columns={
        'REG_ANS': 'RegistroANS',
        'VL_SALDO_FINAL': 'ValorDespesas'
    })

    df_final['DATA'] = pd.to_datetime(df_final['DATA'])
    df_final['Ano'] = df_final['DATA'].dt.year
    # Criando o nome do trimestre baseado no mês
    df_final['Trimestre'] = df_final['DATA'].dt.month.map({1: '1T', 4: '2T', 7: '3T', 10: '4T'})

    # 6. SALVANDO
    os.makedirs("02_transformacao", exist_ok=True)
    caminho_saida = "02_transformacao/despesas_limpas.csv"
    df_final.to_csv(caminho_saida, index=False, sep=';', encoding='utf-8')
    
    print(f"✅ Missão 2 concluída! Arquivo gerado: {caminho_saida}")
    print(f"📊 Foram filtradas {len(df_final)} linhas de despesas assistenciais.")

if __name__ == "__main__":
    transformar_dados()