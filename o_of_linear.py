def find_name(papers, name):
    for paper in papers:
        if (paper == name):
            return True
    return False

papers = ["Reshmi", "Farhana", "Tanisha", "Sadia", "Kabil", "Gumramuku"]
name = "Farhana"

result = find_name(papers, name)

if result:
    print("Paper Found")
else: 
    print("Paper Not found!")