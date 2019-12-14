import pickle


def save_routes(routes):
    file_name = 'routes.data'
    data = {}
    try:
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
    except:
        pass
    key = ''
    start_indexes = []
    for i in range(len(routes)):
        start_indexes.append(len(key))
        key += routes[i]
    destination_index = start_indexes.pop()
    destination = key[destination_index:]
    for index in start_indexes:
        route = key[index:destination_index]
        if route not in data:
            data[route] = {}
        if destination not in data[route]:
            data[route][destination] = 0
        data[route][destination] += 1
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


result = set()
data = None


def get_recomended_destinations(original_routes, routes):
    global result, data
    if data == None:
        file_name = 'routes.data'
        data = {}
        try:
            with open(file_name, 'rb') as f:
                data = pickle.load(f)
        except:
            pass
    keys = ''
    for i in range(len(routes)):
        keys += routes[i]
    if keys in data:
        links = sorted(data[keys].items(), key=lambda item: item[1])
        for (link, _count) in links:
            result.add(link)
            result = result - original_routes
            if len(result) == 8:
                break
    if len(result) == 8 or len(routes) == 1:
        dd = list(result)
        result = set()
        data = None
        return dd
    return get_recomended_destinations(original_routes, routes[1:])


def save_title(title, link):
    file_name = 'title.data'
    data = {}
    try:
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
    except:
        pass
    if link in data:
        return
    data[link] = title
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


def get_title(link):
    file_name = 'title.data'
    data = {}
    try:
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
    except:
        pass
    if link in data:
        return data[link]
    return ''
