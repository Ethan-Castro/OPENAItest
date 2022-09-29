import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Create an outline for an essay about Nikola Tesla and his contributions to technology:",
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
