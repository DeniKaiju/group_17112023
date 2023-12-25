def calculate_distance(**kwargs):
    try:
        time = kwargs['time']
        speed = kwargs['speed']
        weight = kwargs['weight']

        if time < 0 or speed < 0 or weight < 0:
            raise ValueError("Час, швидкість та вага повинні бути не менше 0")

        distance = time * speed
        return f"Транспортний засіб вагою {weight} кг рухався {time} секунд зі швидкістю {speed} м/сек, і подолав відстань {distance} метрів"
    except KeyError as e:
        raise ValueError(f"Помилка: Бракує обов'язкового аргументу: {e}")


def test_calculate_distance_positive():
    result = calculate_distance(time=10, speed=3, weight=1000)
    expected = "Транспортний засіб вагою 1000 кг рухався 10 секунд зі швидкістю 3 м/сек, і подолав відстань 30 метрів"
    assert result == expected, f"Отримано: {result}, Очікувано: {expected}"


def test_calculate_distance_negative_time():
    try:
        calculate_distance(time=-5, speed=5, weight=500)
        assert False, "Очікувалася помилка ValueError"
    except ValueError as e:
        assert str(e) == "Час, швидкість та вага повинні бути не менше 0", f"Отримано: {e}"


def test_calculate_distance_missing_weight():
    try:
        calculate_distance(time=5, speed=5)
        assert False, "Очікувалася помилка ValueError"
    except ValueError as e:
        assert str(e) == "Помилка: Бракує обов'язкового аргументу: 'weight'", f"Отримано: {e}"


def test_calculate_distance_another_positive():
    result = calculate_distance(time=8, speed=2, weight=750)
    expected = "Транспортний засіб вагою 750 кг рухався 8 секунд зі швидкістю 2 м/сек, і подолав відстань 16 метрів"
    assert result == expected, f"Отримано: {result}, Очікувано: {expected}"


def run_tests():
    try:
        test_calculate_distance_positive()
        test_calculate_distance_negative_time()
        test_calculate_distance_missing_weight()
        test_calculate_distance_another_positive()
        print("Усі тести пройдено успішно.")
    except AssertionError as e:
        print(f"Тест провалився: {e}")
    except ValueError as ve:
        print(f"Тест провалився: {ve}")
