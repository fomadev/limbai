# api/main.py
from fastapi import FastAPI
from core.translator import TranslatorManager

app = FastAPI(title="LIMBAI API v1.0.0")
limbai = TranslatorManager()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API LIMBAI - Le moteur est prêt"}

@app.get("/translate")
def translate_text(text: str, source: str, target: str):
    """
    Endpoint pour traduire du texte.
    Exemple: /translate?text=nzo&source=kikongo&target=lingala
    """
    result = limbai.translate(text, source, target)
    return result