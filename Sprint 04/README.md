# 📊 Entrega - Sprint 04

Nessa Sprint 04, a trilha foi dividida entre 2 cursos, sendo eles: **Machine Learning e Data Science com Python** e **Machine Learning com Amazon AWS SageMaker**.

## Link do Vídeo

# 📝 Exercícios

### Curso de Machine Learning e Data Science com Python
Durante o curso, não foram realizados diretamente exercícios, dessa forma, achei interessante fazer o upload dos arquivos notebooks referentes as aulas. Segue abaixo os arquivos divididos pela seção do curso:
1. **Regressão Linear**:

    ➡️ Confira o [notebook](./exercicios/curso%20machine%20learning/regressao-linear.ipynb).

2. **Outros tipos de Regressão**:

    ➡️ Confira o [notebook](./exercicios/curso%20machine%20learning/outras-regressoes.ipynb).    

3. **Algoritmo Apriori**:

    ➡️ Confira o [notebook](./exercicios/curso%20machine%20learning/apriori.ipynb).

4. **Agrupamento**:

    ➡️ Confira o [notebook](./exercicios/curso%20machine%20learning/agrupamento.ipynb).

5. **Seleção de Atributos**:

    ➡️ Confira o [notebook](./exercicios/curso%20machine%20learning/selecao-atributos.ipynb).

6. **Redução da Dimensionalidade (PCA)**:

    ➡️ Confira o [notebook](./exercicios/curso%20machine%20learning/reducao-dimensionalidade.ipynb).

5. **Detecção de Outliers**:

    ➡️ Confira o [notebook](./exercicios/curso%20machine%20learning/outliers.ipynb).


### Machine Learning com Amazon AWS SageMaker
Durante o curso foram realizados alguns exercícios, por questão de tempo não foi possível fazer todos eles, então achei interessante inserir os arquivos notebooks das aulas:

1. **Regressão com Linear Learner e XGBoost**:

    ➡️ Confira o [notebook do linear learner](./exercicios/curso%20amazon%20sagemaker/01%20-%20regressao/learner-houses.ipynb).

    ➡️ Confira o [notebook do xgboost](./exercicios/curso%20amazon%20sagemaker/01%20-%20regressao/xgboost.ipynb).

2. **Classificação com Linear Learner**:

    ➡️ Confira o notebook de [linear learner](./exercicios/curso%20amazon%20sagemaker/02%20-%20classificacao/learner-census.ipynb).

3. **Séries Temporais com DeepAr**:

    ➡️ Confira o notebook de [séries temporais](./exercicios/curso%20amazon%20sagemaker/03%20-%20serie%20temporal/bikes-deepar.ipynb).

4. **Detecção de Outliers com Random Cut Forest**:

    ➡️ Confira o notebook de [detecção de outliers](./exercicios/curso%20amazon%20sagemaker/04%20-%20outliers/bike-random-cut.ipynb).

5. **PCA com Agrupamento**:

    ➡️ Confira o notebook de [redução de dimensionalidade com agrupamento](./exercicios/curso%20amazon%20sagemaker/05%20-%20pca%20com%20agrupamento/pca-agrupamento-credit.ipynb).

6. **TensorFlow**:

    ➡️ Confira o notebook de [tensorflow clássico](./exercicios/curso%20amazon%20sagemaker/06%20-%20tensorflow/tensorflow-classico.ipynb).

# 📂 Evidências

### Curso de Machine Learning e Data Science com Python
Neste curso, foram aprofundados conceitos e algoritmos de Machine Learning de regressão linear e outros tipos de regressão até detecção de outliers:

