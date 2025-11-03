linguagens = ["Python", "Java", "C++"]
linguagens.sort()
print(linguagens)  # ['C++', 'Java', 'Python']

linguagens = ["Python", "Java", "C++"]
linguagens.sort(reverse=True)
print(linguagens) # ['Python', 'Java', 'C++']

linguagens = ["Python", "Java", "C++", "C", "js"]
linguagens.sort(key=lambda x: len(x))
print(linguagens) # ['C', 'js', 'Java', 'C++', 'Python']

linguagens = ["Python", "Java", "C++", "C", "js"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens) # ['Python', 'Java', 'C++', 'js', 'C']