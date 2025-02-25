# 📊 Entrega - Sprint 07

Nessa Sprint 07, a trilha foi dividida entre 2 cursos, sendo eles: **Amazon Bedrock, Amazon Q & AWS Generative AI [HANDS-ON]** e **Credit Risk Modeling in Python**.

## Link do Vídeo
https://compasso-my.sharepoint.com/:v:/r/personal/emanuelle_lima_pb_compasso_com_br/Documents/emanuelle.lima-sprint07.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=Ldjqah

---

# 📝 Exercícios

### Amazon Bedrock, Amazon Q & AWS Generative AI
Durante o curso, não foram realizados diretamente exercícios, dessa forma, achei interessante fazer o upload das funções criadas nas aulas. Segue abaixo os arquivos divididos pela seção do curso:
1. **Amazon Bedrock**:

    ➡️ Confira o arquivo da [função lambda para gerar imagens](./exercicios/curso%20bedrock/moviePosterDesign.py).

    ➡️ Confira o arquivo da [função lambda para gerar texto](./exercicios/curso%20bedrock/demoManufacturing.py).

    ➡️ Confira o arquivo da [função lambda para criar embeddings](./exercicios/curso%20bedrock/demoVectorEmbeddings.py).

    ➡️ Confira o arquivo do [backend do chatbot](./exercicios/curso%20bedrock/chatbot_backend.py).

    ➡️ Confira o arquivo do [frontend do chatbot](./exercicios/curso%20bedrock/chatbot_frontend.py).

    ➡️ Confira o arquivo do [backend do q&a](./exercicios/curso%20bedrock/rag_backend.py).

    ➡️ Confira o arquivo do [frontend do q&a](./exercicios/curso%20bedrock/rag_frontend.py).


### Credit Risk Modeling in Python
Durante o curso, não foram realizados diretamente exercícios, dessa forma, achei interessante fazer o upload das funções criadas nas aulas. Segue abaixo os arquivos divididos pela seção do curso:

1. **Modelagem de Risco de Crédito**:

    ➡️ Confira o arquivo do [pré-processamento](./exercicios/curso%20credit%20risk/credit_risk_preprocessing.ipynb).

    ➡️ Confira o arquivo do [modelo PD](./exercicios/curso%20credit%20risk/pd-model.ipynb).

    ➡️ Confira o arquivo dos [modelos LGD e EAD](./exercicios/curso%20credit%20risk/lgd-ead-model.ipynb).


# 📂 Evidências

### Amazon Bedrock, Amazon Q & AWS Generative AI
Nesse curso, foram aprofundados casos de usos das áreas de GenAI com o Amazon Bedrock, Amazon Q e AWS Generative AI.

- **Amazon Bedrock**:

    - Inicialmente no curso, foram aprofundados conceitos de **geração de imagem com modelos do Amazon Bedrock**. Para isso, foi criada uma função lambda chamada [moviePosterDesign](./exercicios/curso%20bedrock/moviePosterDesign.py) que realizava a conexão com a API do Bedrock e dessa forma, através da variável de prompt, era possível escrever qual imagem você gostaria que fosse criada. Essa variável prompt era testada na aba de *Test*, com a *request* sendo passada da forma que a primeira imagem mostra. A segunda imagem, é o resultado da requisição.

<p align="center">
    <img src="./evidencias/curso bedrock/prompt-dog.png" alt="PromptRequest" width="500">
    <img src="./evidencias/curso bedrock/dog.png" alt="Cachorro" width="400">
</p>

Para que fosse possível salvar as imagens requisitadas, foi feita a conexão da função lambda com o S3 Bucket, assim, todas as vezes que foi pedido a geração de uma imagem no prompt, essas imagens foram armazenadas dentro do bucket *movieposter-bedrock-sprint07*.

<p align="center">
    <img src="./evidencias/curso bedrock/s3-poster-name.png" alt="Bucket" width="500">
</p>

Posteriormente, foi criada uma *API Gateway*, que comunicava com a função lambda criada acima, e através da criação do *method* e o deploy dela, também foi possível gerar imagens por meio de requisições no *prompt*, como é mostrado abaixo:

<p align="center">
    <img src="./evidencias/curso bedrock/prompt-api.png" alt="PromptRequest" width="500">
    <img src="./evidencias/curso bedrock/movie-poster.png" alt="moviePoster" width="400">
</p>

