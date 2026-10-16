*** Settings ***
Library    SeleniumLibrary
Library    Browser
Library    DatabaseLibrary
Library    Collections
Library    RequestsLibrary

Suite Setup    Log    Inside test suite setup
Suite Teardown    log    Inside test suite teardown
Default Tags    Sanity

Test Teardown    SeleniumLibrary.Open Browser    file:///C:/Repo/Demo_RobotFramewrok_Project/results/log.html    chrome

*** Variables ***
${url}    https://google.com 
${Se}    Selenium
${OrangeUrl}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
@{Cities}    Pune    Delhi    Mumbai
@{OrangeCreds}    Admin    admin123
&{testdata}    url=https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    username=Admin    password=admin123

*** Keywords ***

googleIt    
    [Arguments]    ${searchText}
    SeleniumLibrary.Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    5
    Input Text      name=q                ${searchText}
    SeleniumLibrary.Press Keys    name=q    ENTER
    Sleep           2 


*** Test Cases ***

MyFirstTest
    [Tags]    Smoke
    Log     Good morning


FirstSeleniumTest
    [Setup]    Log    Inside test setup
    [TearDown]    Log    Inside Test Teardown
    googleIt    Veena Katiyar
    SeleniumLibrary.Close Browser
    Log    This test was executed by %{username} on %{os}. Log file is ${LOG_FILE}

OrangeHRM Login
    SeleniumLibrary.Open Browser    ${OrangeUrl}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    5
    Wait Until Element Is Visible    name=username    20s
    Input Text    name=username    ${OrangeCreds}[0]
    Input Password    name=password    ${testdata}[password]
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains    Dashboard    10s
    Click Element    xpath://img[@alt="profile picture"]
    Click Element    link=Logout
    SeleniumLibrary.Close Browser

OrangeHRM Login1
    SeleniumLibrary.Open Browser    ${OrangeUrl}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    5
    Wait Until Element Is Visible    name=username    20s
    Input Password    name=password    ${OrangeCreds}[1]
    Input Text    name=username    ${testdata}[username]
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains    Dashboard    10s
    Click Element    xpath://img[@alt="profile picture"]
    Click Element    link=Logout
    SeleniumLibrary.Close Browser

OrangeHRM Login2
    SeleniumLibrary.Open Browser    ${OrangeUrl}    chrome
    Maximize Browser Window
    Set Browser Implicit Wait    5
    Wait Until Element Is Visible    name=username    20s
    Input Password    name=password    admin123
    Input Text    name=username    Admin
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains    Dashboard    10s
    Click Element    xpath://img[@alt="profile picture"]
    Click Element    link=Logout
    SeleniumLibrary.Close Browser

Playwright Test
    New Browser    chromium    headless=False
    New Page    ${url}
    Fill Text    [name='q']    Veena
    Browser.Press Keys    [name='q']    Enter
    Sleep    2s
    Browser.Close Browser

Fill All Fields And Submit Form
    [Documentation]    Enters values in every field and clicks Submit, then verifies the success message.
    SeleniumLibrary.Open Browser    https://rahulshettyacademy.com/angularpractice/    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s
    Wait Until Element Is Visible    xpath=(//input[@name='name'])[1]   timeout=15s
    Input Text                xpath=(//input[@name='name'])[1]      John Doe
    Input Text                name=email       john.doe@example.com
    Input Password            id=exampleInputPassword1    Secret@123
    Select Checkbox           id=exampleCheck1
    ${options1}    Get List Items    id=exampleFormControlSelect1
    Log    ${options1}

    @{opt1}    Create List    Male    Female
    FOR    ${item}    IN    ${options1}
        Log    ${item}
        Should Contain    @{opt1}   ${item}     
    END
    Select From List By Label    id=exampleFormControlSelect1   Male
    Select Radio Button       inlineRadioOptions   option2
    Input Text                name=bday         15-Oct-1995
    Click Button              css=input[type='submit']
    Wait Until Element Is Visible    css=div.alert-success    timeout=10s
    Element Should Contain    css=div.alert-success    Success!
    Capture Page Screenshot   form_submitted.png




# API Testing
#     Create Session  mainSession  https://thinking-tester-contact-list.herokuapp.com     verify=true
#     &{headers}     Create dictionary   Content-Type=application/json
#     &{body}        Create dictionary   email=random@email.com            password=Password123!
#     ${resp}        POST On Session     mainSession     /users/login      headers=${headers}          json=${body}
#     Status Should Be                    200  ${resp}
#     Should Be Equal As Strings          ${resp.json()}[user][email]       ${body}[email]
   


   




