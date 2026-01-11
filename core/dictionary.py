# core/dictionary.py

class LimbaiDictionary:
    def __init__(self):
        # Cette base sera plus tard chargée depuis les fichiers JSON dans /data
        self.registry = {
            "kikongo": {
                "mboté na beno": {
                    "lingala": "mboté na bino",
                    "francais": "bonjour à tous",
                    "note": "Forme plurielle respectueuse"
                },
                "nzo": {
                    "lingala": "ndako",
                    "francais": "maison",
                    "note": "Terme générique"
                }
            }
        }

    def find_exact_match(self, word, source_lang, target_lang):
        """Cherche une expression précise dans notre base artisanale."""
        lang_data = self.registry.get(source_lang.lower())
        if lang_data and word.lower() in lang_data:
            return lang_data[word.lower()].get(target_lang.lower())
        return None