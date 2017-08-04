#!/usr/bin/env python3
# encoding: utf-8
from urllib.request import urlopen
from urllib.parse import quote
from io import StringIO
import csv
import urllib.request
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.font_manager as fm

x = []
y = []
time = []
info = []
Display_count = 144


def request_data(farm, count):
    url = "http://192.168.1.200:8888/miao/" + quote(farm) + ".csv"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    data = urlopen(req).read().decode('ascii', 'ignore')

    datafile = StringIO(data)
    csvReader = csv.reader(datafile)

    for row in csvReader:
        info.append(row)

    x = [datetime.strptime(d[0], '%Y-%m-%d %H:%M:%S') for d in info[-Display_count::]]
    y = [d[1] for d in info[-Display_count::]]
    myFmt = mdates.DateFormatter('%m/%d %H:00:00')
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.xaxis.set_major_formatter(myFmt)
    ax.set_xlim(x[0], x[-1])
    plt.xticks(pd.date_range(x[0], x[-1], freq=('60min')))
    plt.yticks([0, 1], ['offline', 'online'])
    plt.xlabel("Time")
    plt.plot(x, y)
    plt.gcf().autofmt_xdate()
    prop = fm.FontProperties(fname='/usr/share/fonts/truetype/wqy.ttf')
    ax.set_title(farm + ' Latest time:' + info[-1][0], fontproperties=prop)
    figgg = plt.gcf()
    figgg.set_size_inches(13.5, 6.5)
    plt.savefig('./images/' + count + '.png', dpi=100)

if __name__ == '__main__':
    Parameter = [('老安统', '1'), ('统子河', '2'), ('广元_1网段', '3'), ('芒市', '4'), ('木里', '5'), ('广元_3网段', '6'), ('广元_4网段', '7')]
    for data in Parameter:
        request_data(data[0], data[1])
