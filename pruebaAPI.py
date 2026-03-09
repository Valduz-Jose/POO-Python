import google.generativeai as genai

# PEGA AQUÍ LA LLAVE NUEVA
NUEVA_KEY = "TU_NUEVA_API_KEY_AQUI"

genai.configure(api_key=NUEVA_KEY)

try:
    print("Verificando modelos disponibles...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Modelo encontrado: {m.name}")
except Exception as e:
    print(f"❌ Error todavía: {e}")