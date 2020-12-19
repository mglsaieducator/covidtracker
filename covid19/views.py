from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
import requests, json

# Create your views here.

def homeview(request): 
	#World Covid Data API
	api_request = requests.get('https://corona-api.com/timeline') #world covid data api
	api_request_us = requests.get('https://corona-api.com/countries/us')#USA data
	api_request_in = requests.get('https://corona-api.com/countries/in')#India data
	api_request_br = requests.get('https://corona-api.com/countries/br')#Brezil data
	api_request_ru = requests.get('https://corona-api.com/countries/ru')#Russia data
	if api_request:
		try:
			api_json_data = json.loads(api_request.content)
			latest_data = api_json_data['data'][0]
			chart_data = api_json_data['data']

			xaxis = []
			yaxis1 = []
			yaxis2 = []
			for x in chart_data:
				xaxis.append(x['date'])
				yaxis1.append(x['confirmed'])
				yaxis2.append(x['recovered'])


			api_json_data_us = json.loads(api_request_us.content) #USA data
			latest_data_us = api_json_data_us['data']['timeline'][1:8]
			latest_data_us_new = api_json_data_us['data']['timeline'][1]

			api_json_data_in = json.loads(api_request_in.content) #India data
			latest_data_in = api_json_data_in['data']['timeline'][1:8]
			latest_data_in_new = api_json_data_in['data']['timeline'][1]

			api_json_data_br = json.loads(api_request_br.content) #Brezil data
			latest_data_br = api_json_data_br['data']['timeline'][1:8]
			latest_data_br_new = api_json_data_br['data']['timeline'][1]

			api_json_data_ru = json.loads(api_request_ru.content) #Brezil data
			latest_data_ru = api_json_data_ru['data']['timeline'][1:8]
			latest_data_ru_new = api_json_data_ru['data']['timeline'][1]


			deaths = api_json_data['data'][0]['deaths']
			recovered = api_json_data['data'][0]['recovered']
			confirmed = api_json_data['data'][0]['confirmed']
			deathperc = (deaths/confirmed)*100  #death %
			recoper = (recovered/confirmed)*100 #recover %
			pichartdata = {'dper': deathperc, 'rper':recoper}	

			xaxis.reverse()
			yaxis1.reverse()
			yaxis2.reverse()
			
			#print(xaxis)
			#print(yaxis1)

		except Exception as e:
			apidata = 'Error..'
			if apidata == 'Error..':
				return HttpResponse("<h1>There is a problem in connecting with API, Please Check..</h1>")
		#return JsonResponse(api_json_data)
		#return HttpResponse(xaxis)
		return render(request, 'main.html', {'wdata': latest_data, 'pichartdata':pichartdata, 'usdata':latest_data_us, 'indata':latest_data_in, 'brdata':latest_data_br, 'rudata':latest_data_ru, 'usnewdata':latest_data_us_new, 'innewdata':latest_data_in_new, 'brnewdata':latest_data_br_new, 'runewdata':latest_data_ru_new, 'xaxis':xaxis, 'yaxis1':yaxis1, 'yaxis2':yaxis2})
	else:
		return HttpResponse("<h1>There is a problem in connecting with API, Please Check..</h1>")


	

	# #return JsonResponse(deaths)
	# #return HttpResponse(recoper)

