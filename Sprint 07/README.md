# 📊 Entrega - Sprint 07

Nessa Sprint 07, a trilha foi dividida entre 2 cursos, sendo eles: **Amazon Bedrock, Amazon Q & AWS Generative AI [HANDS-ON]** e **Credit Risk Modeling in Python**.

## Link do Vídeo


---

# 📝 Exercícios

### Amazon Bedrock, Amazon Q & AWS Generative AI
Durante o curso, não foram realizados diretamente exercícios, dessa forma, achei interessante fazer o upload das funções criadas nas aulas. Segue abaixo os arquivos divididos pela seção do curso:
1. **Amazon Bedrock**:

    ➡️ Confira o arquivo da [função lambda para gerar imagens](./exercicios/curso%20bedrock/moviePosterDesign.py).


### Credit Risk Modeling in Python




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

- Posteriormente, foi criada uma *API Gateway*, que comunicava com a função lambda criada acima, e através da criação do *method* e o deploy dela, também foi possível gerar imagens por meio de requisições no *prompt*, como é mostrado abaixo:

<p align="center">
    <img src="./evidencias/curso bedrock/prompt-api.png" alt="PromptRequest" width="500">
    <img src="./evidencias/curso bedrock/movie-poster.png" alt="moviePoster" width="400">
</p>

- Por último, foi utilizado o [Postman](https://www.postman.com/company/about-postman/) para testar se a API construída funcionava em outros ambientes, e através do método *GET*, na caixa de *values* que foi utilizada como um prompt se comparado com as outras formas mostradas acima, foi possível gerar a imagem pedida na descrição. Lembrando que indepentende do ambiente ou forma, a imagem gerada é armazenada no S3.

<p align="center">
    <img src="./evidencias/curso bedrock/postman.png" alt="PromptRequest" width="500">
    <img src="./evidencias/curso bedrock/helicpt.png" alt="moviePoster" width="400">
</p>


## 🏆 Certificados

Segue abaixo os certificados obtidos nos cursos da Sprint 07:




