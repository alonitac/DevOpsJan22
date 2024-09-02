FROM daisukekobayashi/darknet:cpu-cv

RUN apt-get update -y && apt-get install -y software-properties-common python3.9 python3-pip
RUN pip3 install --target /lambda_func boto3 awslambdaric

WORKDIR /lambda_func
COPY . .

ENTRYPOINT [ "/usr/bin/python3", "-m", "awslambdaric" ]
CMD [ "app.lambda_handler" ]