
from selenium.webdriver.support.select import Select
import json
import requests
import time
class TestBrowser():

    def test_new(self,browser):
        browser.get("https://color-pickerio.netlify.app/")
        baselurl="https://colorhunt2.onrender.com/color/getallrecentcolors/100/0"
        res=requests.get(baselurl)
        assert res.status_code==200
        print("All recent colors")

    def test_popular(self,browser):
        browser.get("https://color-pickerio.netlify.app/popular")
        res=requests.get("https://colorhunt2.onrender.com/color/popular/100/0")
        assert res.status_code==200
        print("All popular colors")

    def test_create(self, browser):
        try:
            data={
            "color1":"#92dea7",
            "color2":"#52825f",
            "color3":"#336340",
            "color4":"#67db87",
            "tags": [
                    {
                        "id": 1,
                        "label": "mild",
                        "value": "mild"
                    },
                    {
                        "id": 9,
                        "label": "spring",
                        "value": "spring"
                    },
                    {
                        "id": 13,
                        "label": "happy",
                        "value": "happy"
                    },
                    {
                        "id": 12,
                        "label": "halloween",
                        "value": "halloween"
                    },
                    {
                        "id": 2,
                        "label": "night",
                        "value": "night"
                    }
            ],
            "date":"2023-05-12T19:32:30+05:30"

        }
            res=requests.post("https://colorhunt2.onrender.com/color/add",
                    data=json.dumps(data), headers = {'content-type': 'application/json'})
            x=json.loads(res.text)
            global idx
            idx=x['_id']
            print("Color Pallete created successfully")

            assert res.status_code==201
            time.sleep(5)
            browser.get(f"https://color-pickerio.netlify.app/color/{idx}")

            requests.delete(f"https://colorhunt2.onrender.com/color/deletecolor/{idx}")
            print("Deleted Successfully")
        except Exception as e:
            print(e)

