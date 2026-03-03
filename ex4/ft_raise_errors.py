def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> str:
    try:
        "" + plant_name
    except TypeError:
        raise ValueError(f"Invalid plant name: {plant_name!r}")
    try:
        water_level = int(water_level)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid water level: {water_level!r}")
    try:
        sunlight_hours = int(sunlight_hours)

    except (ValueError, TypeError):
        raise ValueError(f"Invalid sunlight hours: {sunlight_hours!r}")
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 12, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    try:
        test_plant_checks()
    except Exception as e:
        print(f"Error: {e}")
