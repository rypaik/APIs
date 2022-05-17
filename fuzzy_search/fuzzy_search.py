from thefuzz import fuzz, process


s1 = "Hello World"
s2 = "helloworld"
print(s1 is s2)
print(s1.lower() == s2)


s3 = "Jsut a test and this is a long string"
s4 = "Just a test and this is a long strinf"

print(fuzz.ratio(s3, s4))


s5 = "Just a test"
s6 = "Just a test and some more"

print(fuzz.partial_ratio(s5, s6))
# returns 100


s7 = "Hello World is what I want to tell you"
s8 = "What I want to tell you is Hello World"


print("Fuzz Ratio is: ")
print(fuzz.ratio(s7, s8))
print("Fuzz Partial Ratio is: ")
print(fuzz.partial_ratio(s7, s8))
print("Fuzz Token Sort Ratio is: ")
print(fuzz.token_sort_ratio(s7, s8))
print("Fuzz Token Set Ratio is: ")
print(fuzz.token_set_ratio(s7, s8))


# List Example


things = [
    "Programming Language",
    "Native Language",
    "React Native",
    "Some Stuff",
    "Hello World",
    "Coding and Stuff",
]

print(process.extract("programming", things, limit=2))
print(process.extractOne("programming", things))


books = [
    "The Python Bible Volume 1 - Beginner",
    "The Python Bible Volume 2 - Intermediate",
    "The Python Bible Volume 3 - Data Science",
    "The Python Bible Volume 4 - Machine Learning",
    "The Python Bible Volume 5 - Finance",
    "The Python Bible Volume 6 - Neural Networks",
    "The Python Bible Volume 7 - Computer Vision",
    "The Java Bible - Beginner",
    "Other",
    "Some Network Book",
]

print(process.extract("python data science", books, limit=3))
print(
    process.extract("python data science", books, limit=3, scorer=fuzz.token_sort_ratio)
)
