
{'date': 'Wed Aug 01 2018 14:26:02.820 GMt-0300 (Horário Padrão da Argentina) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  print "hellow world";
        ^
SyntaxError: missing parenthesis in call to 'print'
'''},
{'date': 'Wed Aug 01 2018 14:26:17.470 GMt-0300 (Horário Padrão da Argentina) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  echo "hellow world";
        ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Aug 01 2018 14:26:42.587 GMt-0300 (Horário Padrão da Argentina) -X- SuPyGirls -X-',
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
  module <module> line 2
    echo("hellow world");
NameError: name 'echo' is not defined
'''},
{'date': 'Wed Aug 01 2018 14:30:02.58 GMt-0300 (Horário Padrão da Argentina) -X- SuPyGirls -X-',
'error': '''hellow world
Traceback (most recent call last):
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
  module <module> line 5
    print("olá, " . nome$);
AttributeError: 'str' object has no attribute 'nome$'
'''},
{'date': 'Wed Aug 01 2018 14:30:14.630 GMt-0300 (Horário Padrão da Argentina) -X- SuPyGirls -X-',
'error': '''
 module <string> line 5
  print("olá, " +. nome$);
                   ^
SyntaxError: invalid syntax
'''},