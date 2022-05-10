def pair_match(men, women):

    age_min = 99999
    names_min = ("a", "b")

    for key, value in men.items():
        for w_key, w_value in women.items():

            d_keys = (key, w_key)
            age_deff = abs(value - w_value)
            if age_min > age_deff:

                names_min = d_keys
                age_min = age_deff

    return names_min


men = {"John": 20, "Abraham": 45}
women = {"July": 18, "Kim": 28}

print(pair_match(men, women))

    #
# d = {"":""}
# man_list = list(d.values())
# women_list = list(d.values())
# man_l_k = list(d.keys())
# women_l_k = list(d.keys())
#
#
#
# for man_list in d:
#
# abs(John - Kim) = abs(20 - 26) = abs(-6) = 6
# abs(John - July) = abs(20 - 18) = abs(2) = 2
# abs(Abraham - Kim) = abs(45 - 26) = abs(19) = 19
# abs(Abraham - July) = abs(45 - 18) = abs(27) = 27
#
