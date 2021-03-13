import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('iam')
    event_type= event["detail"]["responseElements"]
    if "user" in event_type :
        MyArn=event["detail"]["responseElements"]["user"]["arn"]
        MyName=event["detail"]["responseElements"]["user"]["userName"]
        response = client.list_user_tags(
            UserName=MyName,
        )
        print(MyArn)
    else:
        MyArn=event["detail"]["responseElements"]["role"]["arn"]
        MyName=event["detail"]["responseElements"]["role"]["roleName"]
        response = client.list_role_tags(
            RoleName=MyName,
        )
        tags_list=response["Tags"]
        keys=[]
    
    for i in tags_list:
        keys.append(i['Key'])
    
    if "k8s-auth" in keys:
        print ("Authoriized")
    else:
        print ("Non-Authoriized")
        
