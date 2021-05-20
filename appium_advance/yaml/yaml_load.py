import yaml

#yaml数据读取
file=open('familyInfo.yaml', 'r')
data=yaml.load(file,Loader=yaml.FullLoader)

print(data)

print(data['name'])
print(data['age'])

print(data['spouse'])
print(data['spouse']['name'])
print(data['spouse']['age'])

print(data['children'])
print(data['children'][0]['name'])
print(data['children'][0]['age'])

print(data['children'][1]['name'])
print(data['children'][1]['age'])


#yaml数据变量临时修改 不涉及修改文件
data['name']='51zxw'
print(data['name'])
#51zxw