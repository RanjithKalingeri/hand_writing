import xml.etree.ElementTree as ET
import os
import torch
from torchvision import transforms
import cv2
#
# j =0
# id_list = []
# train_x_list = []
#
# rootdir = r'C:\Users\ranji\Desktop\project handwritting\iamdata\xml\xml'
# all_xml_files  = os.listdir(rootdir)
# print(len(all_xml_files))
#
# for filename in all_xml_files:
#     file_path = os.path.join(rootdir, filename)
#     # print(file_path)
#     mytree = ET.parse(file_path)
#     myroot = mytree.getroot()
#     for x in myroot[1].findall('line'):
#         templis = []
#         s = x.attrib['text']
#         n = len(s)
#         # print('lenght of string is ' + str(n))
#         for i in range(40):
#             if i >= n:
#                 templis.append([0])
#             else:
#                 # print(ord(s[i]))
#                 templis.append([ord(s[i])])
#         for key in x.attrib:
#             if key == 'id':
#                 id_list.append(x.attrib[key])
#                 continue
#             if key == 'text':
#                 continue
#             if key == 'segmentation':
#                 continue
#             templis.append([int(x.attrib[key])])
#
#         train_x_list.append(templis)
#     print('just now proccessed ' + str(j))
#     j= j+1
#
# train_x_list_tensor = torch.Tensor(train_x_list)
# torch.save(train_x_list_tensor, r'C:\Users\ranji\Desktop\project handwritting\implimentation\train_X')
# torch.save(id_list, r'C:\Users\ranji\Desktop\project handwritting\implimentation\train_Y_filename')
# print(len(train_x_list_tensor))
# print(len(id_list))


my_filenames = torch.load(r'C:\Users\ranji\Desktop\project handwritting\implimentation\train_Y_filename')
#C:\Users\ranji\Desktop\project handwritting\iamdata\lines (2)\lines (2)\a01\a01-000u\a01-000u-00.png
#C:\Users\ranji\Desktop\project handwritting\iamdata\lines (2)\lines (2)\a01\a01-000u\a01-000u-00.png

rootdirec = r'C:\Users\ranji\Desktop\project handwritting\iamdata\lines (2)\lines (2)'

train_y_list = []
j = 0
for filename in my_filenames[0:5000]:
    l = filename
    s1 = ''
    s2 = ''
    s = ''
    for i in range(len(l)):
        if l[i] == '-':
            s1 = s2
            s2 = s
        s = s + l[i]
    s = s + '.png'
    file = os.path.join(rootdirec, s1)
    file = os.path.join(file, s2)
    file = os.path.join(file, s)
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (1600, 100))
    # print(gray)  # Resize image
    gray_tensor = torch.Tensor(gray)
    # print(gray_tensor)
    # print(gray_tensor.size())
    train_y_list.append(gray_tensor)
    print(' proccessed image ' + str(j))
    j= j+1

print(len(train_y_list))
final3d_tensor = torch.stack(train_y_list, dim=0)
# print(final3d_tensor)

torch.save(final3d_tensor, r'C:\Users\ranji\Desktop\project handwritting\implimentation\train_Y_notnormalized_5000')
# train_y = torch.load(r'C:\Users\ranji\Desktop\project handwritting\implimentation\train_Y_')

