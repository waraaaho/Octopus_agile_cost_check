from requests import get
import json
from datetime import datetime
from whatsapp import *
from plot import plot

try:
    response = get("https://api.octopus.energy/v1/products/AGILE-FLEX-22-11-25/electricity-tariffs/E-1R-AGILE-FLEX-22-11-25-G/standard-unit-rates/", auth=("sk_live_DWM2zh5uWkwARd21TUB9lpDW", ""),)
except:
    print("Not able to retrieve data from Octopus Energy")
text = json.loads(response.text)
today = datetime.today()
for i, result in enumerate(text['results']):
    # get data from today and tmr
    if datetime.now().date() > datetime.strptime(result['valid_from'], '%Y-%m-%dT%H:%M:%SZ').date(): break

today_tariff = plot(today, text)

if (today_tariff['value_inc_vat'] < 0).any():
    announce = "*Cashback Time*\n"
else:
    announce = "*Cheapest Time*\n"
announce += pd.concat([time_HM,today_tariff["value_inc_vat"].round(2)],axis=1).sort_values(by="value_inc_vat").iloc[:5].to_string(header = None,index = None)
pywhatkit.sendwhats_image("GPZpNoHuLGWEbmBwSwzyjD", f"{today.strftime('%Y-%m-%d %H:%M:%S')}.jpeg", f"{today.strftime('%Y-%m-%d')} "+announce)
