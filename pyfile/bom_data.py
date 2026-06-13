import json
bom_file = '/home/deepak/projects/practice/practice/datafile/bom_data.txt'
json_object=[]
with open (bom_file, 'r') as file:
    next(file)
    for line in file:
       line_item= line.split()
       if len(line_item)==4:
        row_object={
            'item': line_item[0],
            'sub_item': line_item[1],
            'quantity': int(line_item[2]),
            'price_per_unit': float(line_item[3])
        }
        json_object.append(row_object)
output = '/home/deepak/projects/practice/practice/datafile/bom_data.json'
with open ( output, 'w') as jf:
   json.dump(json_object,jf, indent=4)
print("Success in loading")



