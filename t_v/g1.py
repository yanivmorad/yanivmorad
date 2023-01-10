import base64
import json
import os
import pickle
from datetime import datetime, timedelta

import requests
# url_id = base64.urlsafe_b64encode("https://developers.virustotal.com/reference/url-object".encode()).decode().strip("=")
#
#
# url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
#
# headers = {
#     "accept": "application/json",
#     "x-apikey": "f5acf4919acd81a1e9927234b0696a2b714d8b73265f49b9e6a077207054b23a"
# }
# # response = requests.get(url, headers=headers)
# #
# # test_json = response.json()
# # print(test_json["data"])
# with open("vt.json", "r") as jf:
#     data = json.load(jf)['data']["attributes"]["last_analysis_stats"]
#     if data['harmless']> data['malicious'] +data['suspicious']+data['undetected']+data['timeout']:

class VTAnalyzer:

    def __init__(self):
        self._cache = {}
        self.time = datetime.now()
        self.counter_reputation = 0


    def get_urls_reputation(self, urls: list) -> dict[str, bool]:
        pass
    def _get(self,url):
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        api_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

        headers = {
            "accept": "application/json",
            "x-apikey": "f5acf4919acd81a1e9927234b0696a2b714d8b73265f49b9e6a077207054b23a"
        }
        return requests.get(api_url, headers=headers)
    def _check_status(self,response):
        data = response.json()['data']["attributes"]["last_analysis_stats"]
        sum = data['harmless'] + data['malicious'] + data['suspicious'] + data['undetected'] + data['timeout']
        if (data['harmless']/sum) * 100 > 60:
            return True
        else:
            return False
    def _date_time_scan(self,response):
        last_analysis_update = response.json()["data"]["attributes"]["last_analysis_date"]
        return datetime.fromtimestamp(last_analysis_update)
    def _scan(self,url_to_scan):
        url = "https://www.virustotal.com/api/v3/urls"

        payload = f"url={url_to_scan}"
        headers = {
            "accept": "application/json",
            "x-apikey": "f5c7983383c2d7e13fde2a7dc9adc43d6a56b108dcc5ad7e6b14de3a7bf44acf",
            "content-type": "application/x-www-form-urlencoded"
        }

        return requests.post(url, data=payload, headers=headers)

    def get_reputation_for_single_url(self, url:str):
        if (url in self._cache.keys()) and ((datetime.utcnow() - self._cache[url]["check_time"]) < timedelta(days=182)):
            print(self._cache)
            return self._cache[url]["status"]

        else:
            if (self.time - datetime.now()).total_seconds() / 60 == 1:
                raise Exception("Too much response in one minute")
            response = self._get(url)
            if (response.status_code<= 400) and ((datetime.utcnow() - self._date_time_scan(response)) < timedelta(days=182)):
                self._cache[url] = {"status": self._check_status(response), "check_time":self._date_time_scan(response)}
                self.counter_reputation +=1
                if self.counter_reputation ==4:
                    self.time = datetime.now()
                    self.counter_reputation =0
                return self._check_status(response)

            else:
                self._scan(url)
                response = self._get(url)
                if response.status_code >= 400:
                    raise Exception("Something is wrong, come back another time ")
                self._cache[url] = {"status": self._check_status(response),
                                    "check_time":self._date_time_scan(response)}
                self.counter_reputation+=1
                if self.counter_reputation ==4:
                    self.time = datetime.now()
                    self.counter_reputation = 0

                return self._check_status(response)


if __name__ == '__main__':

    if not os.path.exists('VT_website.pickle'):
        save_website = VTAnalyzer()
    else:
        with open('VT_website.pickle', 'rb') as fh:
            save_website = pickle.load(fh)
    try:
        print(save_website.get_reputation_for_single_url("https://translate.google.com/?sl=en&tl=iw&text=Too%20much%20response%20in%20one%20minute&op=translate"))
    except Exception as e:
        print(e)
    with open('VTexample.pickle', 'wb') as fh:
        pickle.dump(save_website, fh)

# last_analysis_update = response["data"]["attributes"]["last_analysis_date"]
#         last_analysis_date = datetime.fromtimestamp(last_analysis_update)
#         if (datetime.utcnow() - last_analysis_date) > timedelta(days=182):
#             VirusTotal.scan_url(self)
# with open("vt.json","r") as f:
    # data =json.load(f)
    # last_analysis_stats = data['data']["attributes"]["last_analysis_stats"]
    # sum = last_analysis_stats['harmless'] + last_analysis_stats['malicious'] + last_analysis_stats['suspicious'] + last_analysis_stats['undetected'] + last_analysis_stats['timeout']
    # print((last_analysis_stats['harmless'] / sum) * 100)
    # last_analysis_update = data["data"]["attributes"]["last_analysis_date"]
    # print(last_analysis_update)
    # last_analysis_date = datetime.fromtimestamp(last_analysis_update)
    # print((datetime.utcnow() - last_analysis_date))

