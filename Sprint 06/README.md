# 📊 Entrega - Sprint 06

Nessa Sprint 06, a trilha foi dividida entre 3 cursos, sendo eles: **Formação Processamento de Linguagem Natural, LLMs e GenAI**, **MLOps: Implatação e Operação de Modelos de Machine Learning** e **Face Recognition with Machine Learning**.

## Link do Vídeo
---

# 📝 Exercícios

### Formação Processamento de Linguagem Natural, LLMs e GenAI
Durante o curso, não foram realizados diretamente exercícios, dessa forma, achei interessante fazer o upload dos arquivos notebooks referentes as aulas. Segue abaixo os arquivos divididos pela seção do curso:
1. **NLP com Spacy**:

    ➡️ Confira o [notebook](./exercicios/curso%20de%20nlp/spacy/spacy.ipynb).

2. **NLP com NLTK**:

    ➡️ Confira o [notebook](./exercicios/curso%20de%20nlp/nltk/nltk.ipynb).    

3. **Machine Learning e Deep Learning com NLP na prática**:

    ➡️ Confira o notebook de [machine learning](./exercicios/curso%20de%20nlp/machine%20e%20deep%20learning%20nlp/ml-spam.ipynb).

    ➡️ Confira o primeiro notebook de [rede neural](./exercicios/curso%20de%20nlp/machine%20e%20deep%20learning%20nlp/rede-neural.ipynb).

    ➡️ Confira o segundo notebook de [rede neural](./exercicios/curso%20de%20nlp/machine%20e%20deep%20learning%20nlp/rede-neural-2.ipynb).


4. **Analise de Sentimentos**:

    ➡️ Confira o notebook de [LSTM](./exercicios/curso%20de%20nlp/analise%20de%20sentimentos/lstm.ipynb).

    ➡️ Confira o notebook de [bert](./exercicios/curso%20de%20nlp/analise%20de%20sentimentos/bert.ipynb).

    ➡️ Confira o notebook de [regras supervisionado](./exercicios/curso%20de%20nlp/analise%20de%20sentimentos/regras-supervisionado.ipynb).

    ➡️ Confira o notebook de [vader](./exercicios/curso%20de%20nlp/analise%20de%20sentimentos/vader.ipynb).

5. **Transformers, Bert e GPT**:

    ➡️ Confira o notebook de [geração de textos](./exercicios/curso%20de%20nlp/transformers,%20bert%20e%20gpt/geracao-texto.ipynb).

    ➡️ Confira o notebook de [preenchimento de lacunas](./exercicios/curso%20de%20nlp/transformers,%20bert%20e%20gpt/preenchimento-lacunas.ipynb).

    ➡️ Confira o notebook de [perguntas e respostas](./exercicios/curso%20de%20nlp/transformers,%20bert%20e%20gpt/perguntas-respostas.ipynb).

    ➡️ Confira o notebook de [resumo de textos](./exercicios/curso%20de%20nlp/transformers,%20bert%20e%20gpt/resumo-textos.ipynb).

6. **Modelagem de Tópicos**:

    ➡️ Confira o [notebook](./exercicios/curso%20de%20nlp/modelagem%20de%20topicos/bert.ipynb).


### MLOps: Implatação e Operação de Modelos de Machine Learning
Como no curso de NLP, o de MLOps também não tiveram exercícios. Dado isso, estarei seguindo o mesmo padrão e inserindo os notebooks do curso como exercícios.

1. **MLFlow com Naive Bayes**:

    ➡️ Confira o [notebook](./exercicios/curso%20de%20mlops/MLFlow-NB.ipynb).

2. **MLFlow com Random Forest**:

    ➡️ Confira o [notebook](./exercicios/curso%20de%20mlops/MLFlow-RF.ipynb).

3. **MLFlow com Keras**:

    ➡️ Confira o [notebook](./exercicios/curso%20de%20mlops/MLFlow-Keras.ipynb).


# 📂 Evidências

### Formação Processamento de Linguagem Natural, LLMs e GenAI
Nesse curso, foram aprofundados conceitos de processamento de linguagem natural, com bibliotecas como Spacy, NLTK e Spark, bem como LLMs com Bert e GPT, além de analise de sentimentos. Segue abaixo evidências das seções:

