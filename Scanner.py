from ReservedWords import *
'''
# SCANNER
- Maria Cruz
- Ruben Guzman
'''

# TOKENS
EOF = "EOF"

OPERATORS = ""

##      LETTER = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ_"

##      NUMBER = "0123456789"

id

#class Error():
#    Colocar los posibles errores en otro archivo
#    def __init__(self):
#        self.error_type = ""
#        self.descripcion = ""

class Token():
    def __init__(self, _type,_value, _row, _col):
        self.type = _type
        self.value =_value
        self.row = _row
        self.col = _col
    def __repr__(self):
        return "%s [ %s ] at (%i:%i)" % (self.type, self.value, self.row, self.col)

class Scanner():
    # Hacer cada funcionalidad en una funcion diferente valga la redundancia
    def __init__(self):
        self.archivo = None
        self.buffer = "" # Linea por linea
        self.tokens = []
        self.errores = []

        self.pos = [1,0] # Revisar, se podria usar alguna estructura
        self.current_char = ""
        self.lexeme = ""
        self.state = 0
        self.newLine = False

        #Aux
        self.firstOfDblOper = []
        self.getFirstOfDblOper()

    def __del__(self):
        if self.archivo: self.archivo.close()

    def begin(self, file):
        archivo = open(file)
        self.buffer = self.archivo.read()
        self.errores = []
    
    def getFirstOfDblOper(self):
        for op in OPER_DELIMITERS_2:
            self.firstOfDblOper.append(op[0])

    ### FUNCIONES
    def getInteger(self):
        print("getInteger")

    def getchar(self): # Se actualiza current_char
        # Se puede trabajar como tipo de char
        # ejemplo 0 LETTER, 1 DIGIT 
        if len(self.buffer) == 0:
            self.current_char = ""
        else:
            self.pos[1] += 1
            # Obtiene el primer caracter y lo pone en self current char
            self.current_char = self.buffer[0]
            self.buffer = self.buffer[1:]

    def peekchar(self):
        if len(self.buffer == 0):
            return ""
        return self.buffer[0]
    
    def ignoreSpaces(self):
        if self.current_char == " ":
            while self.peekchar() == " ":
                self.getchar()
                
    def ignoreComents(self):
        c = self.pos[1]
        if self.current_char == "#":
            while self.current_char != '\n':
                self.getchar()
            self.pos[1] = c
        if c == 1:
            
    def getIdentifier(self):
        # Consume todos los caracteres dentro de la expresion [a-z|A-Z][a-z|A-Z|0-9|_]*
        self.lexeme = self.current_char
        c = self.peekchar()
        while c.isalpha() or c.isdigit() or c == "_":
            self.getchar()
            self.lexeme += self.current_char
            c = self.peekchar()
    def getNumber(self):
        # Consume todos los caracteres dentro de la expresion [a-z|A-Z][a-z|A-Z|0-9|_]*
        self.lexeme = self.current_char
        c = self.peekchar()
        while c.isdigit():
            self.getchar()
            self.lexeme += self.current_char
            c = self.peekchar()
        if len(self.lexeme) > 1 and self.lexeme[0] == '0': 
          print("Numero invalido: El numero no puede tener un 0 a la izquierda")
          return False
        if len(self.lexeme) == 10 :
          if int(self.lexeme[:9]) == 214748364:
            if int(self.lexeme[9]) > 7:
              print("Numero invalido: EL numero es muy grande")
              return False
          elif int(self.lexeme[:9]) > 214748364:
            print("Numero invalido: EL numero es muy grande")
            return False
        elif len(self.lexeme) > 10:
          print("Numero invalido: EL numero es muy grande")
          return False
        return True
    
    def getTknOper(self):
        self.lexeme = self.current_char
        if self.current_char in self.firstOfDblOper:
            c = self.peekchar()
            oper = self.lexeme + c
            if oper in OPER_DELIMITERS_2:
                self.getchar()
                self.lexeme = oper
                return Token(OPER_DELIMITERS_2[oper], oper, self.pos[0], self.pos[1])
        return Token(OPER_DELIMITERS[self.lexeme], self.lexeme, self.pos[0], self.pos[1])

    def getToken(self): #(tokentype, tokenval)
        self.lexeme = ""
        token = None
        self.getchar() #Nota, no consumir chars de otros tokens, en cambio usar peek char
        
        # Limpiamos espacios vacios y comentarios
        if not self.newLine: 
            self.ignoreSpaces()
        self.ignoreComents()
        # Si hay un 
        if self.current_char == '\n':
            self.newLine = True
            aux_x = self.pos[0]
            aux_y = self.pos[1]
            self.pos[0] += 1
            self.pos[1] = 0
            return Token("NEWLINE","", aux_x, aux_y)
        # 
        if self.newLine:
            if self.current_char != " ":
              self.newLine = False
            else:
              return Token("IDENT","", self.pos[0], self.pos[1])

        # Esta buscando un id o una palabra reservada
        if self.current_char.isalpha():
            self.getIdentifier()
            if self.lexeme in KEYWORDS:
                token = Token(KEYWORDS[self.lexeme],self.lexeme, self.pos[0], self.pos[1])
            else:
                token = Token("ID",self.lexeme,self.pos[0], self.pos[1])

        # Esta buscando un numero
        elif self.current_char.isdigit():
            if self.getNumber():
              token = Token("NUMBER",self.lexeme,self.pos[0], self.pos[1])
            else: print("Error")
        
        # Buscar operadores
        elif self.current_char in OPER_DELIMITERS or self.current_char in self.firstOfDblOper:
            token = self.getTknOper()

        else:
            print("Error")

        self.newLine = False
        print("getToken")
        return token

    def debug(self):
        print("INFO SCAN - Start scanning...")
        # Falta ver los errores
        while len(self.buffer) != 0: # For now
            token = self.getToken()
            #if token == ERROR: self.errores.append(token)

            self.tokens.append(token)
            print("DEBUG SCAN - %s " % (token))


s = Scanner()
s.begin("file.txt")
s.debug()
