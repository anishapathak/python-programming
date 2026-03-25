d1 = {'user': {'id': 1, 'settings': {'theme': 'dark'}}, 'version': '1.0', 'xzy': 1}
d2 = {'user': {'settings': {'font': 'serif'}}, 'version': '1.1' }


# Output: {'user': {'id': 1, 'settings': {'theme': 'dark', 'font': 'serif'}}, 'version': '1.1'}


# 1. for every key in d1
#     2. check if key exist in d2
#     3 if no just add it in output_dict (keya nd value)
#     4. if yes 
#     5. if value of key is a dict call function (d1['user'], d2['user'])


def merge_dict(d1, d2):
    output_dict {}
    for key in d1:
         if key in d1.values():
             if type(d1[key]) == 'dict' and type(d2[key]) == 'dict' :
                 output_dict[key] = merge_dict(d1[key], d2[key])
             else:
                 output_dict[key] = d1[key] 
         else:
             output_dict[key] = d1[key]
    return output_dict    




  






