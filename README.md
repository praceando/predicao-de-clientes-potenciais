# Predição de Potenciais Anunciantes - Praceando

## Descrição do Projeto
Este projeto tem como objetivo realizar a **clusterização de potenciais anunciantes** para o aplicativo **Praceando**, identificando perfis de usuários que possuam maior potencial para se tornarem anunciantes do app. A partir de uma base de dados coletada através de um formulário, aplicamos técnicas de análise exploratória, redução de dimensionalidade e clustering, utilizando algoritmos de aprendizado não supervisionado.

## Objetivo
O objetivo principal é **identificar padrões de comportamento** e **segmentar os usuários** em clusters, de forma a identificar aqueles que têm maior interesse em anunciar eventos no Praceando. Através dessa segmentação, conseguimos diferenciar os perfis e encontrar os potenciais anunciantes, auxiliando na criação de estratégias personalizadas para cada grupo.

## Bibliotecas Utilizadas
- **Pandas**: Manipulação e tratamento da base de dados.
- **Matplotlib**: Visualização de dados para análise e entendimento dos clusters.
- **Scikit-learn**:
  - **KMeans**: Algoritmo de clusterização utilizado para agrupar os dados.
  - **PCA** (Principal Component Analysis): Redução da dimensionalidade dos dados para facilitar a visualização e melhorar a performance do algoritmo de clusterização.
- **Yellowbrick**:
  - **KElbowVisualizer**: Visualização da métrica para determinar o número ideal de clusters.

## Etapas do Projeto

### 1. Consumo de Dados e Definição de Features
Carregamos os dados da planilha **Praceando.xlsx**, que continha **92 linhas e 20 colunas** com respostas sobre o comportamento e preferências dos usuários em relação à organização e participação em eventos públicos.

### 2. Tratamento das Features
- **Remoção de Features Redundantes**: Eliminamos colunas desnecessárias, como e-mail e informações repetitivas, para focar nas informações que realmente contribuem para a análise.
- **Renomeação de Colunas**: Padronizamos os nomes das colunas para facilitar o uso e melhorar a legibilidade do código.
- **Tratamento de Valores Nulos**: Valores nulos foram preenchidos com opções padrão, garantindo que os dados estivessem completos e prontos para a análise.
- **Tratamento Personalizado**: Realizamos transformações específicas, como padronização de textos para minúsculas e conversão de categorias para valores numéricos, de modo a preparar os dados para a clusterização.

### 3. Redução de Dimensionalidade com PCA
Utilizamos **PCA (Principal Component Analysis)** para reduzir a dimensionalidade dos dados a **3 componentes principais**. Esta técnica permitiu visualizar os dados de maneira simplificada, mantendo uma alta variância explicada, o que facilita a análise dos clusters formados.

### 4. Clusterização dos Usuários
- Utilizamos o algoritmo de **KMeans** para agrupar os usuários em **6 clusters**, selecionando o número de clusters com base no método **Elbow**, que utiliza a métrica de **silhouette score**.
- Os clusters foram analisados para identificar padrões entre os usuários, permitindo definir perfis de potenciais anunciantes.

### 5. Análise dos Clusters
- Os usuários foram agrupados em **clusters** de acordo com variáveis como:
  - **Faixa etária**.
  - **Dificuldade em divulgar eventos**.
  - **Frequência de organização de eventos**.
  - **Disposição para pagar por divulgação**.
- A partir dessa análise, identificamos quais clusters tinham maior probabilidade de conter potenciais anunciantes.

### 6. Resultados e Conclusões
Com base na análise dos clusters, determinamos que:
- Alguns clusters, como o **Cluster 4**, apresentavam características ideais para possíveis anunciantes, como maior frequência de organização de eventos e disposição para pagar por divulgação.
- As variáveis que mais influenciaram na clusterização incluíram o **tipo de evento organizado**, **meios de divulgação utilizados** e **região de residência**.

## Visualização dos Clusters
Foi feita uma visualização dos clusters em um gráfico **3D** utilizando as componentes principais (PCA1, PCA2, PCA3). Isso nos permitiu entender como os usuários estavam agrupados e identificar quais clusters representavam um maior potencial de anúncios no Praceando.

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
## Conclusão
O projeto de clusterização de potenciais anunciantes do Praceando foi fundamental para **identificar padrões de comportamento** dos usuários, segmentando-os em grupos com diferentes níveis de interesse em anúncios. Essa análise contribui para decisões mais assertivas em campanhas e para um melhor direcionamento de funcionalidades específicas do aplicativo.

Para mais informações, entre em contato com os membros da equipe de dados :
- [Fernanda Leão](https://github.com/fernandaleaoleita)
- [Guilherme Barbosa](https://github.com/guii-barbosa)
