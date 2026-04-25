import json
import random

FILE_NAME = "game_stats.json"


def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {"wins": 0, "losses": 0}


def save_data(stats):

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(stats, file, indent=4)
        print("--- Дані успішно збережено! ---")

    except Exception as e:
        print(f"Помилка при збереженні: {e}")


def show_stats(stats):
    print("\n=== РЕЗУЛЬТАТИ ===")
    print(f"Перемог: {stats['wins']}")
    print(f"Програшів: {stats['losses']}")
    print("==================\n")


def play_game(stats):
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts_to_win = 5

    print("\nЯ загадав число від 1 до 100. Спробуй вгадати!")

    while True:
        try:
            user_answer = int(input("Твій варіант: "))
            attempts += 1

            if user_answer < number_to_guess:
                print("Загадане число БІЛЬШЕ.")

            elif user_answer > number_to_guess:
                print("Загадане число МЕНШЕ.")

            else:
                print(f"Вітаю! Ти вгадав число {number_to_guess} за {attempts} спроб.")

                if attempts < max_attempts_to_win:
                    print("Ти переміг користувача! (менше 5 спроб)")
                    stats['wins'] += 1

                else:
                    print("Комп'ютер переміг! (5 або більше спроб)")
                    stats['losses'] += 1

                break

        except ValueError:
            print("Будь ласка, введи ціле число.")


def main():
    stats = load_data()

    while True:
        print("--- МЕНЮ ГРИ ---")
        print("1. Почати нову гру")
        print("2. Вивести результат (статистику)")
        print("3. Зберегти дані у файл")
        print("4. Завантажити дані з файлу")
        print("5. Вихід")

        choice = input("Обери пункт меню: ")

        if choice == "1":
            play_game(stats)
        elif choice == "2":
            show_stats(stats)
        elif choice == "3":
            save_data(stats)
        elif choice == "4":
            stats = load_data()
            print("--- Дані завантажено! ---")
        elif choice == "5":
            print("Дякую за гру! До побачення.")
            break
        else:
            print("Неправильний вибір, спробуй ще раз.")

if __name__ == "__main__":
    main()