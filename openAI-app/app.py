import openai

openai.api_key = "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"

def BasicGeneration(userPrompt):
    completion = openai.Completion.create(
        model = "gpt-3.5-turbo",
        messages = [ {"role" : "user", "content" : userPrompt} ]
    )
    return completion.choices[0].messages.content

prompt = "explain the concept of a diamond pattern"

response = BasicGeneration(prompt)
print(response)