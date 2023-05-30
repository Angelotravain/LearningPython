## Exercicio 1

class Funcionario:
    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario
    
    def aumentar_salario(self, percentual):
        self.salario += self.salario * percentual / 100
    
    def apresentar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Cargo:", self.cargo)
        print("Salário:", self.salario)


class Gerente(Funcionario):
    def __init__(self, nome, idade, cargo, salario, setor):
        super().__init__(nome, idade, cargo, salario)
        self.setor = setor
    
    def apresentar(self):
        super().apresentar()
        print("Setor:", self.setor)


class Empresa:
    def __init__(self):
        self.funcionarios = []
    
    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            funcionario.apresentar()
            print()

## exercicio 2

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            litros_abastecidos = self.quantidade_combustivel
            valor_total = litros_abastecidos * self.valor_litro
            print(f"Quantidade máxima de combustível atingida. Abastecidos {litros_abastecidos:.2f} litros.")
        else:
            valor_total = valor
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros.")
        print(f"Valor a ser pago: R$ {valor_total:.2f}")
    
    def abastecer_por_litro(self, litros):
        if litros > self.quantidade_combustivel:
            litros = self.quantidade_combustivel
            valor_total = litros * self.valor_litro
            print(f"Quantidade máxima de combustível atingida. Abastecidos {litros:.2f} litros.")
        else:
            valor_total = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            print(f"Foram abastecidos {litros:.2f} litros.")
        print(f"Valor a ser pago: R$ {valor_total:.2f}")
    
    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
    
    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
    
    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
