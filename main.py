text = open("in.txt").read()
listt = text.split(" ")
newList = list()
first = "<b>"
last = "</b>"

for x in listt:
    if len(x) == 1:
        a = first+x+last
    else:
        yari = round(len(x)/2)
        a = first+x[0:yari]+last+x[yari:len(x)]
    newList.append(a)

newText = " ".join(item for item in newList)

html = f"""<html>
<head>
</head>
<body>
    <p>{newText}</p>
</body>
</html>"""

with open("index.html","a") as file:
    file.write(html)
    