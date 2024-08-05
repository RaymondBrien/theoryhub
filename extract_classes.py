import re
from glob import glob

# Path to your templates directory
template_files = glob('templates/**/*.html', recursive=True)

class_set = set()

# Regex to match class attributes
class_regex = re.compile(r'class="([^"]+)"')

for file_path in template_files:
    with open(file_path, 'r') as file:
        content = file.read()
        matches = class_regex.findall(content)
        for match in matches:
            classes = match.split()
            class_set.update(classes)

# Print unique class names
print("Custom Classes Used in Templates:")
for class_name in sorted(class_set):
    print(class_name)