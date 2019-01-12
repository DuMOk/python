#модуль для работы с json файлами
import json
import datetime
import decimal
import uuid

#класс для корректной сериализации
class CustomJSONEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, datetime.datetime):
      r = o.isoformat()
      if o.microsecond:
        r = r[:23] + r[26:]
      if r.endswith('+00:00'):
        r = r[:-6] + 'Z'
      return r
    elif isinstance(o, datetime.date):
      return o.isoformat()
    elif isinstance(o, datetime.time):
      if o.utcoffset() is not None:
        raise ValueError("JSON cant't represent timezone-aware times.")
      r = o.isoformat()
      if o.microsecond:
        r = r[:12]
      return r
    elif isinstance(o, (decimal.Decimal, uuid.UUID)):
      return str(o)
    else:
      return super(CustomJSONEncoder, self).default(o)


#функция добавления нового заказа в файл
def write_order_to_json(item, quantity, price, buyer, date):
  order = {
    "item": item,
    "quantity": quantity,
    "price": price,
    "buyer": buyer,
    "date": str(date)
  }
  
  with open('orders.json','r') as fh_r:
    data_orders = json.load(fh_r)
    
  with open('orders.json','w') as fh_w:
    new_data = data_orders['orders']
    new_data.append(order)
    json.dump(data_orders, fh_w, cls=CustomJSONEncoder, indent=4)

#код основной программы
write_order_to_json('Печеньки', 3, 23.4, 'John', datetime.datetime.now())

with open('orders.json') as fh:
  content = fh.read()
  objs = json.loads(content)

for dict in objs['orders']:
  for key, val in dict.items():
    print(key, val)
  print('/////////////////////////////////')
