# 🚀 Desafio Técnico - Cuidado Intuitivo

**Candidato:** Renato Pinheiro Ferreira

Este projeto consiste em um pipeline de dados completo para captura, tratamento, enriquecimento e análise estatística dos dados de demonstrações contábeis de operadoras de saúde, utilizando a base de dados abertos da ANS.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.14**: Linguagem principal para processamento e limpeza.
* **Pandas**: Manipulação de grandes volumes de dados (2M+ linhas).
* **Requests**: Integração e captura de arquivos do servidor FTP da ANS.
* **SQL**: Estruturação de queries para modelagem de banco de dados.

---

## 💻 Como Executar o Projeto

1.  **Instale as dependências:**
    ```bash
    pip install pandas requests
    ```

2.  **Execute o pipeline na ordem abaixo:**
    ```bash
    python 01_integracao_api/coletor.py      # Captura os dados brutos
    python 02_transformacao/transformador.py # Limpa e filtra os dados
    python 02_transformacao/enriquecedor.py  # Cruza dados com cadastro
    python 02_transformacao/agregador.py     # Gera estatísticas e médias
    ```

---

## 🧠 Decisões Técnicas e Trade-offs

Durante o desenvolvimento, foram feitas escolhas estratégicas para garantir a entrega e a qualidade dos dados:

### 1. Estratégia de Captura de Dados
* **Situação:** Links oficiais de 2023 retornando Erro 404 por mudanças no servidor ANS.
* **Trade-off:** Implementação de rotina de mapeamento dinâmico para os diretórios de 2025.
* **Justificativa:** Garantia da continuidade do pipeline mesmo diante de instabilidades em fontes governamentais.

### 2. Filtragem por Granularidade Contábil
* **Situação:** Base bruta com mais de 2 milhões de registros e contas duplicadas por níveis.
* **Trade-off:** Filtro exclusivo no grupo de contas **411 (Eventos Conhecidos ou Avisados)**.
* **Justificativa:** Evita o *double-counting* (contagem dupla) de valores, mantendo apenas o nível analítico real das despesas assistenciais.

### 3. Tratamento de Valores e Sanitização
* **Situação:** Dados brutos com formatos regionais (vírgula decimal) e valores negativos.
* **Trade-off:** Sanitização para padrão numérico internacional e exclusão de registros negativos.
* **Justificativa:** Valores negativos em despesas operacionais representam estornos que distorceriam a análise de média e volatilidade.

### 4. Estratégia de Join e Enriquecimento
* **Situação:** Necessidade de cruzar dados financeiros com informações cadastrais de operadoras.
* **Trade-off:** Utilização de **Left Join** com preenchimento de valores padrão para dados nulos.
* **Justificativa:** Priorização da integridade do volume financeiro; mesmo operadoras sem cadastro atualizado permanecem na análise como "Não Identificadas".

---

## 📈 Resultados Obtidos

* **Total bruto processado:** ~2.113.000 linhas.
* **Total após limpeza e filtro:** 113.288 linhas.
* **Operadoras analisadas:** 712 empresas identificadas.
