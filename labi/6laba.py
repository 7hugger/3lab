#Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной форме. Обязательное требование – минимизация времени выполнения и объема памяти.
#F(x<2) = 3; F(n) = (-1)n*(F(n-1)/n! + F(n-5) /(2n)!)
import timeit
import math
# Рекурсивная функция
def F_recursive(n):
    if n < 2:
        return 3
    factorial_n = math.factorial(n)
    factorial_2n = math.factorial(2 * n)
    sign = -1 if n % 2 else 1
    return sign * ((F_recursive(n - 1) / factorial_n) + (F_recursive(n - 5) / factorial_2n))
# Итерационная функция
def F_iterative(n):
    if n < 2:
        return 3
    f0 = f1 = f2 = f3 = f4 = 3
    factorial_i = 1
    factorial_2i = 2
    for i in range(2, n + 1):
        factorial_i *= i
        factorial_2i *= (2 * i - 1) * (2 * i)
        sign = -1 if i % 2 else 1
        fi = sign * ((f4 / factorial_i) + (f0 / factorial_2i))
        f0, f1, f2, f3, f4 = f1, f2, f3, f4, fi
    return f4
# Сравнение методов
def compare_methods(max_n):
    recursive_times = []
    iterative_times = []
    results = []
    for n in range(max_n + 1):
        recursive_timer = timeit.Timer(lambda: F_recursive(n))
        recursive_time = recursive_timer.timeit(number=1)
        recursive_times.append(recursive_time)
        iterative_timer = timeit.Timer(lambda: F_iterative(n))
        iterative_time = iterative_timer.timeit(number=1)
        iterative_times.append(iterative_time)
        recursive_result = F_recursive(n)
        iterative_result = F_iterative(n)
        results.append((n, recursive_result, iterative_result))
    return recursive_times, iterative_times, results
def main():
    max_n = 20
    recursive_times, iterative_times, results = compare_methods(max_n)
    print("Таблица результатов:")
    print("n | Рекурсивное | Итеративное | Время рекурсии (с) | Время итерации (с)")
    print("-" * 80)
    for n, recursive_result, iterative_result in results:
        print(f"{n:>3} | {recursive_result:.6e} | {iterative_result:.6e} | {recursive_times[n]:.6f} | {iterative_times[n]:.6f}")
if __name__ == "__main__":
    main()
