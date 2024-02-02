import random

from brain_games.cli import welcome_user

print("brain-prime\n")
name = welcome_user()


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    score = 0  # Инициализация счетчика
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while True:
        num = random.randint(1, 2)
        user_answer = input(f'''Question: {num}
Your answer: ''')
        if (is_prime(num) and user_answer.lower() == 'yes') or \
                (not is_prime(num) and user_answer.lower() == 'no'):
            score += 1
            print("Correct!")
            if score >= 3:  # Проверка, достигли ли мы трех правильных ответов
                print(f'Congratulations, {name}!')
                break
        elif is_prime(num) and user_answer.lower() == 'no':
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif not is_prime(num) and user_answer.lower() == 'yes':
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    main()
