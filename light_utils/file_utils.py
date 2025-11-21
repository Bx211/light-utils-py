import json
from typing import Any




def read_json_safe(path: str) -> Any:
try:
with open(path, "r", encoding="utf-8") as f:
return json.load(f)
except Exception:
return None




def write_json(path: str, data: Any) -> None:
with open(path, "w", encoding="utf-8") as f:
json.dump(data, f, indent=4, ensure_ascii=False)
