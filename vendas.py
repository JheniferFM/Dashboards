import pandas as pd
import numpy as np

# Criar dados fictícios
np.random.seed(42)  # Para garantir reprodutibilidade
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

dados = {
    "Mês": meses,
    "Vendas (R$)": np.random.randint(200, 1000, size=12),
    "Custo (R$)": np.random.randint(100, 500, size=12),
}

# Criar o DataFrame
df = pd.DataFrame(dados)

# Calcular lucro
df["Lucro (R$)"] = df["Vendas (R$)"] - df["Custo (R$)"]

# Salvar em Excel
arquivo_excel = "dados_vendas.xlsx"
df.to_excel(arquivo_excel, index=False)
print(f"Dados salvos no arquivo {arquivo_excel}")
