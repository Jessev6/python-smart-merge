import json

def main():
    items = loadJson("input/minimal.json")
    result = merge_diff_values(items)
    saveJson("output/minimal.json", result)
    

def loadJson(filename):
    f = open(filename)
    return json.load(f)

# Expects array of objects with similar keys, merges into single object with all unique keys
def merge_diff_values(items):
    merged_object = {}

    for item in items:
        for key in item:
            if key not in merged_object:
                merged_object[key] = []
            if item[key] not in merged_object[key]:
                merged_object[key].append(item[key])

    # # extract props containing a single value out of the array
    for key in merged_object.keys():
        if len(merged_object[key]) == 1:
            merged_object[key] = merged_object[key][0]

    return merged_object

def saveJson(filename, content):
    f = open(filename, 'w')
    f.write(json.dumps(content, indent=4, sort_keys=True))
    f.close()

main()