- **Regressão**
  - A **regressão linear** é uma das técnicas estatísticas utilizada para 'modelar' a relação entre uma variável dependente (objetivo) e uma ou mais variáveis independentes (previsores). Uma coisa interessante a se destacar nesse curso, é que o instrutor deu foco na equação da reta, podendo até mesmo visualizar os valores da reta buscados na 'unha' utilizando alguns parâmetros como mostrado na imagem abaixo, e além disso é comparado com o resultado da previsão buscado pelo método de previsão:
  
  <p align="center">
    <img src="./evidencias/curso machine learning/reg-formula.png" alt="Gráfico de Regressão" width="400">
  </p>

  Outra coisa interessante a se observar é a geração de um gráfico de visualização dos residuais, esse gráfico mostra o quanto os dados estão afastados da linha de regressão:

  <p align="center">
    <img src="./evidencias/curso machine learning/grafico1.png" alt="Gráfico de Regressão" width="400">
    <img src="./evidencias/curso machine learning/grafico2.png" alt="Gráfico de Residuais" width="400">
  </p>

  - Outro ponto mostrado no curso foi a geração do gráfico de correlação que mostra o quanto as variáveis estão associadas. Esse gráfico é interessante para analisar quais variáveis dependentes podem ser utilizadas para fazer a previsão. A correlação pode ser obtido com o comando ``` base_de_dados.corr() ```.

  <p align="center">
    <img src="./evidencias/curso machine learning/grafico3.png" alt="Gráfico de Correlação" width="400">
  </p>

  - No curso são abordados outros tipos de regressões, a primeira delas é a **regressão polinomial** que é uma extensão da regressão linear, usada para modelar relações não lineares entre as variáveis. Nessa regressão é possível capturar curvaturas e padrões mais complexos nos dados, que não podem ser explicados por uma simples linha reta, como mostrado no gráfico abaixo. Outro tipo de regressão mostrado é a com **árvores de decisão** na qual utiliza um modelo baseado em divisões (splits) sucessivas dos dados (em formato de árvore), formando intervalos onde a predição é constante. Para cada intervalo, a média dos valores de `Y` dentro do intervalo é utilizada como predição.

 <p align="center">
    <img src="./evidencias/curso machine learning/grafico4-poly.png" alt="Gráfico de Regressão Polinomial" width="400">
    <img src="./evidencias/curso machine learning/grafico5-dt.png" alt="Gráfico de Regressão com DT" width="400">
  </p>

Nota-se que no algoritmo de árvore de decisão os dados são exatamente iguais, isso acontece por conta dos splits (segmentação dos dados em blocos).

  - Foram trabalhados outros algoritmos para regressão como regressão com suporte a vetor e redes neurais, mas o 'melhor' algoritmo foi o de random forest. O **Random Forest** é um algoritmo de aprendizado de máquina baseado em um conjunto de árvores de decisão fazendo ao final uma média e escolhendo o melhor modelo. Abaixo segue o gráfico gerado desse algoritmo:

  <p align="center">
    <img src="./evidencias/curso machine learning/grafico6-rf.png" alt="Gráfico de Correlação" width="400">
  </p>

Durante os testes, o random forest foi o algoritmo de regressão com os melhores resultados no dataset utilizado. Isso acontece pois sua capacidade de capturar tanto padrões globais quanto locais nos dados, gerando predições muito precisas.


- **Apriori**  
  - **Apriori** é um algoritmo utilizado para mineração de regras de associação em grandes conjuntos de dados. Ele é muito utilizado em cenários como análise de cestas de mercado (market basket analysis), na qual o objetivo é identificar itens que frequentemente aparecem juntos em transações. A imagem abaixo mostra as regras de associação escolhidas pelo algoritmo no dataset das aulas, bem como a construção do novo dataframe com as regras:

  <p align="center">
    <img src="./evidencias/curso machine learning/apriori.png" alt="Apriori" width="400">
    <img src="./evidencias/curso machine learning/apriori2.png" alt="Apriori" width="400">
    <img src="./evidencias/curso machine learning/aprioridt.png" alt="Apriori" width="400">
  </p>


