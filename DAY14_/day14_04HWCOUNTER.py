def counter_factory():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter1 = counter_factory()

print(counter1())
print(counter1())
print(counter1())

counter2 = counter_factory()

print(counter2())
print(counter2())