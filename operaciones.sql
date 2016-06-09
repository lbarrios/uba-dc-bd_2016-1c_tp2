SELECT
       *
FROM
       operacion
WHERE operacion.fecha < (localtimestamp - interval '1 month');