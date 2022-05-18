import pandas as pd

data = pd.read_csv("/Users/lizazhyrova/Documents/dsmllessons/mlcourse.ai/data/adult.data.csv")
print('Количество мужчин: ', data[data['sex'] == 'Male'].count())
print('Количество женщин: ', data[data['sex'] == 'Female'].count())

print('1____________________________')
print(data["sex"].value_counts())
print('____________________________')

print('2____________________________')
print('Средний возраст женщин: ', data['age'][data['sex'] == 'Female'].mean())
print('____________________________')

print('3____________________________')
print('Процент коренных немцев: ', data['native-country'].value_counts(normalize=True)['Germany'])
print('____________________________')

print('4____________________________')
print('Зарабатывают >50k: ')
print('Средний возраст: ', data['age'][data['salary'] != '<=50K'].mean())
print('Отклонение: ', data['age'][data['salary'] != '<=50K'].std())
print('5____________________________')

print('Зарабатывают <=50k: ')
print('Средний возраст: ', data['age'][data['salary'] == '<=50K'].mean())
print('Отклонение: ', data['age'][data['salary'] == '<=50K'].std())
print('____________________________')

print('7____________________________')
print('Maximum age of men of Amer-Indian-Eskimo race :')
print(data[data['race'] == 'Amer-Indian-Eskimo'].groupby(['race'])['age'].max())
print('____________________________')

print('8____________________________')
print('>50k')
#print(data[data['salary'] != '<=50K'].groupby(['salary'])['' in data['marital-status']].describe())
print(data[(data["marital-status"].str.startswith("Married")) & (data["sex"] == "Male")]['salary'].value_counts())
print('____________________________')


print('9____________________________')
mhr = data['hours-per-week'].max()
print(data[(data['salary'] == '<=50K') & (data['hours-per-week'] == mhr)].count()['age'])
print('____________________________')

print('10____________________________')
print('Время работы тех, кто зарабатывает < 50K: ')
print(data['hours-per-week'][(data['salary'] == '<=50K') & (data['native-country'] == 'Japan')].mean())
print('Время работы тех, кто зарабатывает > 50K: ')
print(data['hours-per-week'][(data['salary'] != '<=50K') & (data['native-country'] == 'Japan')].mean())
print('____________________________')