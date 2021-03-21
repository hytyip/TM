# Think Money Tech Test
Using Python with Selenium, behave and Allure Report

# Reason for using this tool: 
1. Easy to install on any machine Windows, Mac or Linux
2. Faster than Java and some of the other selenium tool
3. Easy to write test
4. The current automation tests have been written in Python too

## To run the test
1. Required to install Python 3, pip
2. Install Allure. Follow this page to install  https://docs.qameta.io/allure/#_windows
2. Navigate to "features" folder in terminal
3. Enter command to install libraries
``` pip install -r requirements.txt ```
4. Enter command to run the test
``` behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% Test.feature ```
5. To view the Allure Test Report
``` allure serve %allure_result_folder% ```

ps: Using Chrome driver 89
