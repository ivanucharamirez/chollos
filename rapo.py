import requests
import json
import time
import os

# --- CONFIGURACIÓN ---
PPLX_KEY = "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"
AMAZON_TAG = "sarahtonin-21"
TELEGRAM_TOKEN = "8471082126:AAHMuHTA5MKSvn6NQGPXMF5Jhteky7lxT9o"
TELEGRAM_CHAT_ID = "1400741639"

def crear_web(contenido_html):
    plantilla = f"""
    <html><head><meta charset='UTF-8'><title>Chollos Ivan</title></head>
    <body style='font-family:sans-serif; padding:20px;'>
    <h1>🔥 Ofertas Amazon España</h1>
    <div>{contenido_html.replace('\n', '<br>')}</div>
    <p>Actualizado: {time.ctime()}</p>
    </body></html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(plantilla)
    print("✅ ARCHIVO index.html CREADO CON ÉXITO EN TU CARPETA.")

def trabajar():
    print("🔍 Investigando en Amazon... (Espera 60 segundos)")
    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": "Bearer " + PPLX_KEY, "Content-Type": "application/json"}
    prompt = ("Busca 3 ofertas reales de Amazon España hoy 30 de diciembre. "
              "Dame links reales con mi tag {0}.".format(AMAZON_TAG))
    try:
        r = requests.post(url, headers=headers, json={"model": "sonar-pro", "messages": [{"role": "user", "content": prompt}]}, timeout=90)
        res = r.json()['choices'][0]['message']['content']
        crear_web(res)
        return res
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        post = trabajar()
        time.sleep(3600)
