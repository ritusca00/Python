# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:06:37 2019

@author: blizn
"""

import sqlite3

def create_table():
    conn= sqlite3.connect("d:\GITHUB\Python\sqlite_app\lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists store (item TEXT, quality INTEGER, price REAL)")
    conn.commit()
    conn.close()
    
def insert(item, quality, price):
    conn= sqlite3.connect("d:\GITHUB\Python\sqlite_app\lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quality, price))
    conn.commit()
    conn.close()
    
#insert("Water Glass", 8, 5)
#insert("Coffe Cup", 10, 5.5)

def view():
    conn= sqlite3.connect("d:\GITHUB\Python\sqlite_app\lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * from store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn= sqlite3.connect("d:\GITHUB\Python\sqlite_app\lite.db")
    cur = conn.cursor()
    cur.execute("delete from store where item=?",(item,))
    conn.close()

def update(item, quality, price):
    conn= sqlite3.connect("d:\GITHUB\Python\sqlite_app\lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quality=?, Price=? WHERE item = ?",(item, quality, price))
    conn.close()
    
    
#insert("Wine Glass", 11, 5.5)
delete("Coffe Cup")   
update("Wine Glass", 11, 11.5)
print(view())