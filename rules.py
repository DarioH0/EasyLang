import re

filename = open('code.el', 'r')
variables = {}

for line, command in enumerate(filename, 1):
     command = command.strip()

     # Comments
     if command.startswith('-') or not command.strip():
          pass

     elif command.casefold().startswith('var '):
          variable_name, variable_value = command[4:].replace(" ", "").split("=")
          variables[variable_name.strip()] = variable_value.strip()

     elif command.casefold().startswith('say '):
          variable_checker = re.findall(re.compile(r"{(\w+)}"), command)

          if variable_checker:
              for var in variable_checker:
                   print(variables[var])

          elif command.casefold().startswith('say '):
              print(command[4:].encode('raw_unicode_escape').decode('unicode_escape'))

     else:
          if command.casefold() == 'say':
               print('There\'s nothing to say! If you want to make a new line use the "\\n" method.')
          else:
               print(f'On line {line}, command was not recognised')
