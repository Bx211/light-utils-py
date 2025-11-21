import re
import unicodedata




def slugify(text: str) -> str:
text = text.lower()
text = unicodedata.normalize("NFKD", text)
text = re.sub(r"[^a-z0-9]+", "-", text)
return text.strip("-")




def clean_text(text: str) -> str:
return re.sub(r"[^a-zA-Z0-9 ]+", "", text)
