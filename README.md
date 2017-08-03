AMS Monitor System
==================
A toolset to monitor AMS online or offline

Installation
------------

#### Requirements
As root
```
apt-get install python3
apt-get install python3-matplotlib
apt-get install python3-pandas
```

#### Configuration
* Modify matplotlib config file `/etc/matplotlibrc` to display chinese
* ```find font.family and font.sans-serif that delete notation, add chinese font SimHei at the top of font.sans-serif```
* SimHei download link:
* ```http://fontzone.net/download/simhei```

* Add simhei.ttf to path
* ```/usr/share/matplotlib/mpl-data/fonts/ttf/``` 
