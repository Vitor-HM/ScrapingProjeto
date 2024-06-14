from deep_translator import GoogleTranslator

# Texto em português
texto_portugues = "Olá, mundo! Como você está?"

# Traduz para o inglês
traducao = GoogleTranslator(source='pt', target='en').translate(texto_portugues)

# Exibe a tradução
print("Texto original:", texto_portugues)
print("Tradução para o inglês:", traducao)