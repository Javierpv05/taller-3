import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio']
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=f'{directorio}/')
    return {
        'statusCode': 200,
        'mensaje': f'Directorio {directorio} creado en {nombre_bucket}'
    }
