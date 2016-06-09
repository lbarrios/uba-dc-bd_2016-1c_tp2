# -*- coding: utf-8 -*-
import os
import pprint, json, simplejson
from bson import json_util # pymongo decoding
from pygments import highlight, lexers, formatters

def clearScreen():
    os.system('clear')

def error(error_message):
    clearScreen()
    print error_message
    exit(1)

def convertToJson(obj):
    formatted_json = simplejson.dumps(obj, indent=4, use_decimal=True, default=json_util.default)
    return formatted_json

def prettyPrintJson(dict):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dict)

def prettyPrintJson2(dict_json):
    #formatted_json = simplejson.dumps(dict_json, indent=4, use_decimal=True)
    formatted_json = convertToJson(dict_json)
    colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
    print colorful_json
