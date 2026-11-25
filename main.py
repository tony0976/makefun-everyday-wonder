"""Writes one sentence that makes a small everyday moment strange and new."""
import os

TEXT = "The lift door opened on a stranger humming my favourite song, and for three floors the building felt less like concrete and more like a radio left on in another room."

# Rule: the wonder line must be a single sentence of at most 200 characters.
assert "\n" not in TEXT and TEXT.count(".") == 1 and TEXT.endswith(".") and len(TEXT) <= 200, f"entry must be one sentence, <=200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