def countryview(request):
	if request.method == "POST":
		try:
			xy = ['india', 'usa', 'russia', 'brazil', 'france', 'italy', 'china', 'uk', 'spain']
			xl = ['in', 'us', 'ru', 'br', 'fr', 'it', 'cn', 'gb', 'es', ]
			countrycode = request.POST['ccode']
			if countrycode in xy:
				xyi = xy.index(countrycode)
				countrycode=xl[xyi]
			else:
				countrycode = countrycode

			api_country = requests.get("https://corona-api.com/countries/"+countrycode+"")
			api_country_data = json.loads(api_country.content)
			card_data = api_country_data['data']
			api_country_latest = api_country_data['data']['timeline'][0]
			chart_data = api_country_data['data']['timeline']

			xaxis = []
			yaxis1 = []
			yaxis2 = []
			for x in chart_data:
				xaxis.append(x['date'])
				yaxis1.append(x['confirmed'])
				yaxis2.append(x['recovered'])

			api_request_us = requests.get('https://corona-api.com/countries/us')#USA data
			api_request_in = requests.get('https://corona-api.com/countries/in')#India data
			api_request_br = requests.get('https://corona-api.com/countries/br')#Brezil data
			api_request_ru = requests.get('https://corona-api.com/countries/ru')#Russia data

			api_json_data_us = json.loads(api_request_us.content) #USA data
			latest_data_us = api_json_data_us['data']['timeline'][1:8]
			latest_data_us_new = api_json_data_us['data']['timeline'][1]

			api_json_data_in = json.loads(api_request_in.content) #India data
			latest_data_in = api_json_data_in['data']['timeline'][1:8]
			latest_data_in_new = api_json_data_in['data']['timeline'][1]

			api_json_data_br = json.loads(api_request_br.content) #Brezil data
			latest_data_br = api_json_data_br['data']['timeline'][1:8]
			latest_data_br_new = api_json_data_br['data']['timeline'][1]

			api_json_data_ru = json.loads(api_request_ru.content) #Brezil data
			latest_data_ru = api_json_data_ru['data']['timeline'][1:8]
			latest_data_ru_new = api_json_data_ru['data']['timeline'][1]

			deaths = api_country_data['data']['timeline'][0]['deaths']
			recovered = api_country_data['data']['timeline'][0]['recovered']
			confirmed = api_country_data['data']['timeline'][0]['confirmed']
			deathperc = (deaths/confirmed)*100  #death %
			recoper = (recovered/confirmed)*100 #recover %
			pichartdata = {'dper': deathperc, 'rper':recoper}	

			xaxis.reverse()
			yaxis1.reverse()
			yaxis2.reverse()
			
		except Exception as e:
			apidata = 'Error..'
			if apidata == 'Error..':
				return HttpResponse("<h1>There is a problem in connecting with API/Country Code, Please Check..</h1>")

		return render(request, 'country.html', {'cdata':api_country_latest, 'carddata':card_data, 'pichartdata':pichartdata, 'usdata':latest_data_us, 'indata':latest_data_in, 'brdata':latest_data_br, 'rudata':latest_data_ru, 'usnewdata':latest_data_us_new, 'innewdata':latest_data_in_new, 'brnewdata':latest_data_br_new, 'runewdata':latest_data_ru_new, 'xaxis':xaxis, 'yaxis1':yaxis1, 'yaxis2':yaxis2})
		#return JsonResponse(api_country_latest)
	else:
		#return JsonResponse(api_country_latest)
		return HttpResponse("<h1>There is a problem in connecting with API/Country Code, Please Check..</h1>")


def cntview(request, ccode):
	try:
		api_country = requests.get("https://corona-api.com/countries/"+ccode+"")
		api_country_data = json.loads(api_country.content)
		card_data = api_country_data['data']
		api_country_latest = api_country_data['data']['timeline'][0]
		chart_data = api_country_data['data']['timeline']

		xaxis = []
		yaxis1 = []
		yaxis2 = []
		for x in chart_data:
			xaxis.append(x['date'])
			yaxis1.append(x['confirmed'])
			yaxis2.append(x['recovered'])

		api_request_us = requests.get('https://corona-api.com/countries/us')#USA data
		api_request_in = requests.get('https://corona-api.com/countries/in')#India data
		api_request_br = requests.get('https://corona-api.com/countries/br')#Brezil data
		api_request_ru = requests.get('https://corona-api.com/countries/ru')#Russia data

		api_json_data_us = json.loads(api_request_us.content) #USA data
		latest_data_us = api_json_data_us['data']['timeline'][1:8]
		latest_data_us_new = api_json_data_us['data']['timeline'][1]

		api_json_data_in = json.loads(api_request_in.content) #India data
		latest_data_in = api_json_data_in['data']['timeline'][1:8]
		latest_data_in_new = api_json_data_in['data']['timeline'][1]

		api_json_data_br = json.loads(api_request_br.content) #Brezil data
		latest_data_br = api_json_data_br['data']['timeline'][1:8]
		latest_data_br_new = api_json_data_br['data']['timeline'][1]

		api_json_data_ru = json.loads(api_request_ru.content) #Brezil data
		latest_data_ru = api_json_data_ru['data']['timeline'][1:8]
		latest_data_ru_new = api_json_data_ru['data']['timeline'][1]

		deaths = api_country_data['data']['timeline'][0]['deaths']
		recovered = api_country_data['data']['timeline'][0]['recovered']
		confirmed = api_country_data['data']['timeline'][0]['confirmed']
		deathperc = (deaths/confirmed)*100  #death %
		recoper = (recovered/confirmed)*100 #recover %
		pichartdata = {'dper': deathperc, 'rper':recoper}	

		xaxis.reverse()
		yaxis1.reverse()
		yaxis2.reverse()

		# x = api_country_data['data']['name']
		# print(x)
		
	except Exception as e:
		apidata = 'Error..'
		if apidata == 'Error..':
			return HttpResponse("<h1>There is a problem in connecting with API, Please Check..</h1>")
	return render(request, 'country.html', {'cdata':api_country_latest, 'carddata':card_data, 'pichartdata':pichartdata, 'usdata':latest_data_us, 'indata':latest_data_in, 'brdata':latest_data_br, 'rudata':latest_data_ru, 'usnewdata':latest_data_us_new, 'innewdata':latest_data_in_new, 'brnewdata':latest_data_br_new, 'runewdata':latest_data_ru_new, 'xaxis':xaxis, 'yaxis1':yaxis1, 'yaxis2':yaxis2})







	# api_country = requests.get("https://corona-api.com/countries/"+ccode+"")
	# api_country_data = json.loads(api_country.content)
	# api_country_latest = api_country_data['data']['timeline'][0]
	# return JsonResponse(latest_data_us, safe=False)


