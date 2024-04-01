


def find_element(element):
    phone_input = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located(element))
    return phone_input