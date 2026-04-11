def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    active_users = []
    for username, info in users.items():
        if info["active"]:
            active_users.append(username)
    return active_users

users = {
    "alice": {"active": True, "email": "alice@example.com"},
    "bob": {"active": False, "email": "bob@example.com"},
    "charlie": {"active": True, "email": "charlie@example.com"}
}

active_users = get_active_users(users)
print(active_users)