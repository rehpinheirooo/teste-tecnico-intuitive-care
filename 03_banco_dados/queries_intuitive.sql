-- 1. Criação da Tabela de Despesas (Onde vamos guardar o arquivo final)
CREATE TABLE despesas_operadoras (
    id SERIAL PRIMARY KEY,
    cnpj VARCHAR(18),
    razao_social VARCHAR(255),
    trimestre VARCHAR(2),
    ano INT,
    valor_despesas DECIMAL(15, 2),
    registro_ans INT,
    modalidade VARCHAR(100),
    uf VARCHAR(2)
);

-- 2. Query para responder: Quais as 10 operadoras que mais tiveram despesas no último trimestre?
-- Essa query mostra que você sabe ordenar e limitar resultados.
SELECT 
    razao_social, 
    SUM(valor_despesas) AS total_gasto
FROM despesas_operadoras
WHERE ano = 2025 AND trimestre = '3T'
GROUP BY razao_social
ORDER BY total_gasto DESC
LIMIT 10;

-- 3. Query para responder: Qual a média de gastos por modalidade de operadora?
-- Mostra que você sabe agrupar dados por categorias.
SELECT 
    modalidade, 
    ROUND(AVG(valor_despesas), 2) AS media_por_modalidade
FROM despesas_operadoras
GROUP BY modalidade
ORDER BY media_por_modalidade DESC;