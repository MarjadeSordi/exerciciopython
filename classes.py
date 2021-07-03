class Pessoa:
  def __init__(self, codigo, nome, endereco, telefone): 
    self.__codigo = codigo 
    self.nome = nome
    self.endereco = endereco
    self.telefone = telefone 

  def imprimirnome(self):
    return print('Nome: ' + self.nome)

  def imprimirtelefone(self):
    return print('Telefone: ' + self.telefone)



class Fisica(Pessoa):
  def __init__(self,codigo, nome, endereco, telefone, cpf,idade, peso, altura):
    super().__init__(codigo, nome, endereco, telefone)
    self.__cpf = cpf
    self.idade = idade
    self.peso = peso
    self.altura = altura 


  def imprimircpf(self):
    return ('CPF: ' + self.cpf)

  def calcularIMC(self): 
    calcular = self.peso / self.altura
    return print('IMC' + str(calcular))



class Juridica(Pessoa):
  def __init__(self,codigo, nome, endereco, telefone, CNPJ, inscricaoEstadual, quantidadeFuncionarios):
    super().__init__(codigo, nome, endereco, telefone)
    self.__CNPJ = 0
    self.__inscricaoEstadual = 0
    self.quantidadeFuncionarios = 0


  def imprimircpf(self):
    return ('CNPJ: ' + self.__CNPJ)

  def imprimirnotaFiscal(self): 
    return print ('Nome: '+ self.nome + "\n"
    'CNPJ: ' + str(self.__CNPJ) + "\n"
    'Inscrição Estadual: ' + str(self.__inscricaoEstadual) + "\n"
    'Quantidade de Funcionários: ' + str(self.quantidadeFuncionarios)) 