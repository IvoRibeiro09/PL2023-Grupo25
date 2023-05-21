
class Values:
    def __init__(self):
        self.tag = ""
        self.posicao = 0
        self.atributo = ""
        self.conteudo = ""
        self.comment = False
        self.If = 0
        self.if_content = ""
    def setTag(self, tag):
        self.tag = tag
    def setIF(self, value):
        self.If = value
    def setIfContent(self, value):
        self.if_content = value
    def setComment(self, comment):
        self.comment = comment
    def setPosicao(self,posicao):
        self.posicao = posicao
    def setAtributo(self,atributo):
        self.atributo = atributo
    def setConteudo(self,conteudo):
        self.conteudo = conteudo
    def getTag(self):
        return self.tag
    def getIf(self):
        return self.If
    def getIfContent(self):
        return self.if_content
    def getPosicao(self):
       return self.posicao
    def getAtributo(self):
        return self.atributo
    def getConteudo(self):
        return self.conteudo
    def getComment(self):
        return self.comment

    def print(self):
        print("TAG |" +self.tag+"|")
        print("Posicao |" +str(self.posicao)+"|")
        print("Atributo |" + self.atributo+"|")
        print("Conteudo |" + self.conteudo+"|")
        print("Comment |" + str(self.comment) + "|")
        print("if |" + str(self.If) + "|")
        print("if content |" + str(self.if_content) + "|")



