try:
with open("example.txt", "w") as file:
data=file.write("hello python")
print(data)
execpt exeption as e:
print("there is errror in your inputs check your inputs")
#finally block always execute no matte what
finally:
file.close()
    