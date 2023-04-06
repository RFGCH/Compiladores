'''
# SCANNER
- Maria Cruz
- Ruben Guzman
'''

# TOKENS
EOF = "EOF"

OPERATORS = ""

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

        self.pos = [0,0] # Revisar, se podria usar alguna estructura
        self.classchar = -1
        self.current_char = None

    def __del__(self):
        if self.archivo: self.archivo.close()

    def begin(self, file):
        archivo = open(file)
        self.errores = []

    
    ### FUNCIONES
    def getInteger(self):
        print("getInteger")


    ####

    def getchar(self):
        # Se actualiza current_char
        # Se puede trabajar como tipo de char
        # ejemplo 0 LETTER, 1 DIGIT 
        print("getchar")

    def peekchar(self):
        # Ve el sig char sin consumirlo
        print("peekchar")


    def getToken(self): #(tokentype, tokenval)
        print("getToken")

    def debug(self):
        print("INFO SCAN - Start scanning...")
        # Falta ver los errores
        while True: # For now
            token = self.getToken()
            #if token == ERROR: self.errores.append(token)

            self.tokens.append(token)
            print("DEBUG SCAN - %s " % (token))
            if token == EOF:
                break

s = Scanner()
s.begin("file.txt")
s.debug()