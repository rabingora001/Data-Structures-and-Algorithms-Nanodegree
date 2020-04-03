# Definition of the generator to produce even numbers & store it in a variable
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)
print('Other Processing')

# Now go back to generating more even numbers.
for i in range(5):
    print(next(my_gen))

# And more...
print('And ten more...')
for i in range(10):
    print(next(my_gen))