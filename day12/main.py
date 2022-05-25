# Create letters using names in name dir 

with open("letters/test_letter.txt", "r") as file:
    text = file.readlines()

with open("names/test_names.txt", "r") as file:
    names = file.readlines()

for name in names:
    name = name.strip("\n")
    with open(f"ready2send/letter_for_{name}.txt", "w") as file:
        text[0] = text[0].replace("[name]", name)     
        file.writelines(text)
        text[0] = text[0].replace(name, "[name]") 