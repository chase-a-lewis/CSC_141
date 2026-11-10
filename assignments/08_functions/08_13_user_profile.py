def build_profile(first, last, **user_info):

    """Build a dictionary containing everything we know about a user."""
    user_info['Chase'] = first
    user_info['Lewis'] = last
    return user_info

user_profile = build_profile('Chase', 'Lewis',
                            location='home',
                            field='Computer Science')
print(user_profile)