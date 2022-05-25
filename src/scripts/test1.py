#Hello World 1
def _get_data(path):
    file = open(path, 'r')
    data = file.readlines()
    print(data)
    file.close()
