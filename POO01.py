
from zmq import NULL


class aluno(object):

    def __init__(self,nome,identidade,entrada,saida):
        self.nome = nome
        self.identidade = identidade
        self.entrada = entrada
        self.saida = saida
    
    def print_full_aluno(self):
        print('Nome: '+ self.nome + '\t| Identidade: ' + str(self.identidade) + '| entrada: ' + str(self.entrada) + '| saida: ' + str(self.saida))

    def setAulunoName(self, nomeAluno):
        self.nome = nomeAluno
    
    def setAlunoID(self, ID):
        self.identidade = ID
    
    def setAlunoEntrada(self, entrada):
        self.entrada = entrada
    
    def setAlunoSaida(self, saida):
        self.saida = saida
    
    def getAlunoName(self):
        return self.nome



x = aluno('Arlindo', 13214, NULL , 2025)


x.print_full_aluno()

x.setAulunoName('Yuri')

x.print_full_aluno()

x.setAlunoEntrada(2023)

x.print_full_aluno()

print(x.getAlunoName())




