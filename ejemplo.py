import boto3

s3 =boto3.client('s3')

def uploadFile(filePath, filename):
    try:
        destinationRoute = "pruebaawsclase15/"+filename
        s3.upload_file(filePath,"pruebaawsclase15",destinationRoute)
        response=destinationRoute
    except Exception as err:
        response="Failure"
    return response

test = uploadFile(filePath=r"C:\Users\Punto De Pago\Documents\version3.txt",filename="version3.txt")
print(test)

def crear_url_pre(bucket_nombre,objeto, tiempo=3600):
    s3 =boto3.client('s3')
    try:
        response=s3.generate_presigned_url('get_object',Params={'Bucket':bucket_nombre, 'Key':objeto},ExpiresIn=tiempo)
    except Exception as e:
        print(f"error: {e}")
        return None
    return response

url= crear_url_pre('pruebaawsclase15','version3.txt')
print(url)