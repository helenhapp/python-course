def ask(question):
    answer = input(question + "\n").strip().upper()
    return answer


def percent(part, total):
    result = part * 100 / total
    return round(result, 2)


quiz = {
    "Яке має бути наступне число: 1, 1, 2, 3, 5, 8, ...?": "13",
    "Яке число пропущене: 1, 4, 9, 16, __, 36?": "25",
    "Яке наступне число: 2, 4, 8, 16, 32, ...?": "64",
    "Яка літера наступна: П, В, С, Ч, П, С, ...?": "Н",
    "Яке наступне число: 10, 9, 7, 4, 0, ...?": "-5",
}

n = len(quiz)

print("== Вікторина ==")
print(f"Дайте відповідь на {n} питань:\n")

c = 0
for q, a in quiz.items():
    answer = ask(q)

    if answer == a:
        print("Правильно!\n")
        c += 1
    else:
        print(f"Неправильно! Правильна відповідь: {a}\n")

print(f"Ви відповіли правильно на {c}/{n} питань. Це {percent(c, n)}%!")
