SELECT
    operacion.id_operacion,
    operacion.comision,
    publicacion.precio,
    publicacion.publicada_por,
    operacion.id_comprador,
    valoracion_comprador.id_valoracion as valoracion_comprador_id_valoracion,
    valoracion_comprador.puntaje as valoracion_comprador_puntaje,
    valoracion_comprador.comentario as valoracion_comprador_comentario,
    valoracion_comprador.respuesta as valoracion_comprador_respuesta,
    valoracion_vendedor.id_valoracion as valoracion_vendedor_id_valoracion,
    valoracion_vendedor.puntaje as valoracion_vendedor_puntaje,
    valoracion_vendedor.comentario as valoracion_vendedor_comentario,
    valoracion_vendedor.respuesta as valoracion_vendedor_respuesta,
    publicacion.id_publicacion,
    publicacion.titulo,
    publicacion.descripcion,
    publicacion.fecha,
    publicacion.id_tipo_publicacion,
    publicacion.tipo,
    CASE 
        WHEN EXISTS (SELECT * from servicio where id_publicacion=publicacion.id_publicacion) THEN 
            CASE WHEN EXISTS (SELECT * FROM articulo WHERE id_publicacion=publicacion.id_publicacion) THEN
                'mixta'
            ELSE
                'servicio'
            END
        ELSE 'articulo'
    END as tipo_publicacion

FROM
    operacion

INNER JOIN publicacion
   ON operacion.id_publicacion = publicacion.id_publicacion

LEFT JOIN valoracion as valoracion_comprador
   ON valoracion_comprador.id_operacion = operacion.id_operacion
      AND valoracion_comprador.tipo = 'comprador'

LEFT JOIN valoracion as valoracion_vendedor
   ON valoracion_vendedor.id_operacion = operacion.id_operacion
      AND valoracion_vendedor.tipo = 'vendedor'

WHERE
   operacion.fecha < (localtimestamp - interval '1 month');