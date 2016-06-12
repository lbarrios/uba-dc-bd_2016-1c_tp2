# -*- coding: utf-8 -*-

def operacion_record_to_dict(record):
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
        'respuesta' : record['valoracion_comprador_respuesta'],
    }
    operacion['valoracion_vendedor'] = {
        'id_valoracion' : record['valoracion_vendedor_id_valoracion'],
        'puntaje' : record['valoracion_vendedor_puntaje'],
        'comentario' : record['valoracion_vendedor_comentario'],
        'respuesta' : record['valoracion_vendedor_respuesta'],
    }
    operacion['publicacion'] = {
        'id_publicacion': record['id_publicacion'],
        'titulo': record['titulo'],
        'descripcion': record['descripcion'],
        'fecha': record['fecha'],
        'id_tipo_publicacion': record['id_tipo_publicacion'],
        'publicada_por': record['publicada_por'],
        'tipo': record['tipo'],
        'tipo_publicacion': record['tipo_publicacion'],
    }
    return operacion

def factura_record_to_dict(record):
    factura = dict()
    factura['id'] = record['id_usuario']
    factura['mes'] = record['mes']
    factura['suscripciones'] = record['suscripciones']
    factura['comisiones'] = record['comisiones']
    return factura