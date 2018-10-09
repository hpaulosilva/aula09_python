class Usuario():
    def __init__(self,login,senha):
        self.login = login
        self.__senha = senha # nao mostra a senha vai ser restrito 

    def valida_senha(self,login):
        return senha == self.__senha

u = Usuario("login","123")
print(u.login)
print(u.valida_senha("123"))