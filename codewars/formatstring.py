def namelist(names):
    if len(names) < 1:
        return ''
    if len(names) >= 1:
        ret = ""
        for i,n in enumerate(names):
        	if i == 0:
        		ret += f"{n['name']}"
        	elif i == len(names)-1:
        		ret += f" & {n['name']}"
        	else:
        		ret += f", {n['name']}"
        return ret


print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'},{'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))