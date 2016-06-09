#!/usr/bin/env python
# -*- coding: utf-8 -*-
import extras
import pgsql

operaciones = pgsql.get_RealDictCursor("operaciones.sql")
facturas = pgsql.get_RealDictCursor("facturas.sql")

# Debug
extras.clearScreen()
print "Facturas:"
extras.prettyPrintJson2(facturas.fetchall())
print "Operaciones:"
extras.prettyPrintJson2(operaciones.fetchall())
