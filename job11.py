#Créer un programme job11.py qui parcourt le contenu du fichier “domains.xml” et 
#qui compte le nombre d’extension de domaines qui s’y trouvent (.com, .net, etc ...).


from xml.dom import minidom

doc = minidom.parse('domains.xml')
elements = doc.getElementsByTagName("column")
newList = []

for element in elements:
    if element.getAttribute("name") == "domain":
        newList.append(element.childNodes[0].data)

print(len(newList))