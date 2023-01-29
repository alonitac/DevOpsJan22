import os


def lambda_handler(event, context):

    stream = os.popen(f'cd /tmp && darknet detector demo /lambda_func/cfg/coco.data /lambda_func/cfg/yolov3.cfg /lambda_func/yolov3.weights /lambda_func/maxresdefault.jpg')
    output = str(stream.read())

    # bucket_name = event['Records'][0]['s3']['bucket']['name']
    # key = event['Records'][0]['s3']['object']['key']

    print(f'Detecting objects in image...')
