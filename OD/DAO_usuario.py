class DAO_usuario():  

    def __init__(self,usuario,senha):
        self.usuario = usuario
        self.senha = senha

    def pegar_usuario(self):
        return self.usuario
    def pegar_senha(self):
        return self.senha