Por último, foi utilizado o [Postman](https://www.postman.com/company/about-postman/) para testar se a API construída funcionava em outros ambientes, e através do método *GET*, na caixa de *values* que foi utilizada como um prompt se comparado com as outras formas mostradas acima, foi possível gerar a imagem pedida na descrição. Lembrando que indepentende do ambiente ou forma, a imagem gerada é armazenada no S3.

<p align="center">
    <img src="./evidencias/curso bedrock/postman.png" alt="PromptRequest" width="500">
    <img src="./evidencias/curso bedrock/helicpt.png" alt="moviePoster" width="400">
</p>


 - Posteriormente no curso, foi trabalhado o *Text Summarization* utilizando o modelo do Amazon Bedrock **Claude Haiku 3**. Seguindo os mesmos passos a geração de imagem acima, foi criada uma função lambda para fazer a conexão com o Bedrock. Na imagem abaixo é possível ver a verificação e teste do funcionamento do modelo durante a criação da função lambda.

<p align="center">
    <img src="./evidencias/curso bedrock/prompt-text.png" alt="PromptRequest" width="400">
    <img src="./evidencias/curso bedrock/response-president.png" alt="PromptResponse" width="600">
</p>  

Assim como no projeto anterior com geração de imagens, foi criada uma API Gateway para expor a funcionalidade de sumarização. Após a criação da API, ela foi testada novamente com a utilização do Postman, dessa vez, pedindo a sumarização em duas linhas do texto enviado.


<p align="center">
    <img src="./evidencias/curso bedrock/postman-text.png" alt="PromptRequest" width="600">
</p>

 - Um outro ponto interessante foi a utilização do Amazon Titan Embed para implementar um serviço de embedding, também utilizando uma função Lambda para se conectar ao Amazon Bedrock. O processo foi testado diretamente na AWS Lambda, onde a função recebeu um texto de entrada e retornou com sucesso os vetores correspondentes aos embeddings gerados, como mostrado no log de teste.

 <p align="center">
    <img src="./evidencias/curso bedrock/embed.png" alt="PromptRequest" width="600">
</p>

 - **Além disso, foram desenvolvidos dois projetos utilizando modelos do Amazon Bedrock**: 
    - Um **chatbot**, na qual o backend era responsável por fazer a conexão com o amazon bedrock e o modelo em questão, lembrando que foi preciso realizar as configurações para conseguir utilizar os serviços da AWS na minha máquina local e o frontend foi feito com o streamlit. Segue abaixo a interface desse projeto com um exemplo de requisição.

<p align="center">
    <img src="./evidencias/curso bedrock/chabot.png" alt="Frontend" width="600">
</p> 

O segundo projeto, foi a criação de um site de **perguntas e respostas (Q&A)**, também utilizando o amazon bedrock no backend para conectar com os modelos desse serviço. O modelo que eu escolhi, diferentemente do professor, foi o usado anteriormente no curso para sumarização, o *Claude Haiku 3*. Nesse caso, a função do projeto era responder perguntas a partir de um documento PDF, ou do link dele como foi o caso do exemplo em questão. Através do PDF, é possível fazer perguntas e as respostas serão procuradas e baseadas nesse arquivo em questão. O fronted também foi criado usando o streamlit, abaixo é possível ver um exemplo de pergunta utilizando esse serviço criado.

<p align="center">
    <img src="./evidencias/curso bedrock/qa-front.png" alt="Frontend" width="600">
</p> 

### Credit Risk Modeling in Python
Neste curso, foram exploradas abordagens de negócios e machine learning para avaliação de risco de crédito, incluindo conceitos fundamentais como **Probabilidade de Inadimplência (PD)**, **Perda Dada a Inadimplência (LGD)** e **Exposição na Inadimplência (EAD)**.

- Um dos destaques foi a criação da variável alvo good_bad, que classifica os clientes em bons (1) ou maus pagadores (0), auxiliando na decisão de concessão de crédito.

<p align="center"> <img src="./evidencias/curso credit-risk/ev2.png" alt="good_bad" width="500"> </p>
Durante o pré-processamento, utilizamos a variável grade como exemplo, calculando sua proporção em relação à variável alvo.

<p align="center"> <img src="./evidencias/curso credit-risk/ev3.png" alt="proporcao_grade" width="400"> </p>

 - Além disso, foi calculado o Peso da Evidência (Weight of Evidence - WoE) para essa e outras variáveis do modelo, permitindo transformar dados categóricos em uma escala mais adequada para modelagem preditiva.

<p align="center"> <img src="./evidencias/curso credit-risk/ev4.png" alt="woe_grade" width="500"> </p>

- Por fim, foi gerado o gráfico de Peso da Evidência por Grade de Crédito, que demonstra a relação entre a qualidade da grade e o risco de inadimplência.

<p align="center"> <img src="./evidencias/curso credit-risk/ev1.png" alt="woe_por_grade" width="500"> </p>

A tendência crescente indica que quanto melhor a grade de crédito, maior o WoE, sugerindo menor risco de inadimplência. Já grades mais baixas (D, E, F, G) apresentam valores negativos, indicando maior risco. Isso é amplamente utilizado em modelos de Machine Learning e scorecards de crédito, pois o WoE transforma variáveis categóricas em uma escala contínua, facilitando a modelagem estatística e melhorando a interpretabilidade de modelos como Regressão Logística. Esse processo foi realizado posteriormente com todas as features do modelo (PD).


## 🏆 Certificados

Segue abaixo os certificados obtidos nos cursos da Sprint 07:

1. **Amazon Bedrock, Amazon Q & AWS Generative AI**
![Certificado 1](./certificados/Curso%20Amazon%20Bedrock.jpg)  

2. **Credit Risk Modeling in Python**
![Certificado 2](./certificados/Curso%20Risco%20de%20Credito.jpg)




