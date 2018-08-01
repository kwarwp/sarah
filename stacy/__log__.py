
{'date': 'Wed Aug 01 2018 15:48:23.249 GMt-0300 (Horário Padrão da Argentina) -X- SuPyGirls -X-',
'error': '''
 module <string> line 8
  HOMEM ARANHA = "https://opcaonews.com.br/wp-content/uploads/2017/07/homem-aranha.png"
         ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Aug 01 2018 15:57:00.602 GMt-0300 (Horário Padrão da Argentina) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 42
    jogo()
  module <module> line 35
    mestreyoda = Elemento(img=MESTREYODA, tit="mestreyoda", style=dict(left=300, 
NameError: name 'MESTREYODA' is not defined
'''},