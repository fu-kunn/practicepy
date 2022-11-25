from datetime import datetime, date
import pickle

d = {
  'today': date.today(),
  'delta': date(2024, 1, 1) - date.today()
}

print(d)
