print("=== Import Transmutation Mastery ===")

# Method 1 - Full module import
import alchemy.elements
print("Method 1 - Full module import:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

# Method 2 - Specific function import
from alchemy.elements import create_water
print("\nMethod 2 - Specific function import:")
print(f"create_water(): {create_water()}")

# Method 3 - Aliased import
from alchemy.potions import healing_potion as heal
print("\nMethod 3 - Aliased import:")
print(f"heal(): {heal()}")

# Method 4 - Multiple imports
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion
print("\nMethod 4 - Multiple imports:")
print(f"create_earth(): {create_earth()}")
print(f"create_fire(): {create_fire()}")
print(f"strength_potion(): {strength_potion()}")

print("\nAll import transmutation methods mastered!")