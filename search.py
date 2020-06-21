from db import get_vials

def search_vials():
	search = input("Product search:")
	get_vials(search)

#def search_ampoules():
#	search = input("Product search:")
#	get_ampoules(search)

if __name__ == '__main__':
	search_vials()
