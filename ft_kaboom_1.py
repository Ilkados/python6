print("=== Kaboom 1 ===")
print("This will crash with an ImportError due to Circular Dependency!")
from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402, F401
