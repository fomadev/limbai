# core/models_loader.py
import whisper
import torch
import os

class ModelsLoader:
    def __init__(self):
        # On choisit le modèle 'base' pour la v1.0.0 
        # (Léger et rapide, idéal pour commencer)
        self.model_name = "base"
        self.stt_model = None

    def load_whisper(self):
        """Charge le modèle Whisper pour la transcription Audio -> Texte"""
        print(f"--- LIMBAI : Chargement du modèle vocal ({self.model_name})... ---")
        
        # Vérifie si on a une carte graphique (GPU) sinon utilise le processeur (CPU)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Chargement du modèle
        self.stt_model = whisper.load_model(self.model_name, device=device)
        print("--- LIMBAI : Oreille activée (Modèle prêt) ---")
        return self.stt_model

# Instance unique pour ne pas recharger le modèle à chaque fois
loader = ModelsLoader()