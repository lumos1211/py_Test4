import csv
import matplotlib.pyplot as plt

f = open('population/202006_202006_연령별인구현황_월간_남여.csv')
data = csv.reader(f)

m = []
f = []

for row in data:
    if '전국' in row[0]:
        for i in range(0, 101):
            m.append(int(row[i+3].replace(",", "")))
            f.append(int(row[-(i+1)].replace(",", "")))
f.reverse()

plt.barh(range(101), m)
plt.barh(range(101), f)
plt.show()
