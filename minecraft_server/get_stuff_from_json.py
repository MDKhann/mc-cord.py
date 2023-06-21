import json

def get_category_entries(filename, main_category, mode="single"):
    with open(filename, 'rb') as f:
        data = json.load(f)

    entries = []
    for key, value in data.items():
        categories = key.split('.')
        if categories[0] == main_category and mode == "single":
            entries.append(value)
        elif key.startswith(main_category) and mode == "multi":
            entries.append(value)

    return entries

def filter_out_vars(obj_list, filter_out=[]):
    # sourcery skip: default-mutable-arg
    filtered_list = []
    for obj in obj_list:
        replaced_obj = obj
        for filterer in filter_out:
            replaced_obj = replaced_obj.replace(filterer, "")
        filtered_list.append(replaced_obj)
    return filtered_list

entries = get_category_entries('./minecraft_server/en_us.json', 'death')
for i in range(len(entries)):
    print(f"{(i + 1)}. {entries[i]}")
filtered = filter_out_vars(entries, ["%1$s","%2$s","%3$s","%4$s"])
for i in range(len(filtered)):
    print(f"{(i + 1)}. {filtered[i]}")
