#!/usr/bin/env python
# -*- coding: utf-8 -*-
import extras
import pgsql

def operacion_record_to_document(record):
    operacion = dict()
    operacion['id'] = record['id_operacion']
    operacion['precio'] = record['precio']
    operacion['vendedor'] = record['publicada_por']
    operacion['comprador'] = record['id_comprador']
    operacion['comision'] = record['comision']
    operacion['valoracion_comprador'] = {
        'id_valoracion' : record['valoracion_comprador_id_valoracion'],
        'puntaje' : record['valoracion_comprador_puntaje'],
        'comentario' : record['valoracion_comprador_comentario'],
        'respuesta' : record['valoracion_comprador_respuesta']
    }
    operacion['valoracion_vendedor'] = {
        'id_valoracion' : record['valoracion_vendedor_id_valoracion'],
        'puntaje' : record['valoracion_vendedor_puntaje'],
        'comentario' : record['valoracion_vendedor_comentario'],
        'respuesta' : record['valoracion_vendedor_respuesta']
    }
    return operacion

operaciones_cur = pgsql.get_DictCursor("operaciones.sql")
facturas_cur = pgsql.get_DictCursor("facturas.sql")

# Debug
extras.clearScreen()
#print "Facturas:"
print "Operaciones:"
ops = operaciones_cur.fetchall()
operaciones = map(operacion_record_to_document, ops)
extras.prettyPrintJson2(operaciones)