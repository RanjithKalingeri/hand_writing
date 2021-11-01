import torch
# import xml.etree.ElementTree as ET
# mytree = ET.parse(r'C:\Users\ranji\Desktop\project handwritting\compressed_data\xml\xml\a01-000u.xml')
# print(mytree)
#
# #getting root tag
# myroot = mytree.getroot()
# print(list(myroot))
# print(myroot.tag)
# print(myroot.attrib)
#
# #get tag of first child of root element
# print(myroot[0].tag)
#
# #getting attribute
# print(myroot[1][0].attrib)
#
# #looping through child tag to get text
# for x in myroot[1]:
#     print(x.tag, x.attrib)
#
# # #looping through child tag to get text
# # for x in myroot[1]:
# #     print(x.text)
#
# #looping through child tag by name to get text of particular attrib
# for x in myroot[1].findall('line'):
#     print(x.attrib['id'])

#
myx = torch.load(r'C:\Users\ranji\Desktop\project handwritting\implimentation\train_X')
myy = torch.load(r'C:\Users\ranji\Desktop\project handwritting\implimentation\train_Y_filename')

print(myy[12323])







