# aws
This repository contains python code to automate aws lambda to check the ec2 instances and filter them by their tags.

This lambda function runs every hour.

We have scheduled the lambda functikn by Event Bridge in which the rate is set to 60 minutes to run lambda function every hour.

If the mentioned tags are not present it senda an email to the owner of the intance .

If after 6 hours tags are not added we terminate the instance. 
