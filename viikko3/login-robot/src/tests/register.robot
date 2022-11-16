*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  nimi  salasana!
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana!
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  mo  salasana!
    Output Should Contain  Username must contain at least 4 characters

Register With Valid Username and Too Short Password
    Input Credentials  nimi  sala
    Output Should Contain  Password must contain at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  nimi  salasana
    Output Should Contain  Password must contain at least 1 other character than letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command

