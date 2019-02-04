
hum = 60  # 습도
temp  = 24.4  # 온도

DI = int(float(0.81) * float(temp) + float(0.01) * float(hum) * (float(0.99) * float(temp) - float(14.3)) + float(46.3))  # 붍쾌지수

print("불쾌지수 : ", DI)
