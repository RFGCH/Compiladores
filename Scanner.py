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
        
    ##      def isLet(self):
        ##      if LETTER.find(current_char) != -1:
            ##      return True
        ##      return False
    ##      def isNum(self):
        ##      if NUMBER.find(current_char) != -1:
            ##      return True
        ##      return False        

    ####

    def getchar(self):
        # Se actualiza current_char
        # Se puede trabajar como tipo de char
        # ejemplo 0 LETTER, 1 DIGIT 
        
        ##      if len(buffer) == 0:
            ##      current_char = ""
        ##      else:
            ##      pos[1] += 1
            ##      current_char = buffer[0]
            ##      buffer = buffer[1:]
        
        print("getchar")

    def peekchar(self):
        
        ##      if len(buffer == 0):
            ##      return ""
        ##      return buffer[0]
        
        # Ve el sig char sin consumirlo
        print("peekchar")
# si se hace por lineas
    ##      def skip_space(self):
        ##      if len(buffer) == 0:    return
        ##      while buffer[0] == ' ':
            ##      current_posx += 1
            ##      buffer = buffer[1:]
        ##      if len(buffer) != 0 and buffer[0] == '\n':   
            ##      newline = True
            ##      current_line += 1
            ##      buffer = buffer[1:]
    
    def getTknKeyword(self,lexeme):
        if lexeme in KEYWORDS:
            return Token(KEYWORDS[lexeme],lexeme, self.pos[0], self.pos[1])
        else:
            return None

    '''
        def getToken(buffer_aux):
  newline = True
  buffer_aux = saltar_fin_cadena(buffer_aux)
  char,buffer_aux = getchar(buffer_aux)
# Identación
#                 Algoritmo para identación:
# si se tiene un salto de linea es porque se tendra una new line
# solo es verdadero cuando se inicia y cuando se entra en saltar_fin_cadena
  if char == " " and newline:
    val = 1
    char = getchar(buffer_aux)[0]
    while char == " ":
     val+=1
     buffer_aux = getchar(buffer_aux)[1]
     char = getchar(buffer_aux)[0]
    print("ident",val)
    newline = False
    return buffer_aux
#Algoritmo para los comentarios
  if char == "/":
    char = getchar(buffer_aux)[0]
    if char == "/":
      buffer_aux = goto("\n",buffer_aux)
      buffer_aux = getToken(buffer_aux)
      return buffer_aux
    elif char == "*":
      char, buffer_aux = getchar(buffer_aux)
      buffer_aux = goto("*",buffer_aux)
      char,buffer_aux = getchar(buffer_aux)
      while char != "/" :
        if len(buffer_aux)==0:
          print("Comentario sin cerrar")
          return buffer_aux
        buffer_aux = goto("*",buffer_aux)
        char,buffer_aux = getchar(buffer_aux)
      buffer_aux = getToken(buffer_aux)
      return buffer_aux
    else:
      print("Div")
      return buffer_aux
# Tokens
  if char == "(":
    print("lparen","(")
  elif char == ")":
    print("rparen",")")
  elif char == "+":
    print("rparen","+")
  elif char == "-":
    print("rparen","-")
  elif char == "*":
    print("rparen","*")
  elif char == ":":
    char = getchar(buffer_aux)[0]
    if char == "=":
      buffer_aux = getchar(buffer_aux)[1]
      print("assing",":=")
    else:
      print("Falta \"=\" para la asignación","")
  elif char == ".":
    val = char
    char = getchar(buffer_aux)[0]
    if isNm(char):
      while(isNm(char)):
        buffer_aux = getchar(buffer_aux)[1]
        val+=char
        char = getchar(buffer_aux)[0]
      print("digit",val)
    else:
      print("Falta un digito despues de \".\"","")
  elif isNm(char):
    val = char
    char = getchar(buffer_aux)[0]
    while(isNm(char)):
      buffer_aux = getchar(buffer_aux)[1]
      val+=char
      char = getchar(buffer_aux)[0]
    if char == '.':
      val += char
      buffer_aux = getchar(buffer_aux)[1]
      char = getchar(buffer_aux)[0]
    while(isNm(char)):
      buffer_aux = getchar(buffer_aux)[1]
      val+=char
      char = getchar(buffer_aux)[0]
    print("num",val)
  elif isID(char):
    val = char
    char = getchar(buffer_aux)[0]
    while(isID(char)or isNm(char)):
      buffer_aux = getchar(buffer_aux)[1]
      val+=char
      char = getchar(buffer_aux)[0]
    print("id",val)

  return buffer_aux
'''
    def getToken(self): #(tokentype, tokenval)
        ##      skip_space()
        ##      getchar()
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
