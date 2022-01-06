first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}"
print(message)

# 3.5 or earlier
full_name = "{} {}".format(first_name, last_name)
print(full_name)
