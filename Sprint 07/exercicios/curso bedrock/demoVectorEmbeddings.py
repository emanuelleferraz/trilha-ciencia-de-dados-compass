import json
import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")

model_id = "amazon.titan-embed-text-v2:0"

input_text = "Hi, what is the cost of one apple?"

native_request = {"inputText": input_text}

# Converter para JSON
request = json.dumps(native_request)

# Adicionar contentType
response = client.invoke_model(
    modelId=model_id,
    body=request,
    contentType="application/json"
)

# Ler e processar resposta
model_response = json.loads(response["body"].read())

embedding = model_response["embedding"]
input_token_count = model_response["inputTextTokenCount"]

print("\nYour input: ")
print(input_text)

print(f"Number of input tokens: {input_token_count}")
print(f"Size of the generated embedding: {len(embedding)}")
print("Embedding: ")
print(embedding)

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from Lambda!"
    }