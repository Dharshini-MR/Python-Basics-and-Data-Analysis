# WEEK 2 - Data Structures and Functions

# ---------- Hands-on: data structures ----------
fruits = ["apple", "banana", "apple"]          # list: ordered, can hold repeats, can be changed
point = (3, 4)                                 # tuple: ordered but cannot be changed
person = {"name": "Asha", "age": 21}           # dictionary: key -> value pairs
unique = set(fruits)                           # set: keeps only unique items
print(fruits, point, person, unique)           # show all four structures

# ---------- Hands-on: functions ----------
def sum_of_squares(numbers):                   # function: takes a list, returns a result
    return sum([n * n for n in numbers])       # list comprehension squares each number, sum adds them
print("Sum of squares:", sum_of_squares([1, 2, 3, 4]))   # 1+4+9+16 = 30

square = lambda x: x * x                       # lambda: a one-line function without a name
print("Square of 7:", square(7))               # use the lambda

def factorial(n):                              # recursion: a function that calls itself
    if n <= 1:                                 # base case stops the recursion
        return 1
    return n * factorial(n - 1)                # smaller problem: n! = n * (n-1)!
print("5! =", factorial(5))                    # 120

evens = [n for n in range(1, 11) if n % 2 == 0]   # filtering with a list comprehension
print("Even numbers:", evens)                  # [2, 4, 6, 8, 10]

# ---------- Client project: data cleaning ----------
records = [                                    # raw data: (name, city, age); has duplicates and a missing age
    ("Asha", "Mumbai", 25),
    ("Ravi", "Delhi", 17),
    ("Asha", "Mumbai", 25),                    # duplicate of the first record
    ("Meena", "Pune", None),                   # missing age
    ("John", "Mumbai", 34),
    ("Ravi", "Delhi", 17),                     # duplicate of the second record
]
print("Raw records:", len(records))            # size before cleaning

no_duplicates = list(dict.fromkeys(records))   # dict keys are unique, so this removes duplicates and keeps order
print("After removing duplicates:", len(no_duplicates))

with_age = [r for r in no_duplicates if r[2] is not None]   # drop records whose age is missing
print("After removing missing ages:", len(with_age))

adults = [r for r in with_age if r[2] >= 18]   # filter: keep only people aged 18 or more
print("Cleaned data (adults):", adults)        # final result
