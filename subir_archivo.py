import boto3
import base64

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio']
    nombre_archivo = event['body']['nombre_archivo']
    contenido = event['body']['contenido']
    s3 = boto3.client('s3')
    archivo_bytes = base64.b64decode(contenido)
    s3.put_object(
        Bucket=nombre_bucket,
        Key=f'{directorio}/{nombre_archivo}',
        Body=archivo_bytes
    )
    return {
        'statusCode': 200,
        'mensaje': f'Archivo {nombre_archivo} subido a {nombre_bucket}/{directorio}'
    }
