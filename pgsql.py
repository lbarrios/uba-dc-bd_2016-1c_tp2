# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
import extras

def get_pg_connection():
    """	Returns the pg_connection descriptor.
    To run this function, please first be sure to configure the tunnel
    to the pgsql[@bbdd.azure...] server to be listening on port 5432
    """
    try:
        conn=psycopg2.connect("dbname='bbdd' user='bbdd' host='localhost'")
    except:
        extras.error("I am unable to connect to the pgsql database.")
    return conn

def get_DictCursor(sql_file):
    """ Given a SQL file path, retrieves the query contained in it and
    returns the pyscopg.DictCursor object representing the result
    """
    conn = get_pg_connection()
    dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query_pg_file = open(sql_file, "r")
    query_pg = query_pg_file.read()
    query_pg_file.close()
    try:
        dict_cur.execute(query_pg)
    except Exception as err:
        extras.error("I can't SELECT from query %s\nError: %s\nQuery:\n%s"%(sql_file,err,query_pg))
    return dict_cur

def get_RealDictCursor(sql_file):
    """ Given a SQL file path, retrieves the query contained in it and
    returns the psycopg.RealDictCursor object representing the result
    """
    conn = get_pg_connection()
    dict_cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    query_pg_file = open(sql_file, "r")
    query_pg = query_pg_file.read()
    query_pg_file.close()
    try:
        dict_cur.execute(query_pg)
    except Exception as err:
        extras.error("I can't SELECT from query %s\nError: %s\nQuery:\n%s"%(sql_file,err,query_pg))
    return dict_cur
