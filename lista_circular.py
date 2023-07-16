from no import No

class Lista_circula:


    def __init__(self) -> None:
        self.tamanho = 0
        self.inicio = None
        self.final = None
        


    def procurar(self):
        variavel = self.inicio
        while True:
            variavel = variavel.next
            if variavel.next == self.inicio:
                break
        return variavel

    def mostrar_tamanho(self):

        print(self.tamanho)

    def adicionar(self,valor,pos = None):

        self.tamanho += 1
        if  pos == None  or pos > self.tamanho-1:
            pos = self.tamanho-1

        no = No(valor)


        if pos == self.tamanho-1:
            self.final = no
            self.final.next = self.inicio
        
        if self.inicio == None:
            self.inicio = no
            self.final = no
            self.final.next = self.inicio

            


        else:
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
        
        if self.tamanho == 1:
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
        self.tamanho -=1
        
        


   


    def mostrar(self):
        
        elemento = self.inicio


        print('[',end='')
        if elemento == None:
            print(']')
        else: 
            while True:
                print( elemento.valor,end='')
                
                elemento = elemento.next
                if elemento == self.inicio:
                    print(']')
                    break
                print(',',end='')
            
            
