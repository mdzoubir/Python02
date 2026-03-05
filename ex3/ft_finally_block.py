def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant == "":
                raise TypeError("Plant name cannot be empty")
            try:
                "" + plant
            except TypeError:
                raise TypeError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    try:
        test_watering_system()
    except Exception as e:
        print(f"Error: {e}")
