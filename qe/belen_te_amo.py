import art

class CorazonDeAlvaro:

    def __init__(self, nombre='_b.lend'):
        self.nombre = nombre

    def __repr__(self):
        return f'Soy el corazón del alvaritions y estoy muy enmorado de:\n {self.nombre}'

if __name__ == '__main__':
    corazon = CorazonDeAlvaro()
    print(corazon)