- **NLP com Spacy**: O **spacy** é uma biblioteca de **Processamento de Linguagem Natural (NLP)** com a vantagem de ter bom desempenho e escalabilidade. A biblioteca fornece diversas funcionalidades comuns de NLP como tokenização, lematização, análise sintática, reconhecimento de entidades nomeadas (NER) e comparação de similaridade entre palavras e sentenças.

- Começando pela funcionalidade de Tokenização, que é o processo de dividir um texto em unidades menores chamadas **tokens**, como palavras ou pontuações. O **spacy** permite uma tokenização eficiente e também possui uma lista integrada de **stop words**, que são palavras consideradas sem grande relevância.  Posteriormente, foi feito o processo de **POS-Tagging (Part-of-Speech Tagging)**, que identifica a classe gramatical de cada palavra no texto, como substantivo, verbo ou adjetivo. Um pouco dos resultados será mostrado nas imagens abaixo:

<p align="center">
    <img src="./evidencias/curso de nlp/spacy-tok.png" alt="Tokenização" width="400">
    <img src="./evidencias/curso de nlp/spacy-postag.png" alt="PosTagging" width="400">
</p>

- Um ponto interessante é que o spacy mantém um **vocabulário** interno onde cada palavra recebe um **ID único**. Esse vocabulário permite mapear as palavras para seus ids correspondentes. A forma de indentifivá-los está na imagem abaixo. Além disso, uma das funcionalidades mais legais do spacy é a **similaridade entre palavras e sentenças**, utilizando embeddings semânticos para entender relações entre termos.

<p align="center">
    <img src="./evidencias/curso de nlp/spacy-vocab.png" alt="Vocabulário" width="400">
    <img src="./evidencias/curso de nlp/spacy-similarity.png" alt="Similaridade" width="400">
</p>

- Outro ponto interessante é o **Reconhecimento de Entidades Nomeadas (NER)** que permite identificar elementos importantes em um texto, como **nomes de pessoas, locais, organizações, datas e valores monetários**. O **spaCy** classifica automaticamente essas entidades usando `ent.label_`.  

<p align="center">
    <img src="./evidencias/curso de nlp/spacy-entidades.png" alt="Entidades" width="400">
</p>

- Por último,  foi possível verificar graficamente a análise das dependências com **displacy**. O displacy é uma ferramenta visual do spacy que permite representar graficamente a estrutura de um texto. Ele exibe a relação entre os tokens, mostrando suas tags gramaticais e conexões sintáticas de maneira intuitiva.  Abaixo é possível ver uma parte dessa análise.

<p align="center">
    <img src="./evidencias/curso de nlp/spacy-display.png" alt="Dependências" width="500">
</p>

- O **NLTK (Natural Language Toolkit)** é uma das bibliotecas mais utilizadas para **Processamento de Linguagem Natural (NLP)** em Python. Ele fornece muitas ferramentas para análise de texto, incluindo tokenização, stemming, lematização, análise sintática e reconhecimento de entidades nomeadas, como vistas no curso de Spacy.

- Como as técnicas de **NLP** são praticamente as mesmas aplicadas com spacy, optei por não inserir evidências de processos como tokenização, POS-Tagging e outros já mencionados anteriormente. Porém, um ponto interessante que não foi abordado no spacy é a busca pela **frequência de uma palavra em uma sentença**, conforme mostrado na imagem abaixo:  

<p align="center">
    <img src="./evidencias/curso de nlp/nltk-frequency.png" alt="Frequências" width="500">
</p>

- **Machine Learning e Deep Learning com NLP na Prática**:

- **Machine Learning com NLP**: Nesta parte, foi utilizado um **dataset de spam** para prever se um e-mail é **spam ou não**. Para isso, foram utilizados os passos comuns ao fazer previsões:

- **Preparação dos dados**: Separação das variáveis em features e target.  
- **Vetorização**: Aplicação do `TfidfVectorizer` para converter os textos em representações numéricas.  
- **Treinamento do modelo**: Utilização do algoritmo **Random Forest** para aprendizado.  
- **Avaliação**: Foram realizadas previsões e as métricas obtidas demonstraram um bom desempenho do modelo. 

Porém, ao inserir **novos dados**, o modelo apresentou erro na previsão, conforme ilustrado na imagem abaixo. Mas isso não significa que o modelo tem desempenho ruim.

