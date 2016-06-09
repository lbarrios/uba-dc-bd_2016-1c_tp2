# -*- coding: utf-8 -*-
import os
import pprint, json, simplejson
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
    formatted_json = simplejson.dumps(dict_json, indent=4, use_decimal=True)
    colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
    print colorful_json
