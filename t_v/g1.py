import base64, time, requests
import concurrent
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
import argparse


class VTAnalyzer:

    def __init__(self):
        self._cache = {}
        self.time = datetime.now()
        self.counter_reputation = 0

    def get_urls_reputation(self, urls: list,
                            apikey="f5acf4919acd81a1e9927234b0696a2b714d8b73265f49b9e6a077207054b23a") -> dict[
        str, bool]:

        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = {executor.submit(self.get_reputation_for_single_url, url, apikey): url for url in urls}

        reputations = {}
        for future in concurrent.futures.as_completed(results):
            url = results[future]
            reputations[url] = future.result()

        return reputations

    def _get(self, url, apikey):
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        api_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

        headers = {
            "accept": "application/json",
            "x-apikey": apikey
        }
        return requests.get(api_url, headers=headers)

    def _check_status(self, response):
        data = response.json()['data']["attributes"]["last_analysis_stats"]
        sum = data['harmless'] + data['malicious'] + data['suspicious'] + data['undetected'] + data['timeout']
        if (data['harmless'] / sum) * 100 > 60:
            return True
        else:
            return False

    def _date_time_scan(self, response):
        last_analysis_update = response.json()["data"]["attributes"]["last_analysis_date"]
        return datetime.fromtimestamp(last_analysis_update)

    def _scan(self, url_to_scan, apikey):

        url = "https://www.virustotal.com/api/v3/urls"

        payload = f"url={url_to_scan}"

        headers = {
            "accept": "application/json",
            "x-apikey": apikey,
            "content-type": "application/x-www-form-urlencoded"
        }

        requests.post(url, data=payload, headers=headers)
        time.sleep(20)

    def multi_scan(self, urls_to_scan: list, apikey="f5acf4919acd81a1e9927234b0696a2b714d8b73265f49b9e6a077207054b23a"):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = {executor.submit(self._scan, url, apikey): url for url in urls_to_scan}

    def get_reputation_for_single_url(self, url: str, apikey):

        if (url in self._cache.keys()) and ((datetime.utcnow() - self._cache[url]["check_time"]) < timedelta(days=182)):

            return self._cache[url]["status"]


        else:
            if (self.time - datetime.now()).total_seconds() / 60 == 1:
                raise Exception("Too much response in one minute")
            response = self._get(url, apikey)
            if (response.status_code < 400) and (
                    (datetime.utcnow() - self._date_time_scan(response)) < timedelta(days=182)):
                self._cache[url] = {"status": self._check_status(response),
                                    "check_time": self._date_time_scan(response)}
                self.counter_reputation += 1
                if self.counter_reputation == 4:
                    self.time = datetime.now()
                    self.counter_reputation = 0

                return self._check_status(response)

            else:
                self._scan(url, apikey)

                response = self._get(url, apikey)
                if response.status_code >= 400:
                    raise Exception("Something is wrong, come back another time ")
                self._cache[url] = {"status": self._check_status(response),
                                    "check_time": self._date_time_scan(response)}
                self.counter_reputation += 1
                if self.counter_reputation == 4:
                    self.time = datetime.now()
                    self.counter_reputation = 0

                return self._check_status(response)
