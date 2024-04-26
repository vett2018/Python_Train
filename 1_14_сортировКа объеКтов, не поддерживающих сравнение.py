from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "user ({})".format(self.user_id)

if __name__ == '__main__':
    users = [User(23), User(3), User(99), User(234), User(999)]
    print(users)

    sorted_1 = sorted(users, key=lambda u: u.user_id)
    print(sorted_1)

    """
    Вместо lambda можно применить альтернативный подход с использованием operator.attrgetter():
    """
    sorted_2 = sorted(users, key=attrgetter('user_id'))
    print(sorted_2)

    min_sorted = min(users, key=attrgetter('user_id'))
    print(f'min = {min_sorted}')