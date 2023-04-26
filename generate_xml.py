from lxml import etree

root = etree.Element("root")
child1 = etree.SubElement(root, "child1")
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")
result = etree.tostring(root, pretty_print=True)#.decode('utf-8')
with open("result.xml","wb") as f:
    f.write(result)
