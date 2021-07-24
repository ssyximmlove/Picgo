import pixivpy3
import json

apiApp = pixivpy3.AppPixivAPI()
apiApp.auth(refresh_token='MfuFPFrhfNIK1yhqo3GMNIyZSFCvj0DC1NxDWhQfBPM')
json_result = apiApp.illust_detail(59580629)
print(json_result['illust']["title"])


