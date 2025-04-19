# Welcome Stranger

# Create a function that takes 2 arguments, a list and a
# dictionary. The list will contain 2 or more elements that, when
# joined with spaces, will produce a person's name. The
# dictionary will contain two keys, "title" and "occupation", and
# the appropriate values. Your function should return a greeting
# that uses the person's full name, and mentions the person's
# title.

def get_full_name(name_list):
    names = []

    # check if names list contains empty string
    for name in name_list:
        if name != '':
            names.append(name.title())

    return (' ').join(names).strip()

def get_title(title_dict):
    job_title = title_dict.get('title', '')
    job_occupation = title_dict.get('occupation', '')

    if not job_title and not job_occupation:
        return ''

    return f"{job_title} {job_occupation}".strip()

def greetings(get_name, get_profession):
    full_name = get_full_name(get_name)
    profession = get_title(get_profession)

    if full_name == '':
        return "Hello Stranger! Care to introduce yourself!"

    return(f"Hello {full_name}! "
           f"Nice to have a {profession} around.")


GREETING1 = greetings(
    ["john", "q", "doe"],
    {"title": "Master", "occupation": "Plumber"},
)
GREETING2 = greetings(
    ["John", "Smith"],
    {"title": "Surgeon", "occupation": "General"},
)
GREETING3 = greetings(
    ["Jane", "Smith"],
    {"title": "Junior", "occupation": "Developer"},
)
GREETING4 = greetings(
    ["", ""],
    {"title": "", "occupation": ""},
)
print(GREETING1)
print(GREETING2)
print(GREETING3)
print(GREETING4)

# Hello John Q Doe! Nice to have a Master Plumber around.
# Hello John Smith! Nice to have a Surgeon General around.
# Hello Jane Smith! Nice to have a Junior Developer around.
# Hello Stranger! Care to introduce yourself!