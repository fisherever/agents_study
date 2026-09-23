import os

import anthropic
from dotenv import load_dotenv

load_dotenv() # load the .env in home path

client = anthropic.Anthropic(
	base_url=os.environ["LLM_BASE_URL"],
	api_key=os.environ["LLM_API_KEY"],
)
model = os.environ["LLM_MODEL"]

response = client.messages.create(
	model=model,
	max_tokens=256,
	messages=[
		{"role": "user", "content": "用一句话解释什么是 agent loop. "}
	],
)

print("content:", response.content)
print("stop_reason:", response.stop_reason)
print("usage:", response.usage)
