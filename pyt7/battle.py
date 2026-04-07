import ex0


def test_factory(factory: ex0.CreatureFactory) -> None:
    print("\nTesting factory")

    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def make_base_creatures_fight(
    first_factory: ex0.CreatureFactory,
    second_factory: ex0.CreatureFactory,
) -> None:
    print("\nTesting battle")

    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()

    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())
    print("fight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    flame = ex0.FlameFactory()
    aqua = ex0.AquaFactory()

    test_factory(flame)
    test_factory(aqua)
    make_base_creatures_fight(flame, aqua)


if __name__ == "__main__":
    main()
