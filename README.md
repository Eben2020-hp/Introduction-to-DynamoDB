# Introduction-to-DynamoDB

## What is DynamoDB?
DynamoDB is a speedy and flexible NoSQL database service offered by AWS (Amazon Web Service). You can use Amazon DynamoDB to create a database table that can store and retrieve any amount of data, and serve any level of request traffic. Amazon DynamoDB automatically spreads the data and traffic for the table over a sufficient number of servers to handle the request capacity specified by the customer and the amount of data stored, while maintaining consistent and fast performance.

We will be understanding how to use Python SDK (Boto3) to perform operations in DynamoDB. 

## Prerequisites
Before going any further we need to download three main things:
|  | Instructions | Link |
| --- | --- | --- |
| 1 | Download DynamoDB locally | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html |
| 2 | Download AWS CLI | https://awscli.amazonaws.com/AWSCLIV2.msi |
| 3 | Install Java Runtime Environment (JRE) | https://www.java.com/en/download/manual.jsp |

**IMPORTANT:** 
- If working with ***Windows OS***, please make sure that you have installed all the three inside the same folder.
- If working with ***Linux***, this will not be an issue, although it is recommended to keep *DynamoDB* and *AWS CLI* inside the same folder.

---

## Procedure

After completing the above prerequisites, we have to next Deploy DynamoDB in our computer. For this open your Command Prompt (Preferablly Anaconda) or a terminal in your IDE. I use VSCode.

