def occurances(string, substr):
  
  stripped_string = string.replace(substr, '')
  
  return (len(string) - len(stripped_string)) // len(substr)


def occurances(string, substr):
  return string.count(substr)