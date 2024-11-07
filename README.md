# Predição de Potenciais Anunciantes - Praceando

## Descrição do Projeto
Este projeto visa a **predição de potenciais clientes** para o aplicativo **Praceando**, através de técnicas de clusterização e classificação. A principal meta é identificar usuários com alto potencial para se tornarem **anunciantes** do aplicativo, utilizando algoritmos de aprendizado de máquina para identificar padrões e prever esses potenciais. Esta análise possibilita direcionar campanhas de marketing mais eficazes e otimizar as estratégias de monetização do Praceando.

## Bibliotecas Utilizadas
- **Pandas, NumPy**: Manipulação e tratamento de dados.
- **Matplotlib, Seaborn**: Visualização dos dados e métricas de desempenho dos modelos.
- **Scikit-learn**:
  - **Pipeline, ColumnTransformer**: Para pré-processamento dos dados.
  - **StandardScaler, OrdinalEncoder, OneHotEncoder**: Escalonamento e codificação das features.
  - **KMeans, PCA (Principal Component Analysis)**: Técnicas de clusterização e redução de dimensionalidade.
  - **Naive Bayes, Decision Tree, K-Nearest Neighbors**: Modelos de classificação.
  - **train_test_split, KFold, GridSearchCV**: Para separação dos dados e validação cruzada.
  - **Métricas de avaliação**: Precisão, F1-score, matriz de confusão, entre outras.
- **Yellowbrick**:
  - **KElbowVisualizer**: Para identificar o número ideal de clusters.
- **Imbalanced-Learn (SMOTE)**: Para balanceamento de classes e lidar com o problema de desbalanceamento dos dados.

## Etapas do Projeto

### 1. Consumo e Tratamento de Dados
- **Consumo dos Dados**: A base de dados utilizada foi a **Praceando_supervisionado.csv**, que contém informações dos usuários que participaram de um formulário sobre eventos públicos.
- **Pré-Processamento**:
  - **Remoção de colunas irrelevantes**, como IDs.
  - **Codificação das features categóricas** utilizando **OrdinalEncoder**.
  - **Escalonamento das features** numéricas utilizando **StandardScaler**.
  - Utilizamos um **Pipeline** para aplicar todas essas transformações, garantindo um processo automatizado e padronizado.

### 2. Clusterização de Potenciais Clientes
Aplicamos técnicas de **clusterização** usando **KMeans** e determinamos a quantidade ideal de clusters com o **KElbowVisualizer**. A clusterização ajudou a entender os diferentes perfis dos usuários e identificar grupos com maior potencial para se tornarem anunciantes.

### 3. Modelagem Preditiva
- Foram utilizados três modelos principais para a predição:
  1. **Naive Bayes (GaussianNB)**.
  2. **Árvore de Decisão (Decision Tree Classifier)**.
  3. **K-Nearest Neighbors (KNN)**.
- Utilizamos **validação cruzada (KFold)** para garantir a robustez dos resultados dos modelos e **GridSearchCV** para encontrar os melhores hiperparâmetros.
- **Métricas Avaliadas**: Precisão, F1-score e matriz de confusão foram as principais métricas utilizadas para avaliar a performance dos modelos.

### 4. Balanceamento de Classes
Utilizamos o **SMOTE** para balancear a base de dados devido ao desbalanceamento entre as classes "anunciante" e "não anunciante". O SMOTE gerou novas amostras sintéticas da classe minoritária, garantindo que os modelos tivessem dados mais equilibrados para treinar, o que melhorou a capacidade de generalização dos modelos.

### 5. Redução de Dimensionalidade com PCA
Para facilitar a visualização e reduzir a complexidade dos dados, aplicamos **PCA** (Principal Component Analysis). A técnica foi utilizada para reduzir a quantidade de variáveis, preservando a variância explicada e permitindo uma análise mais direta dos padrões presentes nos dados.

### 6. Serialização do Melhor Modelo
Após testar os modelos, o **KNN** com os melhores hiperparâmetros e utilizando SMOTE apresentou o melhor desempenho. Esse modelo foi então **serializado** utilizando **Joblib**, facilitando sua aplicação futura para predições de novos dados.

### 7. Resultados e Conclusões
- **Clusters de Potenciais Anunciantes**: Os usuários foram agrupados em diferentes clusters, dos quais identificamos grupos que apresentavam maior disposição para pagar por anúncios e maior frequência de organização de eventos.
- **Melhor Modelo Preditivo**: O **KNN** com hiperparâmetros otimizados e usando dados balanceados com **SMOTE** mostrou o melhor desempenho para prever os potenciais anunciantes do Praceando.

## Visualização dos Resultados
- **Clusterização**: Gráficos **3D** utilizando as componentes principais foram gerados para visualizar a distribuição dos clusters e entender melhor os padrões de comportamento dos usuários.
- **Matriz de Confusão**: Cada modelo gerou uma matriz de confusão que foi visualizada para avaliar a capacidade do modelo em distinguir corretamente entre anunciantes e não anunciantes.

![Visualização dos Clusters](link-para-imagem)

## Como Executar o Projeto
### Pré-requisitos
- Python 3.7+
- Bibliotecas listadas no **requirements.txt**

### Instruções
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/predicao-anunciantes-praceando.git
   cd predicao-anunciantes-praceando
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python clusterizacao_anunciantes.py
   ```

Para mais informações, entre em contato com os membros da equipe de dados :
- [Fernanda Leão](https://github.com/fernandaleaoleita)
- [Guilherme Barbosa](https://github.com/guii-barbosa)
