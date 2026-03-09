# # # # CHATBOT Analizador de Sentimientos
# # # from textblob import TextBlob

# # # class AnalizadorDeSentimientos:
# # #   def analizar_sentimiento(self, texto):
# # #     analisis = TextBlob(texto)
# # #     if analisis.sentiment.polarity > 0:
# # #       return "Positivo"
# # #     elif analisis.sentiment.polarity == 0:
# # #       return "Neutral"
# # #     else:
# # #       return "Negativo"
    
# # # analizador = AnalizadorDeSentimientos()
# # # resultado = analizador.analizar_sentimiento("this is funny, but is not my interesting")
# # # print(resultado)
# # import openai

# # 

# # system_rol = '''Has de cuenta de que eres un analizador de sentimientos
# # yo te pasare un texto y tu me diras si es positivo, negativo o neutro
# # debes analizar el sentimiento en el texto y devolver un caracter solo respuestas numericas
# # donde -1 es negativo, 0 es neutro y 1 es positivo (solo puedes responder con ints o floats)''' 

# # mensajes = [{"role": "system", "content": system_rol}]
# # class AnalizadorDeSentimientos:
# #   def analizar_sentimiento(self, polaridad):
# #     if polaridad > -0.6 and polaridad <=-0.3:
# #       return "\x1b[1;31m" + "Negativo"
    
# #     elif polaridad > -0.3 and polaridad <-0.1:
# #       return "\x1b[1;31m" + "Algo Negativo"
    
# #     elif polaridad >= -0.1 and polaridad <=0.1:
# #       return "\x1b[1;33m" + "Neutral"
    
# #     elif polaridad >= 0.1 and polaridad <=0.4:
# #       return "\x1b[1;32m" + "Algo Positivo"
    
# #     elif polaridad >= 0.4 and polaridad <=0.9:
# #       return "\x1b[1;32m" + "Positivo"
    
# #     elif polaridad >0.9:
# #       return "\x1b[1;32m" + "Muy Positivo"
    
# #     else:
# #       return "\x1b[1;31m" + "Muy Negativo"
    


# # analizador = AnalizadorDeSentimientos()
# # # resultado = analizador.analizar_sentimiento(0.2)
# # # print(resultado)

# # while True:
# #   user_prompt = input("\x1b[1;33m" + "Introduce un texto para analizar su sentimiento: "+"\x1b[0;37m")
# #   mensajes.append({"role": "user", "content": user_prompt})
# #   completion = openai.ChatCompletion().create(
# #     model="gpt-3.5-turbo",
# #     messages=mensajes,
# #     max_tokens=8
# #   )
# #   respuesta = completion.choices[0].message.content
# #   mensajes.append({"role": "assistant", "content": respuesta})
  
# #   sentimiento = analizador.analizar_sentimiento(float(respuesta))
# #   print(sentimiento)
  
  
# import openai
# from openai import OpenAI

# # 1. Nueva forma de inicializar el cliente
# 

# system_rol = '''Eres un analizador de sentimientos.
# Yo te pasaré un texto y tú me dirás si es positivo, negativo o neutro.
# Debes devolver SOLO un número:
# -1 si es negativo, 0 si es neutro, 1 si es positivo.
# (Puedes usar decimales entre -1 y 1 si el sentimiento no es extremo).''' 

# mensajes = [{"role": "system", "content": system_rol}]

# class AnalizadorDeSentimientos:
#     def analizar_sentimiento(self, polaridad):
#         # Lógica de colores corregida para evitar solapamientos
#         if polaridad <= -0.6:
#             return "\x1b[1;31m" + "Muy Negativo"
#         elif -0.6 < polaridad <= -0.1:
#             return "\x1b[1;31m" + "Negativo"
#         elif -0.1 < polaridad < 0.1:
#             return "\x1b[1;33m" + "Neutral"
#         elif 0.1 <= polaridad <= 0.6:
#             return "\x1b[1;32m" + "Positivo"
#         else:
#             return "\x1b[1;32m" + "Muy Positivo"

# analizador = AnalizadorDeSentimientos()

# while True:
#     user_prompt = input("\n\x1b[1;33m" + "Introduce un texto para analizar: " + "\x1b[0;37m")
#     if user_prompt.lower() in ["salir", "exit"]:
#         break
        
#     mensajes.append({"role": "user", "content": user_prompt})
    
#     # 2. Nueva sintaxis para crear la respuesta
#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=mensajes,
#         max_tokens=5
#     )
    
#     # 3. Nueva forma de acceder al contenido
#     respuesta = completion.choices[0].message.content.strip()
    
#     try:
#         sentimiento_num = float(respuesta)
#         resultado_final = analizador.analizar_sentimiento(sentimiento_num)
#         print(f"Puntaje IA: {respuesta} -> {resultado_final}\x1b[0m")
#     except ValueError:
#         print("La IA no devolvió un número válido. Respuesta:", respuesta)
import google.generativeai as genai

# 1. Tu API Key
MI_API_KEY = "ApiKey"

# Configuración de seguridad para que la IA no bloquee frases negativas
seguridad = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

genai.configure(api_key=MI_API_KEY)

class AnalizadorDeSentimientos:
    def __init__(self):
        # Usamos el modelo 1.5-flash con la librería clásica
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={"temperature": 0.1},
            safety_settings=seguridad
        )

    def obtener_polaridad(self, texto_usuario):
        prompt = f"Analiza el sentimiento de este texto y responde SOLO con un numero entre -1.0 y 1.0: '{texto_usuario}'"
        try:
            response = self.model.generate_content(prompt)
            # El strip() es vital para limpiar la respuesta
            res_texto = response.text.strip()
            return float(res_texto)
        except Exception as e:
            print(f"\x1b[1;31mError: {e}\x1b[0m")
            return 0.0

    def formatear_resultado(self, valor):
        if valor <= -0.6: return "\x1b[1;31mVery Negative"
        elif -0.6 < valor <= -0.1: return "\x1b[1;31mNegative"
        elif -0.1 < valor < 0.1: return "\x1b[1;33mNeutral"
        elif 0.1 <= valor <= 0.6: return "\x1b[1;32mPositive"
        else: return "\x1b[1;32mVery Positive"

# --- Lógica principal ---
analizador = AnalizadorDeSentimientos()
print("\x1b[1;36m=== ANALIZADOR DE SENTIMIENTOS (FINAL FIX) ===\x1b[0m")

while True:
    entrada = input("\nTexto: ")
    if entrada.lower() in ["salir", "exit"]: break
    
    puntuacion = analizador.obtener_polaridad(entrada)
    print(f"IA Score: {puntuacion} -> {analizador.formatear_resultado(puntuacion)}\x1b[0m")