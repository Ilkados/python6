import ex2
import ex0
import ex1
def main():
    flame_factory = ex0.FlameFactory()
    healing_factory = ex1.HealingCreatureFactory()
    normal_strategy =  ex2.NormalStrategy()
    defensive_strategy =ex2.DefensiveStrategy()
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")