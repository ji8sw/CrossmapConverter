import re
InCrossmap = ""

def format_hex_values(input_string):
    hex_values = re.findall(r'0x[0-9A-Fa-f]+', input_string)
    formatted_values = []  # Store formatted values as a list
    for i in range(0, len(hex_values), 2):  # Process values in pairs
        formatted_pair = '{' + ', '.join(hex_values[i:i+2]) + '},'
        formatted_values.append(formatted_pair)
    formatted_output = '\n'.join(formatted_values)  # Join pairs with newlines
    return formatted_output

with open(input("Raw Crossmap: "), 'r') as InFile:
        InCrossmap = InFile.read()

with open(input("Formatted Crossmap: "), 'w') as OutFile:
        OutFile.write(format_hex_values(InCrossmap))
        
formatted_result = format_hex_values(InCrossmap)
print(formatted_result)
