/*
--
-- Intento 1
--
SELECT
   usuario.id_usuario, month_index
FROM
   usuario CROSS JOIN generate_series(1, 12) as month_index;
*/

/*
--
-- Intento 2
--
SELECT
	usuario.id_usuario,
	sum(comision) as monto_comisiones,
	count(suscripcion)*37 as monto_suscripciones,
	extract('month' from operacion.fecha)::int as mes
FROM
	operacion
INNER JOIN publicacion ON publicacion.id_publicacion=operacion.id_publicacion
LEFT JOIN usuario on usuario.id_usuario=publicacion.publicada_por
FULL JOIN suscripcion ON usuario.id_usuario=suscripcion.id_usuario
	AND extract('month' from operacion.fecha) = extract('month' from suscripcion.fecha_suscripcion)

GROUP BY 
	usuario.id_usuario,
	extract('month' from operacion.fecha)
*/

--
-- Intento 3
--
SELECT
    usuario.id_usuario,
    extract (month from fecha)::int as mes,
    sum(comisiones_suscripciones.suscripcion) as suscripciones,
    sum(comisiones_suscripciones.comision) as comisiones

FROM
    usuario

INNER JOIN 
    (SELECT
        id_usuario,
        fecha_suscripcion as fecha
        37.00 as suscripcion,
        0 as comision,
    FROM
        suscripcion
    UNION
    SELECT
        id_usuario,
        operacion.fecha
        0 as suscripcion,
        comision,
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
    extract (month from fecha)::int
