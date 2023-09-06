#9.2[42]: Работа в Google Colab.
#Файл california_housing_train.csv, который находится в папке sample_data Узнать какая максимальная households в зоне минимального значения population

import pandas as pd
df=pd.read_csv('sample_data/california_housing_train.csv')
df[df['population']==df['population'].min()]['households'].max()

#9.1[40]: Работа в Google Colab.
#Файл california_housing_train.csv, который находится в папке sample_data Для домов, где кол-во людей от 0 до 500 (population) вывести информацию о цене дома(median_house_value):
#максимальное значение
#минимальное значение
#среднее
#медиану

import pandas as pd
df=pd.read_csv('sample_data/california_housing_train.csv')
df[df['population'] < 500]['median_house_value'].describe()
