import sys


def main() -> None:
    grade = int(input("Введите оценку (от 2 до 5): "))

    match grade:
        case 2:
            print("неудовлетворительно")
        case 3:
            print("удовлетворительно")
        case 4:
            print("хорошо")
        case 5:
            print("отлично")
        case _:
            print("Ошибка: оценка должна быть от 2 до 5", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()