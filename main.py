import pandas as pd

#from USDMX.sdmx_data_access import SDMX_DataAccess
#from USDMX import sdmx_data_access
#import src.USDMX.sdmx_data_access
#from src.USDMX.sdmx_data_access import SDMX_DataAccess
import src.USDMX.sdmx_data_access

#https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,GLOBAL_DATAFLOW,1.0/CZE+DZA.CME_MRM0.?format=sdmx-compact-2.1
sdmx_endpoint = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest"
sdmx_access = src.USDMX.sdmx_data_access.SDMX_DataAccess(sdmx_endpoint)

#df = sdmx_access.get_data("UNICEF","GLOBAL_DATAFLOW","1.0","CZE+DZA.CME_MRM0.")

# print(df.head())

dsd = sdmx_access.get_dataflow_info("UNICEF","GLOBAL_DATAFLOW","1.0", "en")



import sdmxthon
#https://docs.sdmxthon.meaningfuldata.eu/packages/model/item.html#sdmxthon.model.itemScheme.Item

message_metadata = sdmxthon.read_sdmx("https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/dataflow/UNICEF/GLOBAL_DATAFLOW/1.0/?detail=full&references=all")
#message_data = sdmxthon.read_sdmx('https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,GLOBAL_DATAFLOW,1.0/CZE+DZA.CME_MRM0.')

'''
print(message_metadata.type)

print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].name)

print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.dimension_codes)
print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.attribute_codes)
print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.measure_code)


print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content)

print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["dimensions"])
print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["dimensions"]["REF_AREA"])
print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["dimensions"]["REF_AREA"].concept_identity.name)
print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["dimensions"]["REF_AREA"].representation)
print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["dimensions"]["REF_AREA"].local_representation)


print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["attributes"]["UNIT_MEASURE"].concept_identity)
print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["attributes"]["UNIT_MEASURE"].representation)
print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["attributes"]["UNIT_MEASURE"].local_representation.codelist)

print(message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["attributes"]["UNIT_MEASURE"].local_representation.codelist.items)


cl = message_metadata.content["Dataflows"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.content["attributes"]["UNIT_MEASURE"].local_representation.codelist

for c in cl.items:
    print(c, cl.items[c], cl.items[c].name)
'''

#print(message_metadata.content)



#print(message_metadata.content["DataStructures"]["UNICEF:GLOBAL_DATAFLOW(1.0)"].structure.dimension)



# dsd = sdmx_access.get_dataflow_info("UNICEF","GLOBAL_DATAFLOW","1.0", "en")
print(dsd)
print(dsd["dsd"]["dims"])
# print(dsd["dsd"]["attribs"])
# print(dsd["dsd"]["measures"])