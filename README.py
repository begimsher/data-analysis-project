# data-analysis-project
import pandas as pd
import random

# Создаем исходный список
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создаем DataFrame
data = pd.DataFrame({'whoAmI': lst})
print("Original DataFrame:")
print(data.head())

# Создаем новый DataFrame для one-hot представления
one_hot_data = pd.DataFrame()

# Получаем уникальные значения в столбце 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создаем столбцы для каждого уникального значения и заполняем их
for value in unique_values:
    one_hot_data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)

# Присоединяем one-hot столбцы к исходному DataFrame (опционально)
# data = data.join(one_hot_data)

print("\nOne-hot encoded DataFrame:")
print(one_hot_data.head())
