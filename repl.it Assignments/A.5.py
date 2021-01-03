def get_files():
    n = int(input())
    files = {}
    for i in range(n):
        file = input().split()
        files[file[0]] = set(file[1:])
    return files

def get_operations():
    n = int(input())
    operations = []
    for i in range(n):
        operations.append(input().split())
    return operations

def determine_rights(filesDict, operations):
    rightskey = {'write':'W', 'read':'R', 'execute':'X'}

    accessRights = []
    for o in operations:
        if rightskey[o[0]] in filesDict[o[1]]:
            accessRights.append('OK')
        else:
            accessRights.append('Access denied')
    return accessRights


def run():
  accessRights = determine_rights(get_files(), get_operations())
  for right in accessRights:
    print(right)

def test():
    print(determine_rights({'goodluck': {'W', 'X'}}, [['read', 'goodluck']]) ==
        ['Access denied'])
    print(determine_rights({'goodluck': {'R', 'W', 'X'}}, [['read', 'goodluck']]) ==
        ['OK'])
    print(determine_rights({'helloworld.exe':{'R', 'X'}, 'pinglog':{'W', 'R'},
        'nya':{'R'}, 'goodluck':{'X', 'W', 'R'}}, [['read', 'nya'], ['write', 'helloworld.exe'],
        ['execute', 'nya'], ['read', 'pinglog'], ['write', 'pinglog']])
        == ['OK', 'Access denied', 'Access denied', 'OK', 'OK'])

test()
# run()
