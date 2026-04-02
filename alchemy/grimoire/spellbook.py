def record_spell(spell_name: str, ingredients: str) -> str:
    # LATE IMPORT: We import the validator inside the function!
    # This prevents the circular curse because Python only reads this 
    # when the function is actually called, not when the file first opens.
    from .validator import validate_ingredients
    
    validation_result = validate_ingredients(ingredients)
    
    if "VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell rejected: {spell_name} ({validation_result})" 