- **Agrupamento**  
  - O agrupamento é uma técnica para agrupar dados que são semelhantes, nesse sentido, existem alguns algoritmos que foram mostrados no curso, sendo o primeiro deles o **K-Means**.
    - **K-Means** é um agrupamento não supervisionado que divide os dados em `K` clusters. Ele busca minimizar a variância dentro de cada cluster, agrupando pontos que são mais semelhantes entre si. Abaixo, segue como foi feita a clusterização com esse algoritmo. Além disso, quando não se tem certeza sobre a quantidade de centroides que serão criados, pode-se usar o método **WCSS**, nesse método, o ponto onde a redução do WCSS começa a diminuir significativamente é escolhido como o número ótimo de clusters.

  <p align="center">
    <img src="./evidencias/curso machine learning/kmeans.png" alt="K-Means" width="400">
    <img src="./evidencias/curso machine learning/kmeans-wcss.png" alt="WCSS" width="400">
  </p>

  Abaixo segue os gráficos referentes a codificação do K-Means e do WCSS acima:

  <p align="center">
    <img src="./evidencias/curso machine learning/grafico-kmeans.png" alt="Gráfico K-Means" width="400">
    <img src="./evidencias/curso machine learning/grafico-kmeans-wcss.png" alt="Gráfico WCSS" width="400">
  </p>

  - Outros dois algoritmos famosos são o **DBSCAN** e o **Agrupamento Hierárquico**, na qual o primeiro realiza o agrupamento baseado em densidade. Ele agrupa pontos densamente conectados e marca os pontos que não pertencem a nenhum cluster como ruído. O segundo cria uma árvore de agrupamentos chamada **dendrograma**:

   <p align="center">
    <img src="./evidencias/curso machine learning/dbscan.png" alt="DBSCAN" width="400">
    <img src="./evidencias/curso machine learning/grafico-dendrograma.png" alt="Dendrograma" width="400">
   </p>

   Ainda sobre agrupamento, ao final das aulas, foram feitas algumas comparações entre os algoritmos e a clusterização de ambos. Os resultados estão apresentados nos gráficos abaixo sendo o DBSCAN com desempenho superior aos outros dois.

   <p align="center">
    <img src="./evidencias/curso machine learning/graf-comp-hierarquico.png" alt="Hierárquico" width="300">
    <img src="./evidencias/curso machine learning/graf-comp-kmeans.png" alt="K-Means" width="300">
    <img src="./evidencias/curso machine learning/graf-comp-dbscan.png" alt="DBSCAN" width="300">
   </p>

- **Seleção de Atributos**  
  - A seleção de atributos é uma técnica usada para escolher os atributos mais relevantes em um conjunto de dados, removendo aqueles que não contribuem significativamente para o modelo. Nas aulas do curso, foi utilizado o critério da **variância** para identificar os atributos mais importantes:

   <p align="center">
    <img src="./evidencias/curso machine learning/atributos1.png" alt="Atributos" width="400">
    <img src="./evidencias/curso machine learning/atributos2.png" alt="Atributos" width="400">
   </p>

- **Outliers**  
  - A detecção de outliers é uma etapa fundamental na análise de dados, pois valores atípicos podem distorcer as análises e comprometer a performance de modelos de machine learning. Nas aulas foram utilizadas três técnicas para detecção de outliers, sendo: Boxplot, Gráfico de Dispersão e algoritmo PYOD.

   <p align="center">
    <img src="./evidencias/curso machine learning/boxplot.png" alt="Outliers" width="300">
    <img src="./evidencias/curso machine learning/grafico-dispersao.png" alt="Outliers" width="300">
    <img src="./evidencias/curso machine learning/outlier-pyod.png" alt="Outliers" width="300">
   </p>

### Curso de Machine Learning com Amazon AWS SageMaker

Nesse curso, os conceitos mais importantes de Machine Learning foram aplicados na prática utilizando a Amazon AWS SageMaker:

