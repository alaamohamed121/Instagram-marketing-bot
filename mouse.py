with open('users.txt', 'r') as f:
    lines = f.readlines()

modified_lines = [line.strip() + ' ' for line in lines]

result = ''.join(modified_lines)

with open('out.txt', 'w') as f:
    f.writelines(result)
