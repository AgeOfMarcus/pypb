#!/usr/bin/python3

from flask import flask, request
import sqlite3

def sql(cmd):
	with sqlite3.connect("pastes.db") as db:
		res = db.cursor().execute(cmd).fetchall()
		db.commit()
	return res

def fixsql(lst):
	res = []
	for i in lst: res.append(i[0])
	return res
