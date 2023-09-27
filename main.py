import pandas as pd

from USDMX_reader.sdmx_data_access import SDMX_DataAccess

#https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,GLOBAL_DATAFLOW,1.0/CZE+DZA.CME_MRM0.?format=sdmx-compact-2.1
sdmx_endpoint = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest"
sdmx_access = SDMX_DataAccess(sdmx_endpoint)

df = sdmx_access.get_data("UNICEF","GLOBAL_DATAFLOW","1.0","CZE+DZA.CME_MRM0.")

print(df.head())

