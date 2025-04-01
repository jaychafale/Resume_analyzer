import google.generativeai as genai
genai.configure(api_key="AIzaSyBLyDQWmYrnKZnyHbJzs_rYNEhr9Lp4jI0")

models = genai.list_models()
for m in models:
    print(m.name, m.supported_generation_methods)