- **Regressão**  
  - Nesse curso, a regressão linear foi aplicada utilizando os algoritmos de **Linear Learner** e **XGBoost**, segue abaixo a parametrização e o treinamento de ambos:

  <p align="center">
    <img src="./evidencias/curso amazon sagemaker/regressao.png" alt="linear learner" width="400">
    <img src="./evidencias/curso amazon sagemaker/regressaoxg.png" alt="xgboost" width="400">
   </p>

  - No SageMaker, a utilização da regressão linear com o Linear Learner e o XGBoost comparado com os métodos comuns fora da AWS oferece alta eficiência e facilidade para resolver problemas de regressão. O Linear Learner é ideal para problemas lineares, pois é simples de interpretar, enquanto o XGBoost é mais poderoso para lidar com relações não-lineares e interações complexas entre variáveis. Ambos são otimizados para treinar rapidamente em grandes volumes de dados e permitem ajustes personalizados para melhorar a performance do modelo. Além disso, sua integração no SageMaker facilita o pré-processamento, a tunagem automática de hiperparâmetros e a implantação de modelos, tornando o processo mais ágil e eficiente.

    E por falar em tunagem...

    - **Tunning**  
        - O Tuning consiste em buscar os valores ideais para os hiperparâmetros de um modelo de machine learning, com o objetivo de melhorar sua performance. Durante o curso no SageMaker foram criados vários trabalhos de treinamento em paralelo, avaliando os modelos com base em uma métrica de performance (RMSE) e identificando a melhor configuração. Abaixo segue as melhores configurações obtidas com o dataset:

        <p align="center">
          <img src="./evidencias/curso amazon sagemaker/tunning.png" alt="Tuning" width="500">
        </p>

        Importante ressaltar que nesse caso em específico os valores do processo de tunagem não foram melhores que os dos algoritmos anteriores, mas isso acontece pelo fato de que o processo foi feito uma única vez. Para encontrar as melhores configurações possíveis é interessante realizar esse processo mais vezes.

- **Classificação**  
  - Para fazer a classificação, também foi utilizado o algoritmo de **Linear Learner** com a diferença de que, nesse caso, a previsão será de uma classe.

  <p align="center">
    <img src="./evidencias/curso amazon sagemaker/deploy-classificacao.png" alt="Tuning" width="500">
  </p>

  Um ponto interessante do SageMaker, é que há a possibilidade de fazer o deploy do modelo, ao chamar o método de deploy(), o modelo e o endpoint são criados.

- **Séries Temporais**  
  - Nesse curso, os dados foram treinados como séries temporais utilizando o algoritmo de DeepAR.

  <p align="center">
    <img src="./evidencias/curso amazon sagemaker/series-temporais.png" alt="Series Temporais" width="400">
    <img src="./evidencias/curso amazon sagemaker/grafico-series.png" alt="Gráfico de Series Temporais" width="400">
   </p>

   O DeepAR é um modelo baseado em redes neurais recorrentes (RNNs), especialmente projetado para prever séries temporais, permitindo que ele capture padrões complexos, sazonais e tendências em várias séries simultaneamente.

- **PCA com Agrupamento**  
  - No curso, a redução da dimensionalidade foi feita com o PCA e logo em seguida foi utilizado o K-Means para a clusterização. Abaixo está o resultado representado graficamente:

  <p align="center">
    <img src="./evidencias/curso amazon sagemaker/pca-agrupamento.png" alt="PCA e K-Means" width="400">
  </p>

- **Outliers**
  - O processo de detecção de outliers no curso foi feito com o algoritmo de Random Cut Forest.

  <p align="center">
    <img src="./evidencias/curso amazon sagemaker/outlier-randomcut.png" alt="Random Cut Forest" width="530">
    <img src="./evidencias/curso amazon sagemaker/outlier-randomcut2.png" alt="Random Cut Forest" width="400">
  </p>

  Para encontrar os outliers (pontos em preto no gráfico), foi usado a regra comum da média e desvio padrão que é verificar se os valores estão fora de um intervalo de 3 desvios padrão (3σ) acima da média.
  

## 🏆 Certificados

Segue abaixo os certificados obtidos nos cursos da Sprint 04:

1. **Machine Learning com Amazon AWS SageMaker**
![Certificado 1](./certificados/Certificado%20Machine%20Learning%20na%20AWS%20SageMaker.jpg)  

Não foi possível obter o certificado do primeiro curso de Machine Learning com Python, uma vez que foi determinado completar apenas algumas seções do curso. 
