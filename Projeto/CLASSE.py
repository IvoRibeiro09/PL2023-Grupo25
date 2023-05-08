
class Values:
    def __init__(self):
        self.tag = ""
        self.posicao = 0
        self.atributo = ""
        self.conteudo = ""

    def setTag(self,tag):
        self.tag = tag
    def setPosicao(self,posicao):
        self.posicao = posicao
    def setAtributo(self,atributo):
        self.atributo = atributo
    def setConteudo(self,conteudo):
        self.conteudo = conteudo
    def getTag(self):
        return self.tag
    def getPosicao(self):
       return self.posicao
    def getAtributo(self):
        return self.atributo
    def getConteudo(self):
        return self.conteudo

    def print(self):
        print("TAG |" +self.tag+"|")
        print("Posicao |" +str(self.posicao)+"|")
        print("Atributo |" + self.atributo+"|")
        print("Conteudo |" + self.conteudo+"|")



