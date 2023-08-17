mport pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Загрузка датасета
def load_dataset(file):
    try:
        df = pd.read_csv(file)
        return df
    except FileNotFoundError:
        print("Файл не найден")
        return None

# Визуализация распределения
def plot_distribution(data, col):
    if data[col].dtype == 'object':
        # Построение pie chart для категориальных переменных
        fig, ax = plt.subplots()
        ax.pie(data[col].value_counts(), labels=data[col].value_counts().index, autopct='%1.1f%%')
        ax.set_title(f"Распределение {col}")
        plt.show()
    else:
        # Построение гистограммы для числовых переменных
        fig, ax = plt.subplots()
        sns.histplot(data=data, x=col, kde=True)
        ax.set_title(f"Распределение {col}")
        plt.show()

# Выполнение алгоритма проверки гипотез
def run_hypothesis_test(data, col1, col2, test):
    test_results = None
    if test == "t-test":
        test_results = stats.ttest_ind(data[col1], data[col2])
    elif test == "wilcoxon":
        test_results = stats.wilcoxon(data[col1], data[col2])
    # Добавьте другие алгоритмы проверки гипотез по выбору

    if test_results:
        print("Результаты проверки гипотез:")
        print(test_results)

# Загрузка датасета
file = input("Введите путь к CSV файлу: ")
data = load_dataset(file)
if data is not None:
    # Выбор двух переменных из датасета
    col1 = input("Выберите первую переменную: ")
    col2 = input("Выберите вторую переменную: ")

    # Визуализация распределения
    plot_distribution(data, col1)
    plot_distribution(data, col2)

    # Выбор алгоритма проверки гипотез
    test = input("Выберите алгоритм проверки гипотез (t-test / wilcoxon): ")

    # Выполнение алгоритма проверки гипотез
    run_hypothesis_test(data, col1, col2, test)