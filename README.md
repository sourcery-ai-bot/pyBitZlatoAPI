# pyBitZlatoAPI
I think it is a python lib, but it is looks like python script for bitzlato.com API :)

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
result = bot.get_my_orders('purchase')
print(result)
```

2. Get all market orders with parameters

```
from bitzlato import Bitzlato

bot = bitzlato.Bitzlato(parameters=<dict with bitzlato key>, email=<your bitzlato account email>)
result = bot.get_all_orders(cryptocurrency='BTC', currency='RUB', is_owner_active = True, limit=20,
                            pay_method='443', order_type='purchase')
print(result)
```
