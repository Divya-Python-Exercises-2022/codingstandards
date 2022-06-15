def my_custom_validation_function(one=False, two=False, three=False,
                                  four=False,
                                  five=False, six=True, seven=True, eight=True,
                                  nine=True, ten=True):
    # Checking arguments
    if [one, two, three, four, five, six, seven, eight, nine, ten] == \
            [True, True, True, True, True, False, False, False, False, False]:
        print('OK')  # arguments are ok


if __name__ == '__main__':

    my_custom_validation_function(True, True, True, True, True,
                                  False, False, False, False, False)
