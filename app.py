import os
llm_url = os.getenv('LLM_URL', 'default_value_if_not_set')
print(llm_url)
