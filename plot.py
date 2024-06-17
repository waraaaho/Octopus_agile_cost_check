import pandas as pd
import matplotlib.pyplot as plt

def plot(today, text)
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

    return today_tariff
