sudo usermod -aG docker $USER
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

print(pair_match(''))