# core/translator.py
from core.dictionary import LimbaiDictionary

class TranslatorManager:
    def __init__(self):
        # On initialise notre dictionnaire local
        self.local_dict = LimbaiDictionary()
        
        # Note : Dans la v1.1.0, nous chargerons ici le modèle NLLB 
        # pour la traduction automatique. Pour la v1.0.0, on prépare la structure.
        self.ai_model_ready = False 

    def translate(self, text, source_lang, target_lang):
        """
        Logique hybride : 
        1. Chercher dans le dictionnaire de précision (Village).
        2. Si non trouvé, utiliser l'IA générique.
        """
        text_clean = text.lower().strip()

        # ÉTAPE 1 : Recherche dans le dictionnaire "Vérité"
        result = self.local_dict.find_exact_match(text_clean, source_lang, target_lang)
        
        if result:
            return {
                "status": "success",
                "translated_text": result,
                "method": "Limbai-Village-Core", # On identifie que c'est notre savoir
                "accuracy": "High"
            }

        # ÉTAPE 2 : Si non trouvé, on bascule sur la logique IA
        return self._translate_with_ai(text_clean, source_lang, target_lang)

    def _translate_with_ai(self, text, source_lang, target_lang):
        """Ici on appellera les modèles comme Meta NLLB ou SeamlessM4T."""
        # Simulation pour la v1.0.0 avant chargement des gros modèles
        return {
            "status": "partial",
            "translated_text": f"Traduction automatique de '{text}' en cours...",
            "method": "AI-Generic",
            "accuracy": "Medium"
        }