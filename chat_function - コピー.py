from openai import AzureOpenAI

# Azure OpenAIの設定
azure_endpoint = ""
api_key = ""
api_version = "2025-01-01-preview"
model = "gpt-5-chat"

client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version=api_version,
)



def simple_chat(question: str) -> str:
    """質問を受けてAzure OpenAIのチャットモデルから回答を取得する関数"""
    messages = [{"role": "user", "content": question}]
    response = client.chat.completions.create(
        messages=messages,
        model=model
    )
    answer = response.choices[0].message.content
    return answer



if __name__ == "__main__":
    question = "日本で一番高い山は？"
    answer = simple_chat(question)
    print("Answer:", answer)
