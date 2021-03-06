#!/usr/bin/env python
# -*- coding: utf-8 -*-
import screen
import pgsql
from converter import operacion_record_to_dict, factura_record_to_dict
from pymongo import MongoClient

screen.clearScreen()
client = MongoClient()
db = client.prod

# Facturas
print "Facturas:"
facturas_cur = pgsql.get_DictCursor("facturas.sql")
facturas = map(factura_record_to_dict, facturas_cur.fetchall())
screen.prettyPrintJson2(facturas)
db.facturas.delete_many({})
db.facturas.insert_many(facturas)

# Operaciones
print "Operaciones:"
operaciones_cur = pgsql.get_DictCursor("operaciones.sql")
operaciones = map(operacion_record_to_dict, operaciones_cur.fetchall())
screen.prettyPrintJson2(operaciones)
db.operaciones.delete_many({})
db.operaciones.insert_many(operaciones)
