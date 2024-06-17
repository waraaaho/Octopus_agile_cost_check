from requests import get
import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from whatsapp import *
try:
    response = get("https://api.octopus.energy/v1/products/AGILE-FLEX-22-11-25/electricity-tariffs/E-1R-AGILE-FLEX-22-11-25-G/standard-unit-rates/", auth=("sk_live_DWM2zh5uWkwARd21TUB9lpDW", ""),)
except:
    print("Not able to retrieve data from Octopus Energy")
text = json.loads(response.text)
today = datetime.today()
for i, result in enumerate(text['results']):
    # get data from today and tmr
    if datetime.now().date() > datetime.strptime(result['valid_from'], '%Y-%m-%dT%H:%M:%SZ').date(): break

if i<48:
    today_tariff = pd.DataFrame(text['results'][:i])[::-1]
else:
    today_tariff = pd.DataFrame(text['results'][i-48:i])[::-1]
#today_tariff['valid_from'] = today_tariff['valid_from'].apply(lambda x: x[11:13])
today_tariff['value_inc_vat'] = today_tariff['value_inc_vat'].astype(float)

time_HM = today_tariff['valid_from'].apply(lambda x: x[11:16] )
x_labels = time_HM.apply(lambda x: x[:2] if x[-2]=="0" else "")
plt.figure(figsize=(12, 8))
ax = today_tariff['value_inc_vat'].plot(kind="bar")
ax.set_title(today.strftime("%Y%m%d %H:%M:%S"))
ax.set_ylabel("Amount (p)")
ax.set_xlabel("Time")
ax.set_xticklabels(x_labels,rotation=0)

plt.savefig(f"{today.strftime('%Y-%m-%d %H:%M:%S')}.jpeg")
if (today_tariff['value_inc_vat'] < 0).any():
    announce = "*Cashback Time*\n"
else:
    announce = "*Cheapest Time*\n"
announce += pd.concat([time_HM,today_tariff["value_inc_vat"].round(2)],axis=1).sort_values(by="value_inc_vat").iloc[:5].to_string(header = None,index = None)
pywhatkit.sendwhats_image("GPZpNoHuLGWEbmBwSwzyjD", f"{today.strftime('%Y-%m-%d %H:%M:%S')}.jpeg", f"{today.strftime('%Y-%m-%d')} "+announce)
