# Class List Manager - Group 2
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====
# Written by: Lama Alsumikhi 446203280 (task 1)
def count_names(names):
    return len(names)
    
# Written by: Danah Alfallaj 446201945 (task 2)
def search_name(names, name):
    return name in names
    
# Written by: Maha alsultan 446203568 (task 5)
def names_starting_with(names, letter):
    result = []
    for name in names:
        if name.startswith(letter):
            result.append(name)
    return result
#written by :latifa-446204298(task 3) 
def sort_names(names):
   return sorted(names) 

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Search result:", search_name(names, "Danah"))
    print("Names starting with L:", names_starting_with(names, "L"))
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))


main()

