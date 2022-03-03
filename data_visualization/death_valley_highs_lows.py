import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)

    head_row = next(reader)
    # for index, column_header in enumerate(head_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {date}')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    plt.style.use('seaborn')
    plt.rcParams['font.sans-serif'] = ['Songti SC']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(date, highs, lows, facecolor='blue', alpha=0.1)

    ax.set_title("2018年每日最高温度和最低温度\n美国加利福尼亚州死亡谷", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('温度（F）', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
