import urllib.parse

def generate_link(user):
    user = urllib.parse.quote(user)
    return 'http://www.codewars.com/users/'+ user