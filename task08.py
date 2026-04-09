user = {
    "name": "Jasur",
    "email": "jasuruktamov@gmail.com"
}

if not user["email"].endswith("@email.com"):
    user.update({"email": "jasuruktamov@email.com"})

print(user) 