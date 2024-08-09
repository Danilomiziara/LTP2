from Classes import Veiculo, Carro, Moto


if __name__ == '__main__':
    v1 = Veiculo(2000000.00, "supra", 0)
    ("------------------------------------------------")
    print("- veiculo 1:", v1)
    print(vars(v1))
    print(v1.__dict__)
    print(f'valor do veiculo 1 --> {v1.get_valor()}')
    print(f'modelo do veiculo 1 --> {v1.get_modelo()}')
    print(f'quilometragem do veiculo 1 --> {v1.get_km()}')
    v1.atuliza_valor(50000.00)
    print(f'novo valor veiculo 1 --> {v1.get_valor()}')
    print("------------------------------------------------")
    c1 = Carro (100000.00, "carro joia", 2000, 2)
    print("- Carro 1:", c1)
    print(f'valor carro 1--> {c1.get_valor()}')
    print(f'modelo carro 1--> {c1.get_modelo()}')
    print(f'quilometragem carro 1--> {c1.get_km()}')
    print(f'quantidade de portas do carro 1--> {c1.get_portas()}')
    c1.atuliza_valor(50000)
    c1.set_km(5000)
    print("------------------------------------------------")
    print(f'novo valor do carro 1--> {c1.get_valor()}')
    print(f'nova quilometragem do carro 1--> {c1.get_km()}')
    print("------------------------------------------------")
    c2 = Carro (2000.00, "unozinho prejudicado", 600000)
    print('- Carro 2:\n', c2)
    print(f'valor carro 2--> {c2.get_valor()}')
    print(f'modelo carro 2--> {c2.get_modelo()}')
    print(f'quilometragem carro 2--> {c2.get_km()}')
    print("------------------------------------------------")
    c3 = Carro (1111111.00, "toro com 2 rodas")
    print('- Carro 3:\n', c3)
    print(f'valor carro 3--> {c3.get_valor()}')
    print(f'modelo carro 3--> {c3.get_modelo()}')
    print("------------------------------------------------")
    m1 = Moto (10323.00, "moto paia", 0, 100)
    print('- moto 1:\n', m1)
    print(f'valor moto 1--> {m1.get_valor()}')
    print(f'modelo da moto 1--> {m1.get_modelo()}')
    print(f'cilindrada moto 1--> {m1.get_cilidrada()}')
    print(f'quilometragem moto 1--> {m1.get_km()}')
    print("------------------------------------------------")
    m2 = Moto (1033.00, "moto nem anda mais", 1000000, 30)
    print('- moto 2:\n', m2)
    print(f'valor moto 2--> {m2.get_valor()}')
    print(f'modelo da moto 2--> {m2.get_modelo()}')
    print(f'cilindrada moto 2--> {m2.get_cilidrada()}')
    print("------------------------------------------------")
    m2.set_valor(1000.00)
    print(f'novo valor da moto 2 --> {m2.get_valor()}')
    print("------------------------------------------------")
    m3 = Moto (1000000.00, "super")
    print('- moto 3:\n', m3)
    print(f'valor moto 3--> {m3.get_valor()}')
    print(f'modelo da moto 3--> {m3.get_modelo()}')
    print("------------------------------------------------")
