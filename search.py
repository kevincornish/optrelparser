from db import get_vials, get_ampoules

def search_vials():
	search = input("Batch number: ")
	get_vials(search)

def search_ampoules():
	search = input("Batch number: ")
	get_ampoules(search)
