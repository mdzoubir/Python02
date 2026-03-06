def garden_operations(error: object) -> None:

    if error is ValueError:
        int("abc")
    if error is ZeroDivisionError:
        10 / 0
    if error is FileNotFoundError:
        f = open("missing.txt", "r")
        f.close()
    if error is KeyError:
        plants = {"plant": "rose", "age": 45}
        plants['missing_plant']


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        garden_operations(ValueError)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        garden_operations(ZeroDivisionError)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFound...")
        garden_operations(FileNotFoundError)
    except FileNotFoundError:
        print("Caught FileNotFound: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        garden_operations(KeyError)
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    try:
        print("Testing multiple errors together...")
        garden_operations(ValueError)
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print(f"Error: {e}")
