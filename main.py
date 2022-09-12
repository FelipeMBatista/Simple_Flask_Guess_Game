class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def auth_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

@auth_decorator
def create_blog_post(user, test):
    print(f"This is {user.name}'s new blog post! {test}")

new_user = User("Felipe")
new_user.is_logged_in = True
create_blog_post(new_user)