def recomendar_plano (consumo):

  if consumo <= 10:
    print ("Plano Essencial Fibra - 50Mbps")
  elif consumo > 10 and consumo < 20:
    print ("Plano Prata Fibra - 100Mbps")
  elif consumo > 20:
    print ("Plano Premium Fibra - 300Mbps")

consumo = float(input())

recomendar_plano(consumo)

