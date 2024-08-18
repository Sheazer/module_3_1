calls = 0


def count_call():
    global calls
    calls += 1


def string_info(s):
    count_call()
    return len(s), s.upper(), s.lower(),


def is_contains(s, list_def):
    count_call()
    for word in list_def:
        if word.lower() == s.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
