# Return the count of how many times the sub-string “Katie” appears in the given string

str = "Katie is good developer. Katie is a writer"

# Primera forma
def some_times(string):
    return string.count("Katie") # 2

print(some_times(str))

# Segunda forma
str_count = str.count("Katie")
print(str_count) # 2