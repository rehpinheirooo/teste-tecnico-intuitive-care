# Desafio Técnico - Intuitive Care
**Candidato:** Renato Pinheiro

## 🛠️ Tecnologias Utilizadas
- **Python 3.14**: Processamento e limpeza de dados.
- **Pandas**: Manipulação de grandes volumes de dados (2M+ linhas).
- **Requests**: Integração com servidor FTP da ANS.
- **SQL**: Estruturação de banco de dados.

## 🚀 Como executar o projeto
1. Instale as dependências: `pip install pandas requests`
2. Execute o coletor: `python 01_integracao_api/coletor.py`
3. Execute o transformador: `python 02_transformacao/transformador.py`
4. Execute o enriquecedor: `python 02_transformacao/enriquecedor.py`
5. Execute o agregador: `python 02_transformacao/agregador.py`

## 🧠 Decisões Técnicas (Trade-offs)
- **Resiliência:** O script de coleta foi adaptado para identificar a estrutura de pastas da ANS de 2025, tratando erros 404 e instabilidades de conexão.
- **Performance:** Utilizei o Pandas para consolidar mais de 2 milhões de registros em menos de 1 minuto, aplicando filtros de contas contábeis (Grupo 411 - Sinistros) para reduzir o ruído nos dados.
- **Qualidade:** Implementei sanitização de tipos (conversão de vírgula para ponto e preenchimento de zeros em CNPJ) para garantir que a carga no banco de dados seja limpa.

## 📈 Resultados obtidos
- Total bruto processado: ~2.113.000 linhas.
- Total após limpeza e filtro assistencial: 113.288 linhas.
- Operadoras analisadas: 712 empresas.
