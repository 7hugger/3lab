#Формируется матрица F следующим образом: скопировать в нее А и если количество нулей в В больше, чем в Е, то поменять в ней местами В и С симметрично, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * F, иначе вычисляется выражение (A-1 +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере 
import numpy as np
import matplotlib.pyplot as plt

N = 6
file_path = '4.txt'

# Проверка существования файла и его содержимого
try:
    A = np.loadtxt(file_path, dtype=int)
except Exception as e:
    print(f"Ошибка при загрузке файла: {e}")
    exit()

if A.shape != (N, N):
    print("Ошибка: Матрица A должна быть размером 6x6.")
    exit()

print("Матрица A:")
print(A)

# Обработка ввода K
try:
    K = int(input("Введите K: "))
except ValueError:
    print("Ошибка: K должно быть целым числом.")
    exit()

F = A.copy()
half_N = N // 2
B, C, D, E = A[:half_N, :half_N], A[:half_N, half_N:], A[half_N:, :half_N], A[half_N:, half_N:]

if np.sum(B == 0) > np.sum(E == 0):
    print("Замена B и C симметрично")
    F[:half_N, half_N:], F[:half_N, :half_N] = B[:, ::-1], C[:, ::-1]
else:
    print("Замена B и E несимметрично")
    F[:half_N, :half_N], F[half_N:, half_N:] = E, B

det_A = np.linalg.det(A)
trace_F = np.trace(F)

if det_A > trace_F:
    result = A @ A.T - K * F
else:
    try:
        A_inv = np.linalg.inv(A)
        F_inv = np.linalg.inv(F)
        G = np.tril(A)
        result = (A_inv + G - F_inv) * K
    except np.linalg.LinAlgError:
        print("Ошибка: Невозможно вычислить обратную матрицу для A или F.")
        exit()

print("\nМатрица F:")
print(F)

print("\nРезультат вычислений:")
print(result)

plt.figure(figsize=(10, 8))

# График 1: Тепловая карта F
plt.subplot(2, 2, 1)
plt.title("Матрица F")
plt.imshow(F, cmap='plasma')
plt.colorbar()

# График 2: Гистограмма значений результата
plt.subplot(2, 2, 2)
plt.title("Гистограмма значений матрицы F")
plt.hist(F.flatten(), bins=30, color='blue', alpha=1)
plt.xlabel("Значения")
plt.ylabel("Частота")

# График 3: Линейный график средних значений строк результата
plt.subplot(2, 2, 3)
plt.title("Средние значения строк матрицы F")
plt.plot(np.mean(F, axis=1), marker='o', color='red')
plt.xlabel("Номер строки")
plt.ylabel("Среднее значение")

plt.tight_layout()
plt.show()
