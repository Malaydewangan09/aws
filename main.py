import os
import boto3
 ec2_instances = []

def get_ec2_intances(Name , environment);


    ec2 = boto3.resources('ec2')
    filters = [
        
            {'Name':'tag:environment','Values':[{'exixts':false}]}
            {'Name':'tag:Name','Values':[{'exists':false]}
                




            ]
    instances= ec2.instance.Filter(filters)
    

    for instance in instances:
      instance_id = ['InstanceId']
      response = ses.send_email(

          source = 'zxyce@gmai.com',
          Destination = {
              "ToAddress" : email_address },
          Message = {
              'Subject':{
                  'Data': "Missing tags in your ec2 instance"
                  }
,
'Body':{
    'Text': "your instance id " + instance_id + "is missing tags environment and name tags. Please add the tags" + 
    }}
    }













