import csv, urllib.request, re

#TODO: Create a function that's called at start of the program, which asks for file input and returns the fields/data

# This creates a new file. Create the path and name the headers.
def create_file(file_name, my_fields):
    with open(file_name, 'w') as csv_file:
        file = csv.DictWriter(csv_file, fieldnames=my_fields, lineterminator='\n')
        file.writeheader()
        print("Successfully created file:", file_name, "with fields:", my_fields)

# Feed in the filename you're looking to add to, and the data. Data must be an array.
def write_file(file_name, row_input):
    try:
        with open(file_name, 'r') as csv_file:
            file = csv.reader(csv_file).__next__()
            if len(file) > 0:
                field_names = file
                csv_file.close()
                with open(file_name, 'a') as csv_append:
                    file = csv.DictWriter(csv_append, fieldnames=field_names, lineterminator='\n')
                    file.writerow(row_input)
    except FileNotFoundError:
        print('File:', file_name, 'was not found. Use create_it() to create a new file.')


def grab_tags(url):
    url_obj = urllib.request.urlopen(url).read().decode('utf-8')

    js_re = re.findall(r"/{2}(.+\.js[\?.*]?)[\"|\']", url_obj)
    #ir = js_re.insert(0, url)
    return js_re

def collect_tags(file_name, url):
    t = grab_tags(url)
    for i in t:





#data = ["those", "these"]
#fields = ['url', 'tag']
#create_file('test.csv', fields)
#write_file('test.csv', data)

x = grab_tags('http://multuple.com/')
print(x[0], x[1])