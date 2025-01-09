def occurances(string, substr):
  # remove each occuance of substr
  stripped_string = string.replace(substr, '')
  # compute based on length of the strings
  return (len(string) - len(stripped_string)) // len(substr)

# Python actually has a method to solve this too!
def occurances(string, substr):
  return string.count(substr)