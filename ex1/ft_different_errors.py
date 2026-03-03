def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        f = open("missing.txt")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden = {"tomato": 5}
        _ = garden["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("\nTesting multiple errors together...")
    try:
        int("bad")
        _ = 1 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print(f"Error: {e}")
