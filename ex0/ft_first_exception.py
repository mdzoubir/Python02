def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except (ValueError, TypeError):
        raise ValueError(f"'{temp_str}' is not a valid number")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for t in tests:
        print(f"Testing temperature: {t}")
        try:
            temp = check_temperature(t)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as e:
            print(f"Error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(f"Error: {e}")
