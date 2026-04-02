def validate_ingredients(ingredients: str) -> str:
    # Check if any of the valid elements are in the ingredients string
    valid_elements = ["fire", "water", "earth", "air"]
    
    for element in valid_elements:
        if element in ingredients.lower():
            return f"{ingredients} - VALID"
            
    return f"{ingredients} - INVALID"