from flask import g

# Utility function to get the current user's ID
def get_user_id():
    return g.user.id

def is_admin():
    return "Admin" in [role.name for role in g.user.roles]
