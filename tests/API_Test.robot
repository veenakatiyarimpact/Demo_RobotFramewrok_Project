*** Settings ***
Documentation       Tests for the /users/login authentication endpoint.

Library             Collections
Library             RequestsLibrary


*** Variables ***
${BASE_URL}     https://api.practicesoftwaretesting.com
${EMAIL}        customer@practicesoftwaretesting.com
${PASSWORD}     welcome01


*** Test Cases ***
Should Return Access Token On Successful Login
    [Documentation]    Verify that a successful login returns an access token.
    ${payload}    Create Dictionary    email=${EMAIL}    password=${PASSWORD}
    ${response}   POST    ${BASE_URL}/users/login    json=${payload}
    Status Should Be    200
    Dictionary Should Contain Key    ${response.json()}    access_token
    ${accessToken}    Get From Dictionary    ${response.json()}    access_token
    Log    ${accessToken}