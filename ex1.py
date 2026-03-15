personal_info_dict: dict = {
    "name": "",
    "email": "",
    "phone": "",
    "job title": "",
}
temp = input("Please enter your name: ")
personal_info_dict["name"] = temp
temp = input("Please enter your email: ")
personal_info_dict["email"] = temp
temp = input("Please enter your phone: ")
personal_info_dict["phone"] = temp
temp = input("Please enter your job title: ")
personal_info_dict["job title"] = temp
print(personal_info_dict)

print()
print("--- Business card ---")
print(f"Name: {personal_info_dict['name']}")
print(f"Email: {personal_info_dict['email']}")
print(f"Phone: {personal_info_dict['phone']}")
print(f"Job title: {personal_info_dict['job title']}")