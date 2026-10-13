import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=500,
    messages=[{"role": "user", "content": "Explain Value at Risk in two sentences."}],
)

print(message.content[0].text)