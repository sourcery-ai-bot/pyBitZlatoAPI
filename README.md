# pyBitZlatoAPI
Python script for BitZlatoAPI

It is unofficial lib for work with bitzlato.com API. The repository will updates...

### Dependencies
```
pip install requests
pip install python-jose
```


### How it's work?
1. Get account purchase orders 
```
from bitzlato import Bitzlato

bot = bitzlato.Bitzlato(parameters=<dict with bitzlato key>, email=<your bitzlato account email>)
bot.get_my_orders('purchase')
```
