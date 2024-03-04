import http.client
import json

API_KEY = "App f061d81db195515f3f02ce30b88111cf-730b1533-f863-45f4-b814-e4d72ced11ca"

conn = http.client.HTTPSConnection("1jddn.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [
                {
                    "to": "254720032567"
                }
            ],
            "from": "StimaSacco",
            "text": "Dear SAMSON, Your Stima Sacco membership application has been processed. Your Member number is 1018620.For M-Pesa deposits, use the paybill business number 4083183 and your Account number. Your Prime Account Number is 801101862001, Alpha deposits/Savings account is 802101862001 and Share capital account is 800101862001. For queries WhatsApp 0703024001 or SMS 23356."
        }
    ]
})
headers = {
    'Authorization': API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/sms/2/text/advanced", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))