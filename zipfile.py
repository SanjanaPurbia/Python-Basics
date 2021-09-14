from zipfile import ZipFile

examplezip=ZipFile("C:\\Users\\LENOVO\\Downloads\\Artificial Intelligence (AI)-20210711T152405Z-001.zip")
files=examplezip.namelist()
print(files)