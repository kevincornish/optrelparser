from db import get_vials, get_ampoules

def search_vials():
	search = input("Vial search:")
	get_vials(search)

def search_ampoules():
	search = input("Ampoule search:")
	get_ampoules(search)
