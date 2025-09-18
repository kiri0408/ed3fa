from openai import AzureOpenAI

azure_endpoint = ""
api_key = ""
api_version = "2025-01-01-preview"
model = "gpt-5-chat"

client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version=api_version,
)

messages = [ {"role": "user", "content": "日本で一番高い山は何？"} ]

response = client.chat.completions.create(
    messages=messages,
    model=model
)

print(response.choices[0].message.content)


