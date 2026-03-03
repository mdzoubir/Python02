class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred.") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The plant has a problem.") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "There is a watering problem.") -> None:
        super().__init__(message)


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_catch_all_garden_errors() -> None:
    print("\nTesting catching all garden errors...")
    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]
    for err in errors:
        try:
            raise err
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error()
    test_water_error()
    test_catch_all_garden_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    try:
        test_custom_errors()
    except Exception as e:
        print(f"Error: {e}")
