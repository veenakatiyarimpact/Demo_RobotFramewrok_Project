*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
TC_Google_App1
    Launch Browser

TC_Google_App2
    Launch Browser 

TC_Google_App3
    Launch Browser

TC_Google_App4
    Launch Browser

*** Keywords ***
Launch Browser
    Open Browser    https://www.google.co.in/?gws_rd=ssl
    sleep    5s
    Maximize Browser Window
    Input Text    xpath=.//input[@name='q']    Google
    Click Button    xpath=.//input[contains(@value,'Google Search')]
    ${TC_SEARCHTIME}    Get Text    xpath=.//*[@id='resultStats']
    Log    ${TC_SEARCHTIME}
    Close Browser
