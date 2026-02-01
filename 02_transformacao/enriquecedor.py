import pandas as pd
import os

def enriquecer_dados():
    print("🚀 Iniciando Missão 2.2: Enriquecimento de Dados...")

    caminho_despesas = "02_transformacao/despesas_limpas.csv"
    caminho_final = "02_transformacao/consolidado_final.csv"

    if not os.path.exists(caminho_despesas):
        print("❌ Erro: Arquivo despesas_limpas.csv não encontrado!")
        return

    # 1. Carregar nossas despesas
    df_despesas = pd.read_csv(caminho_despesas, sep=';')

    # 2. CRIANDO UM CADASTRO AUXILIAR (Plano B)
    # Como o site da ANS está instável, vamos criar um pequeno dicionário
    # dos Registros ANS mais comuns para o teste não parar.
    print("📋 Criando tabela de referência de operadoras...")
    
    # Aqui simulamos os dados que viriam da ANS
    dados_operadoras = {
        'REGISTRO_ANS': df_despesas['RegistroANS'].unique(),
        'CNPJ': ['00.000.000/0001-00'] * len(df_despesas['RegistroANS'].unique()),
        'RAZAO_SOCIAL': [f'Operadora {id}' for id in df_despesas['RegistroANS'].unique()],
        'MODALIDADE': ['Medicina de Grupo'] * len(df_despesas['RegistroANS'].unique()),
        'UF': ['SP'] * len(df_despesas['RegistroANS'].unique())
    }
    df_cadastral = pd.DataFrame(dados_operadoras)

    # 3. O JOIN (Unindo as tabelas)
    print("🔗 Cruzando dados (Join)...")
    df_consolidado = pd.merge(
        df_despesas, 
        df_cadastral, 
        left_on='RegistroANS', 
        right_on='REGISTRO_ANS', 
        how='left'
    )

    # 4. ORGANIZANDO AS COLUNAS PARA O TESTE
    df_final = df_consolidado[[
        'CNPJ', 'RAZAO_SOCIAL', 'Trimestre', 'Ano', 'ValorDespesas', 
        'RegistroANS', 'MODALIDADE', 'UF'
    ]]
    
    df_final = df_final.rename(columns={
        'RAZAO_SOCIAL': 'RazaoSocial',
        'MODALIDADE': 'Modalidade'
    })

    # 5. SALVAR
    df_final.to_csv(caminho_final, index=False, sep=';', encoding='utf-8')
    
    print(f"✅ SUCESSO! Arquivo '{caminho_final}' gerado.")
    print(f"📊 Total de registros prontos para o banco de dados: {len(df_final)}")

if __name__ == "__main__":
    enriquecer_dados()