from maxmin import max_min_select

def main():
    try:
        numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
        max_value, min_value = max_min_select(numbers)
        print(f"Maximum value: {max_value}")
        print(f"Minimum value: {min_value}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()