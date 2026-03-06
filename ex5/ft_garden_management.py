class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = {}

    def add_plant(self, name: str) -> None:
        try:
            "" + name
        except TypeError:
            raise TypeError(f"Invalid plant name: {name}")
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {"water": 5, "sun": 8}

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for name in self.plants:
                print(f"Watering {name} - success")
        except Exception as e:
            print(f"Error during watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str, water: int, sun: int) -> None:
        try:
            "" + name
        except TypeError:
            raise TypeError(f"Invalid plant name: {name}")
        if not name:
            raise PlantError(f"Plant '{name}' not found in garden")
        if water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        if water < 1:
            raise WaterError(f"Water level {water} is too low (min 1)")
        if sun > 12:
            raise ValueError(f"Sunlight hours {sun} is too high (max 12)")
        if sun < 2:
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    print("Adding plants to garden...")
    for plant in ["tomato", "lettuce", ""]:
        try:
            manager.add_plant(plant)
            print(f"Added {plant} successfully")
        except (PlantError, TypeError) as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        manager.water_plants()
    except Exception as e:
        print(f"Unexpected watering error: {e}")

    print("\nChecking plant health...")
    checks = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
    ]
    for name, water, sun in checks:
        try:
            manager.check_plant_health(name, water, sun)
        except (TypeError, ValueError, PlantError, WaterError) as e:
            print(f"Error checking {name}: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    try:
        test_garden_management()
    except Exception as e:
        print(f"Error: {e}")
