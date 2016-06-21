SELECT
    usuario.id_usuario,
    mes,
    sum(comisiones_suscripciones.suscripcion) as suscripciones,
    sum(comisiones_suscripciones.comision) as comisiones

FROM
    usuario

INNER JOIN 
    (SELECT
        suscripcion.id_usuario,
        extract (month from fecha_suscripcion)::int as mes,
        37.00 as suscripcion,
        0 as comision
    FROM
        suscripcion
    UNION
    SELECT
        usuario.id_usuario,
        extract (month from operacion.fecha)::int as mes,
        0 as suscripcion,
        operacion.comision
    FROM
        operacion
        INNER JOIN
            publicacion
            ON publicacion.id_publicacion=operacion.id_publicacion
        INNER JOIN
            usuario
            ON usuario.id_usuario=publicacion.publicada_por
    ) AS comisiones_suscripciones
    ON comisiones_suscripciones.id_usuario=usuario.id_usuario

GROUP BY
    usuario.id_usuario,
    comisiones_suscripciones.mes
