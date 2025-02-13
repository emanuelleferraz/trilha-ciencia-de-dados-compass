import json
import boto3
import base64
import datetime

# Criando a conexão com o bedrock-s3 com o boto3
client_bedrock = boto3.client('bedrock-runtime')
client_s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Criando o prompt (para consultas futuras (DADOS))
    input_prompt = event['prompt'] # key -> prompt
    print(input_prompt)

    # Criando a sintaxe (Request) para acessar a API do Bedrock
    body = {
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {
        "text": input_prompt,
        "negativeText": "none"  
    },
    "imageGenerationConfig": {
        "quality": "standard",  
        "numberOfImages": 1,  
        "height": 512,  
        "width": 512,  
        "cfgScale": 10.0, 
        "seed": 0  
    }
}

    response_bedrock = client_bedrock.invoke_model(contentType='application/json', accept='application/json', modelId='amazon.titan-image-generator-v2:0',
       body=json.dumps(body))

    # Recuperando a resposta em formato dicionário e convertendo para byte
    response_bedrock_byte=json.loads(response_bedrock['body'].read())
    print(response_bedrock_byte)

    # Convertendo para Base64 e depois para byte
    response_bedrock_base64 = response_bedrock_byte['images'][0]
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)
    print(response_bedrock_finalimage)

    # Salvando a imagem no S3
    poster_name = 'posterName'+ datetime.datetime.today().strftime('%Y-%M-%D-%M-%S')
    
    response_s3=client_s3.put_object(
        Bucket='movieposter-bedrock-sprint07',
        Body=response_bedrock_finalimage,
        Key=poster_name)

    # Pre-Signed
    generate_presigned_url = client_s3.generate_presigned_url('get_object', Params={'Bucket':'movieposter-bedrock-sprint07','Key':poster_name}, ExpiresIn=3600)
    print(generate_presigned_url)

    return {
        'statusCode': 200,
        'body': generate_presigned_url
    }
