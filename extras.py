# -*- coding: utf-8 -*-
import os
import pprint, json
from pygments import highlight, lexers, formatters

def clearScreen():
   os.system('clear')

def error(error_message):
   clearScreen()
   print error_message
   exit(1)

def prettyPrintJson(dict_json):
   pp = pprint.PrettyPrinter(indent=4)
   pp.pprint(dict_json)

def prettyPrintJson2(dict_json):
   print dict_json
   json_txt = str(dict_json)
   print json_txt
   formatted_json = json.dumps(json_txt, sort_keys=True, indent=4)
   print formatted_json
   colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
   print colorful_json
