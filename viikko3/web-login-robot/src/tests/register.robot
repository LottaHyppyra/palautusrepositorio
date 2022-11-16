*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kayttajatunnus
    Set Password  salasana1
    Set Confirm  salasana1
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mo
    Set Password  salasana1
    Set Confirm  salasana1
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  kayttajatunnus
    Set Password  s
    Set Confirm  s
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatchin Password And Password Confirmation
    Set Username  kayttajatunnus
    Set Password  salasana1
    Set Confirm  salasana2
    Submit Credentials
    Register Should Fail With Message  Passwords not matching

*** Keywords ***
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirm
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}