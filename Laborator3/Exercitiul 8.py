import datetime

dt = datetime.datetime.now()
print("Data completa:", dt)

anul = lambda x: x.year
luna = lambda x: x.month
ziua = lambda x: x.day
ora = lambda x: x.time()

print("An:", anul(dt))
print("Luna:", luna(dt))
print("Ziua:", ziua(dt))
print("Ora:", ora(dt))