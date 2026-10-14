*** Settings ***
Variables    ../Layer_Application/OR/Demo_OR.py
Library     SeleniumLibrary

*** Keywords ***
Launch Browser
    Open Browser    https://www.google.com   chrome
    sleep    5s
    Maximize Browser Window
    Input Text    ${Obj_Txt_Search}    Google
    Click Button    ${Obj_Btn_Search}
    ${TC_SEARCHTIME}    Get Text    ${Obj_Txt_SearchResult}
    Log    ${TC_SEARCHTIME}
    Close Browser

*** Test Cases ***
TC_Google_App1
    Launch Browser

TC_Google_App2
    Launch Browser 

TC_Google_App3
    Launch Browser

TC_Google_App4
    Launch Browser
