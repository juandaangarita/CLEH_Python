def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Juan", "lastname": "Angarita"}

    super_list = [
        {"firstname": "Juan", "lastname": "Angarita"},
        {"firstname": "Daniel", "lastname": "Torres"},
        {"firstname": "Sebastián", "lastname": "Zapata"},
        {"firstname": "Adele", "lastname": "Adkins"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.3, 5.42],
    }

    for key, value in super_dict.items():
        print(key," - ",value)

    for values in super_list:
        for key, value in values.items():
            print(key, ": ", value)

    for values in super_list:
        print(values["firstname"], values["lastname"])


if __name__ =="__main__":
    run()