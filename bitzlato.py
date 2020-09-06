import requests
import datetime
import time
import random
from jose import jws
from jose.constants import ALGORITHMS


class Bitzlato():
    def __init__(self, parameters: dict, email: str):
        self.kty = parameters['kty']
        self.alg = parameters['alg']
        self.crv = parameters['crv']
        self.x = parameters['x']
        self.y = parameters['y']
        self.d = parameters['d']
        self.email = email
        self.kid = '1'
        self.conn = requests.Session()

    def connector(self):
        dt = datetime.datetime.now()
        ts = time.mktime(dt.timetuple())
        claims = {
            "email": self.email,
            "aud": "usr",
            "iat": int(ts),
            "jti": hex(random.getrandbits(64))
        }
        key = {
            "kty": self.kty,
            "alg": self.alg,
            "crv": self.crv,
            "x": self.x,
            "y": self.y,
            "d": self.d
        }
        token = jws.sign(claims, key, headers={"kid": self.kid}, algorithm=ALGORITHMS.ES256)
        return token

    def get_all_orders(self, cryptocurrency: str, currency: str, is_owner_active: bool, limit: int,
                       pay_method: str, order_type: str) -> dict:
        result = requests.get('https://bitzlato.com/api/p2p/exchange/dsa/', headers={
            "Authorization": "Bearer " + self.connector()
        },
            params={
                "cryptocurrency": f'{cryptocurrency}',
                "currency": f"{currency}",
                "type": f"{order_type}",  # purchase, selling
                "isOwnerActive": True,
                "limit": 20,
                "paymethod": f'{pay_method}'
        })
        response = result.json()
        return response

    def get_account_orders_by_order_type(self, order_type) -> list:
        result = self.conn.get('https://bitzlato.com/api/p2p/dsa/all', headers={
            "Authorization": "Bearer " + self.connector()
        })
        local_array = []
        if result.status_code == 200:
            for res in result.json():
                try:
                    if res['type'] == order_type:
                        local_array.append(res)
                except KeyError:
                    pass
        return local_array

    def set_new_price(self, order_id, price):
        result = self.conn.put(f'https://bitzlato.com/api/p2p/dsa/{order_id}', headers={
            "Authorization": "Bearer " + self.connector()
        }, json={
            "rateValue": str(price)
        })
        return result.json()

    def get_paymethods(self):
        result = self.conn.get('https://bitzlato.com/api/p2p/dsa/paymethods/purchase/RUB/BTC/',
                               headers={
                                   "Authorization": "Bearer " + self.connector()
                               })
        return result.json()
