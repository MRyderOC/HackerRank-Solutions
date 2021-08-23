import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    
    if len(elem) >= 0: # Making sure the element is not an empty string
        level += 1 # Since it's not empty add a level
        
        if level >= maxdepth: # If this level is deeper than previous one assign new one to maxdepth
            maxdepth = level
        
        for child in elem: # Recursive-like procedure
            depth(child, level)



if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
