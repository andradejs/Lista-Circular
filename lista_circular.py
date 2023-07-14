from no import No

class Lista_circula:


    def __init__(self) -> None:
        self.indice = 0
        self.inicio = None
        self.final = None
        


    def procurar(self):
        variavel = self.inicio
        while True:
            variavel = variavel.next
            if variavel.next == self.inicio:
                break
        return variavel


    def adicionar(self,valor,pos = 0):

        no = No(valor)

        if self.inicio == None:
            self.inicio = no

        self.indice += 1
        if pos == self.indice-1:
            self.final = no
            self.final.next = self.inicio
        

            


        if self.inicio != None:
            if pos != 0:
                variavel = self.inicio
                for elemento in range(0,pos-1):
                    variavel = variavel.next
                no.next = variavel.next
                variavel.next = no    
            else:
                no.next = self.inicio
                self.inicio = no
                self.final.next = no
                

            


    def apagar(self,valor):
        
        if self.indice == 1:
            self.inicio = None
        else:
            variavel = self.inicio
            while True:

                var_referencia = variavel
                variavel = variavel.next

                if variavel.valor == valor:

                    if variavel == self.inicio:
                        self.inicio = variavel.next

                    var_referencia.next = variavel.next

                    break
        self.indice -=1
        
        


    def tamanho(self):

        print(self.indice)


    def mostra(self):
        
        elemento = self.inicio

        print('[',end='')
        while True:
            print( elemento.valor,end='')
            
            elemento = elemento.next
            if elemento == self.inicio:
                print(']')
                break
            print(',',end='')
            
            
