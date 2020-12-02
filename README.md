# mecab-api

Serverless MeCab API with AWS SAM.
You can deploy to AWS (API Gateway + Lambda).

## Launch in Local

```bash
# install dependencies
pip3 install -r requirements.txt

# this commands invokes ./mecab_api/Makefile via aws-sam-cli
sam build
```

## Deploy to AWS

``bash
sam deploy --guided
```
