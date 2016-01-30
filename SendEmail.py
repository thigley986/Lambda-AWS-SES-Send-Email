import boto3

ses = boto3.client('ses')

email_from = 'Email'
email_to = 'Email'
email_cc = 'Email'
emaiL_subject = 'Subject'
email_body = 'Body'


def lambda_handler(event, context):
    response = ses.send_email(
        Source = email_from,
        Destination={
            'ToAddresses': [
                email_to,
            ],
            'CcAddresses': [
                email_cc,
            ]
        },
        Message={
            'Subject': {
                'Data': emaiL_subject
            },
            'Body': {
                'Text': {
                    'Data': email_body
                }
            }
        }
    )
