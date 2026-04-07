import ex0
import ex1
import ex2


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("* \nBattle *")
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
            except ex2.InvalidStrategyCreatureError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main():
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()
    healing_factory = ex1.HealingCreatureFactory()
    transform_factory = ex1.TransformCreatureFactory()

    normal_strategy = ex2.NormalStrategy()
    aggressive_strategy = ex2.AggressiveStrategy()
    defensive_strategy = ex2.DefensiveStrategy()

    print("\nTournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents0 = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ]
    battle(opponents0)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents1 = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ]
    battle(opponents1)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents2 = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy),
    ]
    battle(opponents2)


if __name__ == "__main__":
    main()