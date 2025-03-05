import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulando dados fictícios de vendas
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=12, freq="M")
sales = np.random.randint(5000, 20000, size=len(dates))
customers = np.random.randint(100, 500, size=len(dates))
avg_ticket = sales / customers

# Criando um DataFrame
df = pd.DataFrame({"Data": dates, "Vendas": sales, "Clientes": customers, "Ticket Médio": avg_ticket})

# Criando um painel com múltiplos gráficos
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Gráfico 1 - Evolução das vendas
sns.lineplot(ax=axes[0, 0], x=df["Data"], y=df["Vendas"], marker="o", color="b")
axes[0, 0].set_title("Evolução das Vendas Mensais")
axes[0, 0].set_xlabel("Data")
axes[0, 0].set_ylabel("Vendas")
axes[0, 0].tick_params(axis='x', rotation=45)

# Gráfico 2 - Distribuição do Ticket Médio
sns.histplot(ax=axes[0, 1], x=df["Ticket Médio"], bins=10, kde=True, color="g")
axes[0, 1].set_title("Distribuição do Ticket Médio")
axes[0, 1].set_xlabel("Valor do Ticket Médio")
axes[0, 1].set_ylabel("Frequência")

# Gráfico 3 - Ticket Médio por Mês
sns.barplot(ax=axes[1, 0], x=df["Data"].dt.strftime("%b/%Y"), y=df["Ticket Médio"], palette="coolwarm")
axes[1, 0].set_title("Ticket Médio por Mês")
axes[1, 0].set_xlabel("Mês")
axes[1, 0].set_ylabel("Valor do Ticket Médio")
axes[1, 0].tick_params(axis='x', rotation=45)

# Gráfico 4 - Correlação entre Clientes e Vendas
sns.scatterplot(ax=axes[1, 1], x=df["Clientes"], y=df["Vendas"], color="r", alpha=0.7)
axes[1, 1].set_title("Correlação entre Clientes e Vendas")
axes[1, 1].set_xlabel("Número de Clientes")
axes[1, 1].set_ylabel("Vendas")

plt.tight_layout()
plt.savefig("painel_analise_dados.png")
plt.show()
