--SELECT
--   usuario.id_usuario, month_index
--FROM
--   usuario CROSS JOIN generate_series(1, 12) as month_index;

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