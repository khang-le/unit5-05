#!/usr/bin/env python3

# Created by : Khang Le
# Created on : September 2019
# This program prints out your name, using default function parameters


def full_address(first_name, last_name, street_address, city, province,
                 postal_code, apt_number=None):
    # return full address format
    full_address = first_name
    if apt_number is not None:
        full_address = ("\n" + full_address + " " + last_name + "" +
                        street_address + "" + city + " " +
                        province + " " + postal_code + "  " + apt_number)
    elif apt_number is None:
        full_address = ("\n" + full_address + " " + last_name + "" +
                        street_address + "" + city + " " +
                        province + " " + postal_code)

    return full_address.upper()


def main():
    # get user informations

    apt_number = None
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ") + "\n"
    street_address = input("Enter your address: ") + "\n"
    question = input("Do you have an ap.number? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter your apt.number here: ") + "\n"
    city = input("Enter your current city: ")
    province = input("Enter your current province: ") + " "
    postal_code = input("Enter your postal code: ")
    if apt_number is not None:
        address = full_address(first_name, last_name, street_address,
                               city, province, postal_code, apt_number)
    else:
        address = full_address(first_name, last_name, street_address,
                               city, province, postal_code)
    print(("Your shipping informations: {}").format(address))


if __name__ == "__main__":
    main()
