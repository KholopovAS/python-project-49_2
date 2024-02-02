import random

from brain_games.cli import welcome_user

print("brain-progression\n")
name = welcome_user()


def generate_progression():
    # Генерируем длину от 5 до 15
    length = random.randrange(5, 16)
    # Выбираем случайную позицию для скрытого числа
    hidden_index = random.randrange(length)
    # Генерируем начальное значение
    start = random.randrange(1, 100)
    # Генерируем общую разницу
    diff = random.randrange(1, 10)
    # Генерируем прогрессию
    progression = [start + i * diff for i in range(length)]
    # Заменяем скрытое число на две точки
    progression[hidden_index] = ".."
    # Возвращаем прогрессию и скрытое число
    return (progression, progression[hidden_index]
            == "..", start + diff * hidden_index)


def main():
    score = 0  # Инициализация счетчика
    print("What number is missing in the progression?")
    while True:
        progression, is_hidden, correct_answer = generate_progression()
        print("Question:", end=' ')
        print(" ".join(map(str, progression)))
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
            score += 1  # Увеличение счетчика
            if score >= 3:  # Проверка, достигли ли мы трех правильных ответов
                print(f'Congratulations, {name}!')
                break
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    main()
