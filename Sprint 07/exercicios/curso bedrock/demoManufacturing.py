import json
import boto3

client_bedrock = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    # Criando o prompt para requisições
    input_prompt = event['prompt']
    print(input_prompt)

    # Criando o body da requisição
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [
            {"role": "user", "content": input_prompt}
        ],
        "temperature": 0.9,
        "top_p": 0.9,
        "max_tokens": 200,  
        "stop_sequences": []
    }

    # Criando a sintaxe para a requisição
    client_bedrockrequest = client_bedrock.invoke_model(
        contentType='application/json',
        accept='application/json',
        modelId='anthropic.claude-3-haiku-20240307-v1:0',
        body=json.dumps(body)
    )

    # print(client_bedrockrequest)

    # Fazendo a conversão da resposta para string
    client_bedrock_byte = client_bedrockrequest['body'].read()
    client_bedrock_string = json.loads(client_bedrock_byte)
    client_final_response = client_bedrock_string['content'][0]['text']

    print(client_final_response)

    return {
        'statusCode': 200,
        'body': json.dumps(client_final_response)
    }