<p align="center">
    <img src="./evidencias/curso de nlp/ml-spam.png" alt="Frequências" width="500">
</p>

- **Deep Learning com NLP**: O mesmo problema foi abordado utilizando **Redes Neurais**, seguindo um fluxo semelhante, mas usando uma abordagem diferente de vetorização com o `CountVectorizer` e **redes neurais** para treinamento.

- **Análise de Sentimentos**:
Para a análise de sentimentos, foram testadas diferentes abordagens, incluindo:  
- **LSTM (Long Short-Term Memory)**  
- **BERT (Bidirectional Encoder Representations from Transformers)**  
- **Regras Supervisionadas**  

Contudo, o exemplo apresentado abaixo utiliza o **Vader**, uma ferramenta baseada em regras, otimizada para análise de sentimentos em textos curtos, como comentários e também tweets. No exemplo, foram utilizada sentenças simples e através do `mas.popularity_score()` foi possível obter as métricas correspondentes as três classes negativo, positivo, neutro.

<p align="center">
    <img src="./evidencias/curso de nlp/vader-analise-sentimentos.png" alt="Vader" width="500">
</p>

- Outra parte bem legal dos cursos foi a utilização do **Transformers** com o **Hugging Face Hub**. Através deles, foi possível testar modelos já treinados para diferentes tarefas de NLP.  

Primeiramente, exploramos a funcionalidade de **Perguntas e Respostas**, onde um modelo recebe um texto e responde perguntas com base nele. Outra aplicação interessante foi o **preenchimento de lacunas**, onde o modelo completa palavras faltantes dentro de uma frase, demonstrando sua capacidade contextual.

<p align="center">
    <img src="./evidencias/curso de nlp/pergunta-resposta.png" alt="*" width="400">
    <img src="./evidencias/curso de nlp/lacunas.png" alt="#" width="400">
</p>

### MLOps: Implatação e Operação de Modelos de Machine Learning
O curso de MLOps foi de longe um dos mais interessantes e proveitsos da trilha. Nesse curso foi possível entender o processo por trás do registro e implantação de um modelo de machine learning utilizando **MLFlow**.

Com o MLflow, foi possível:  
- **Registrar modelos treinados** e acompanhar suas versões. Posteriormente foi possível**interagir com a interface do MLflow**, visualizando métricas e artefatos dos experimentos.  

- O primeiro modelo a ser registrado foi o de **Naive Bayes**:
<p align="center">
    <img src="./evidencias/curso mlops/mlflow-ui.png" alt="MLFLOW" width="600">
</p>

Outro ponto interessante é que foi possível gerar gráficos para ter uma noção do desempenho, como o gráfico de **Matriz de Confusão** e o gráfico de **ROC**:

<p align="center">
    <img src="./evidencias/curso mlops/matriz1.png" alt="Matriz de Confusão" width="400">
    <img src="./evidencias/curso mlops/roc1.png" alt="ROC" width="400">
</p>

- O segundo modelo a ser registrado foi o de **Random Forest**:
<p align="center">
    <img src="./evidencias/curso mlops/mlflow-ui2.png" alt="MLFLOW" width="600">
</p>

O modelo possui mais registros pois a execução foi através de um looping aumentando o número de árvores a cada vez que rodasse, sendo primeiro com 50, depois 100, 500, 750 e 1000. Abaixo, segue a comparação da matriz de confusão com todas as cinco quantidades de árvores mencionadas anteriormente.

<p align="center">
    <img src="./evidencias/curso mlops/matriz_rf1.png" alt="Matriz de Confusão" width="300">
    <img src="./evidencias/curso mlops/matriz_rf2.png" alt="Matriz de Confusão" width="300">
    <img src="./evidencias/curso mlops/matriz_rf3.png" alt="Matriz de Confusão" width="300">
    <img src="./evidencias/curso mlops/matriz_rf4.png" alt="Matriz de Confusão" width="300">
    <img src="./evidencias/curso mlops/matriz_rf5.png" alt="Matriz de Confusão" width="300">
</p>

- O terceiro modelo a ser registrado foi utilizando o **Keras**:
<p align="center">
    <img src="./evidencias/curso mlops/mlflow-ui3.png" alt="MLFLOW" width="600">
</p>