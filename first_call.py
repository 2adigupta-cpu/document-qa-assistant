import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-fable-5-1",
    max_tokens=300,
    messages=[{"role": "user", "content": "Explain Value at Risk in two sentences."}],
)

print(message.content[0].text)
