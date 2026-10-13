*** Settings ***
Library    SeleniumLibrary

Suite Setup    Log    Inside test suite setup
Suite Teardown    log    Inside test suite teardown
Default Tags    Sanity

*** Variables ***
${url}    https://google.com 
${Se}    Selenium
${OrangeUrl}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
@{OrangeCreds}    Admin    admin123
&{testdata}    url=https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    username=Admin    password=admin123

*** Keywords ***

googleIt    
    [Arguments]    ${searchText}
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    5
    Input Text      name=q                ${searchText}
    Press Keys    name=q    ENTER
    Sleep           2 


*** Test Cases ***

MyFirstTest
    [Tags]    Smoke
    Log     Good morning


FirstSeleniumTest
    [Setup]    Log    Inside test setup
    [TearDown]    Log    Inside Test Teardown
    googleIt    Veena Katiyar
    Close Browser
    Log    This test was executed by %{username} on %{os}. Log file is ${LOG_FILE}

OrangeHRM Login
    Open Browser    ${OrangeUrl}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    5
    Wait Until Element Is Visible    name=username    20s
    Input Text    name=username    ${OrangeCreds}[0]
    Input Password    name=password    ${testdata}[password]
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains    Dashboard    10s
    Click Element    xpath://img[@alt="profile picture"]
    Click Element    link=Logout
    Close Browser

OrangeHRM Login1
    Open Browser    ${OrangeUrl}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    5
    Wait Until Element Is Visible    name=username    20s
    Input Password    name=password    ${OrangeCreds}[1]
    Input Text    name=username    ${testdata}[username]
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains    Dashboard    10s
    Click Element    xpath://img[@alt="profile picture"]
    Click Element    link=Logout
    Close Browser

OrangeHRM Login2
    Open Browser    ${OrangeUrl}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    5
    Wait Until Element Is Visible    name=username    20s
    Input Password    name=password    admin123
    Input Text    name=username    Admin
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains    Dashboard    10s
    Click Element    xpath://img[@alt="profile picture"]
    Click Element    link=Logout
    Close Browser
