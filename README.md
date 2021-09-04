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

- **STEP 1:** After completing the above prerequisites, we have to next Deploy DynamoDB in our computer. For this open your Command Prompt (Preferablly Anaconda) or a terminal in your IDE. I use VSCode.
<img src="https://user-images.githubusercontent.com/66016994/132091977-80f94f68-271e-4b86-b034-5c8d0724ddc9.png" />
This is your Java Instance that needs to keep on running.

- **STEP 2:** In a seperate terminal run the following commands to configure your credentials in order to enable authorization.
<img src="https://user-images.githubusercontent.com/66016994/132092067-01d61598-08f7-42d6-94ec-56c17753b576.png" />
By doing this you will now be able to access your DynamoDB.

- **STEP 3:** Next we will create the necessary python files. This will be used for creating the table and inserting new values. We will be using six codes to perform six different tasks, and after creating the necessary files we will be calling all the .py files using *python <u>filename</u>.py*.
  - ### Create Table
  <img src="https://user-images.githubusercontent.com/66016994/132092137-d20e1d37-3d8e-49e4-abbd-8f94da5ca1bf.png" />

  - ### Data Creation
  <img src="https://user-images.githubusercontent.com/66016994/132092186-2056ae20-7edd-4d4a-9a69-0fcaa19b5879.png" />

  - ### Loading Data
  <img src="https://user-images.githubusercontent.com/66016994/132092196-89ada4ae-457a-4705-b652-e585b3edb538.png" />

  - ### Reading Items in the Table
  <img src="https://user-images.githubusercontent.com/66016994/132092212-ef5c6e87-114d-480e-abad-02a50d71de8c.png" />

  - ### Query
  <img src="https://user-images.githubusercontent.com/66016994/132092214-298d38ac-393d-4821-80bc-324c8aa49081.png" />

<img src="https://user-images.githubusercontent.com/66016994/132092270-e8d9a6f7-410f-4f4e-b9ff-c578179dd310.png" />
We can see how we excecuted the above files and we can also see their outputs. We will be able to see all the data in out table using the *scam.py*.

  - ### Scan Table
  <img src="https://user-images.githubusercontent.com/66016994/132092227-801da2cc-a692-4266-bd4b-4afeffe27291.png" />
  <img src="https://user-images.githubusercontent.com/66016994/132092312-b54327b6-7ebc-4ee4-9d32-fad66ca3bc4c.png" />

We have done our initial procedure or adding Data to our table and perform basic operations. Now we will go the extra mile and create a function that will do a simple task of turning on the sprinklers when the **Temperature** is greater than *25 degree Celcius*.

  - ### Activating the Device
  <img src="https://user-images.githubusercontent.com/66016994/132096756-e7ef9729-1080-49e2-9646-425d87de2008.png" />
  <img src="https://user-images.githubusercontent.com/66016994/132096768-293a1c3f-bb83-402e-bc9b-aba58ce8a41e.png" />

- As shown above we have thus completed the task assigned to us. Now we can ***Delete the Table.***

  - ### Delete Table
  <img src="https://user-images.githubusercontent.com/66016994/132096824-0d6a0625-48e9-400f-a1ff-1c018d2ab283.png" />
  <img src="https://user-images.githubusercontent.com/66016994/132096817-160833c3-6b3d-4fec-8196-0e7a5d25c43c.png" />
  
---

This shows us a basic idea on how to get started with DynamoDB and Python.
