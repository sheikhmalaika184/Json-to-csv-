import json
import csv
import ijson

# opening a csv file in writing mode
file = open("allowed-amounts-multiple-plan-sample.csv","w")
#creating a writer to write in file 
file_writer = csv.writer(file)
#writing headers in csv file 
file_writer.writerow(("Sr","Reporting entity name","Reporting entity type" , "Last updated on" , "Version","Name","Billing code type","Billing code type version","Billing code","Description","Tin type","Tin Value","Service code","Billing class","Allowed amount","Billed charge" , "Npi"))

with open("allowed-amounts-multiple-plan-sample.json", "rb") as f:
  count = 0
  # these values will be same for every entity 
  reporting_entity_name = "cms" # reporting_entity_name tag
  reporting_entity_type = "cms" # reporting_entity_type tag
  last_updated_on = "2020-08-27" # last_updated_on tag
  version = "1.0.0" #version tag
  # out of network is a list thats why we are looping through out_of_network
  for record in ijson.items(f, "out_of_network.item"): # ijson.items is a function to read json array
    name = record['name'] # name tag in out_of_network
    billing_code_type = record['billing_code_type'] # billing_code_type tag in out_of_network
    billing_code_type_version = record['billing_code_type_version'] # billing_code_type_version tag in out_of_network
    billing_code = record['billing_code'] # billing_code tag in out_of_network
    description = record['description'] # description tag in out_of_network
    for allowed_amount in record['allowed_amounts']: #allowed_amounts is also a list with in out_of_network tag that why we are looping through the list
      # tin entity has two more entities type and value 
      tin_type = allowed_amount['tin']['type'] # this is tin and type
      tin_value = allowed_amount['tin']['value'] # this is tin and value 
      service_codes = allowed_amount['service_code'] # list of services code 
      billing_class = allowed_amount['billing_class'] # billing_class tag in list of allowed_amounts
      allowed_amount1 = allowed_amount['payments'][0]['allowed_amount'] # allowed_amount tag in list of allowed_amounts
      for provider in allowed_amount['payments'][0]['providers']: # providers is a list within allowed_amount so we are looping through
        billed_charge = provider['billed_charge'] # billed charge tag in providers list
        npi =  provider['npi'] # npi tag in providers list
        # writing each row in a file 
        file_writer.writerow((count, reporting_entity_name, reporting_entity_type , last_updated_on , version, name , billing_code_type, billing_code_type_version, billing_code, description, tin_type, tin_value, service_codes, billing_class, allowed_amount1, billed_charge , npi))
        count = count + 1
file.close()
        



 