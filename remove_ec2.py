import boto3
ec2client = boto3.client('ec2')

def lambda_handler(event , context):
    instanceswithevent = ec2client.describe_instance_status{
            Filters= [{
                'Name' : 'tag': ' environment' , 'Values':[{exists:false}]
,
{

    'Name': ' tag':'Name', 'Values': [{ exists:false]},
    }











                },
    
                ],
            )
            instancestoterminate = []
            
            for index in instanceswithevent:
                instancestoterminate.append(index['InstanceId'])
            if len(instancetoterminate)>0:
                ec2client.treminate_instances(InstanceIdss = instancetoterminate)
            else:
                return ()
