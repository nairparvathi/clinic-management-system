from flask import Flask, render_template
import os
from flask import request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlite3 import Error



app = Flask(__name__)


def create_connection(Patients):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(Patients)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Patients ")

        rows = cur.fetchall()
        print(rows)
    except Error as e:
        print(e)

    return conn

def create_connection(Patients):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('Patients')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            




def create_connection(Medicines):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(Medicines)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Medicines")

        rows = cur.fetchall()
        print(rows)
    except Error as e:
        print(e)

    return conn

def create_connection(Medicines):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('Medicines')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



def create_connection(Staff):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(Staff)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Staff")

        rows = cur.fetchall()
        print(rows)
    except Error as e:
        print(e)

    return conn

def create_connection(Staff):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('Staff')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            

def create_connection(Appointments):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(Appointments)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Appointments")

        rows = cur.fetchall()
        print(rows)
    except Error as e:
        print(e)

    return conn

def create_connection(Appointments):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('Appointments')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

db = SQLAlchemy(app)           

db = SQLAlchemy(app)
            
db = SQLAlchemy(app)

db = SQLAlchemy(app)

