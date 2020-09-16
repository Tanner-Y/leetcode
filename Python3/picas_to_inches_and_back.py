# this is actually something I did on my own for graphic design purposes, but I didn't feel it needed its own repo.
def convert_to_picas(inches):
	picas = int((inches*6)//1)
	points = int(((inches*6)%1)*12)
	return f"{picas}p{points}"
  
def convert_to_inches(picas):
	inches = picas.split("p")
	return (int(inches[0])/6)+(int(inches[1])/12)
