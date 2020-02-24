# 0x06. Regular expression

## Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

# 0. Simply matching Holberton
Requirements:

* The regular expression must match Holberton
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.

# 1. Repetition Token #0
Requirements:

*  Find the regular expression that will match the below cases:

    hbn
    hbtn
    `**hbttn**`
    `**hbtttn**`
    `**hbttttn**`
    hbtttttn

# 2. Repetition Token #1 
Requirements:

*  Find the regular expression that will match the below cases:

    `**htn**`
    `**hbtn**`
    hbbtn
    hbbbtn

# 3. Repetition Token #2
Requirements:

* Find the regular expression that will match the below cases:


    hbn
    `**hbtn**`
    `**hbttn**`
    `**hbtttn**`
    `**hbttttn**`

# 4. Repetition Token #3
Requirements:

* Find the regular expression that will match the below cases:


    **hbn**
    hbon
    `**hbtn**`
    `**hbttn**`
    `**hbtttn**`
    `**hbttttn**`
# 5. Not quite HBTN yet
Requirements:

* The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between

# 6. Call me maybe
Requirement:

* The regular expression must match a 10 digit phone number
Example:


    sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e 
    4155049898$ 
    sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e 
    $
    sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e 
    $
    sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
    $
    sylvain@ubuntu$


# 7. OMG WHY ARE YOU SHOUTING?
Requirement:

* The regular expression must be only matching: capital letters


    sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
    ILOVESYSADMIN$
    sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
    WHATSAY$
    sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
    $
    sylvain@ubuntu$
