# -*- coding: utf-8 -*-
import requests
import string
from foo.utils.string_utils import StrList
import logging
import sys

COOKIE = ("has_recent_activity=1; "
          "_ga=GA1.2.383375504.1562551032; "
          "tz=Asia%2FShanghai; "
          "_octo=GH1.1.1301990110.1562551032; "
          "_device_id=2ec212bc7c29135cf6b7842a61cb7369; "
          "logged_in=no; "
          "_gat=1; "
          "_gh_sess=U3dmR2xrQlplVFVJUk1oV2M1RkxueVZadktUZzZQOXNSOHJpbXpUbXZLVFF3bERBK0RLa09nZDFKcWJmNWtXK20zdjFjMHhrb0F"
          "GM3BqaTdjRHpuY2wwTEx2aEhyK3g2dVJadmd2S3NZaVVtd1hxRlR5WE1NNlZnZk5ORXk5cUdFY2o3TUh5MFlNdVBMdC80QW16SytsRGhnMHJ"
          "TcFFnMlJGd1lnZi92djBTQkZ4WGppaXNFVmM5Z1lQZ2M3ekpieXFhMUVOQ2FnVmZTWSsrNWlHYXhHUmJtcU9sMEZQMkZ4R3RrRXNpU1Z0dVc"
          "5RVgzdXIwL1JVKzlRbncvc0NMWGtjM1U3dWZ3MVpUallEWVBOSWlPVDZMeWhxOHlZam80ZVV1ZGNhT0JLVFhDNkxWR3AwakV3THMzMG1OSXh"
          "vVlNyZVFoOXlTKzNrbm40M3Z5KzBIc1ExbGFMTkVhRWZYSFBWMlAvSkRkWlR4NFRUNHJoUk8yU25iczF4V1ZhRXpkUXZIMXF5cHdIVHYrc09"
          "iRnBybmtpSmVrMHVQSCt5UEY3ZFc2Yks1MFJiK1A1U28rUEQyOU9RSHpmYkYwSE56UHZLSG5NRG9VbnRGU2dBVXdiUW4zcXoxTXJXZWFlZ0F"
          "ITDZxQWRZNnBiekc3Y0JReldPMEpsK3FLRVJ5U2YzcnlEWGhza2Y0VTdCR0NMRjQ3Y0ovZy8wamJsWnNTU3RwK3piaHByWWxaV1ZJRVAyZW5"
          "XNmZFRDIwTnQxNnVqZHd4SjFQRWVSczZzTDZwM1JocGhCZ3U2Ti9ta3UyYXFMYU5TYjR6ajM0RU1FaUF1Qm9mbTNKZjRoNjFEV0k4ejM1d3R"
          "hRm4yL1p1OUpYZlAvbnRCMVpLK1I0WUwyMzB2UjN1SXFYK0Mzd0pKbWFrd1VGTUw2amQ4VmR2YmVJNGJaeW4tLVJSNWZCWXYycmRnbU5HMlh"
          "VWlBJOUE9PQ%3D%3D--003d36809ef5b52e777ab30cd7ff2871ab7322d8")
logger_name = "scan"
logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s\t %(message)s')
logger = logging.getLogger(logger_name)



def run(file_name):
    s1 = requests.session()
    s1.headers = {'Accept': ('text/html,application/xhtml+xml,application/xml;'
                             'q=0.9,image/webp,image/apng,*/*;'
                             'q=0.8,application/signed-exchange;'
                             'v=b3'
                             ),
                  'Host': 'github.com',
                  'Connection': 'keep-alive',
                  'Pragma': 'no-cache',
                  'Cache-Control': 'no-cache',
                  'Origin': 'https://github.com',
                  'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/75.0.3770.100 Safari/537.36'),
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Content-Type': 'multipart/form-data',
                  'Referer': 'https://github.com/join?source=header-home',
                  'Upgrade-Insecure-Requests': '1',
                  'Cookie': COOKIE
                  }
    s2 = requests.session()
    s2.headers = {'Accept': 'text/html; fragment',
                  'Host': 'github.com',
                  'Connection': 'keep-alive',
                  'Pragma': 'no-cache',
                  'Cache-Control': 'no-cache',
                  'Origin': 'https://github.com',
                  'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/75.0.3770.100 Safari/537.36'),
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'Content-Type': 'multipart/form-data',
                  'Referer': 'https://github.com/join?source=header-home',
                  'Cookie': COOKIE
                  }
    result_file = open(file_name, 'a+')
    for i in range(1, 5):
        all_char = string.lowercase[:] + "1234567890-"
        str_list = StrList(all_char).get_string(i)
        for word in str_list:
            s1_res = s1.get("https://github.com/{user_name}".format(user_name=word))
            if s1_res.status_code != 200:
                data = {
                    'authenticity_token': 'GrZOZH6oXLHjzftC41G9BpaSCN/5hMulrdIs37pPESc7I1tXeDKbVnaXHRkVzPqn2OKVQ16ChI+8f3FhiuKwrw==',
                    'value': '{word}'.format(word=word)
                }
                s2_res = s2.post("https://github.com/signup_check/username?suggest_usernames=true", data=data)
                if s2_res.status_code != 422:
                    result = "s1[{s1_code}]\ts2[{s2_code}]\tword[{word}]".format(s1_code=s1_res.status_code,
                                                                                 s2_code=s2_res.status_code,
                                                                                 word=word)
                    logger.info(result)
                    result_file.write(result + "\n")
                    result_file.flush()
    result_file.close()


def main():
    try:
        file_name = sys.argv[1]
    except Exception, e:
        logger.error(e)
        file_name = "./result.txt"
    run(file_name)


if __name__ == '__main__':
    main()