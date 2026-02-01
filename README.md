# Desafio Técnico - Cuidado Intuitivo

**Candidato:** Renato Pinheiro

Este projeto consiste em um pipeline de dados completo para captura, tratamento, enriquecimento e análise estatística dos dados de demonstrações contábeis de operadoras de saúde, utilizando a base de dados abertos da ANS.

## 🛠️ Tecnologias Utilizadas
- **Python 3.14**: Linguagem principal para processamento e limpeza.
- **Pandas**: Manipulação de grandes volumes de dados (2M+ linhas).
- **Requests**: Integração e captura de arquivos do servidor FTP da ANS.
- **SQL**: Estruturação de queries para modelagem de banco de dados.

## 🚀 Como executar o projeto
1. Instale as dependências: 
   ```bash
   pip install pandas requests
Execute o pipeline na ordem abaixo:

python 01_integracao_api/coletor.py (Captura os dados brutos)

python 02_transformacao/transformador.py (Limpa e filtra os dados)

python 02_transformacao/enriquecedor.py (Cruza dados com cadastro de operadoras)

python 02_transformacao/agregador.py (Gera estatísticas e médias)

🧠 Decisões Técnicas e Trade-offs
Durante o desenvolvimento, foram feitas as seguintes escolhas estratégicas para garantir a entrega e a qualidade dos dados:

1. Estratégia de Captura de Dados (Resiliência vs. Automação)
Situação: Os links oficiais de 2023 retornaram Erro 404 devido a mudanças estruturais no servidor da ANS.

Trade-off: Implementei uma rotina de investigação manual e automatizada para mapear a nova estrutura de diretórios de 2025.

Justificativa: Priorizei a continuidade do pipeline. Dados governamentais mudam com frequência; a solução foi adaptada para ser flexível a essas mudanças.

2. Filtragem por Granularidade Contábil (Precisão vs. Volume)
Situação: O arquivo original continha mais de 2 milhões de linhas com diferentes níveis de contas (contas "pai" e contas "filhas").

Trade-off: Filtrei especificamente o grupo de contas 411 (Eventos Conhecidos ou Avisados).

Justificativa: Somar todas as linhas causaria duplicidade (double-counting), pois as contas sintéticas já englobam os valores das analíticas. O grupo 411 reflete com precisão as despesas assistenciais solicitadas.

3. Tratamento de Valores e Sanitização (Qualidade dos Dados)
Situação: Existência de valores negativos e formatos de string com vírgula (padrão PT-BR).

Trade-off: Conversão de tipos para numérico e exclusão de registros negativos.

Justificativa: Na contabilidade de despesas, valores negativos costumam ser estornos. Para o cálculo de média e desvio padrão, mantê-los distorceria a análise de volatilidade real.

4. Estratégia de Join (Left Join vs. Inner Join)
Situação: Cruzamento entre a base de despesas e a base cadastral das operadoras.

Trade-off: Utilização de Left Join com tratamento de nulos.

Justificativa: Garante que o volume total de despesas seja preservado. Operadoras não encontradas no cadastro foram rotuladas como "Não Identificada" para evitar a perda de dados financeiros.

5. Contingência de Conexão (Fallback)
Situação: Instabilidades no servidor de FTP da ANS impediram o download direto em certas execuções.

Trade-off: Implementação de lógica de contingência (Mocking/Fallback) baseada nos registros ativos.

Justificativa: Um pipeline profissional deve ser capaz de concluir sua execução mesmo com falhas em serviços de terceiros, permitindo a validação das etapas de agregação e SQL.

📈 Resultados obtidos
Total bruto processado: ~2.113.000 linhas.

Total após limpeza e filtro assistencial: 113.288 linhas.

Operadoras analisadas: 712 empresas identificadas.


### O que eu mudei para você:
1.  **Termos Técnicos:** Corrigi "Solicitações" para **Requests** e "instale as partes" para **instale as dependências** (linguagem mais usada na área).
2.  **Correção de nomes:** Troquei "vôngdor" por **enriquecedor**.
3.  **Trade-offs Detalhados:** Adicionei as justificativas que explicam o porquê de cada escolha sua (isso mata a pau na entrevista!).
4.  **Formatação SQL:** Adicionei o bloco de código para os comandos de instalação ficarem mais legíveis.

**Dica:** Vá no seu repositório do GitHub, clique no lápis para editar o `README.md`, apague tudo o que está lá e cole esse novo texto. Depois, clique em "Commit changes".

Você está com o projeto na mão, Renato! Alguma dúvida antes de enviar? 🚀🏆
