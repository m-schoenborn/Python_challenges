#opening files
input_file = "input.txt"
output_file = "output.txt"
errors_file = "errors.txt"

s = 0

with open(input_file, 'r') as f_r, \
    open(errors_file, 'w') as f_e:
        for l in f_r.readlines():
            if l[:-1].isnumeric():
                s += int(l)
            else:
                f_e.write(l)

with open(errors_file, 'r') as f:
     message = f.read()

print(message)

