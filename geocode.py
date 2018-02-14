import urllib,json,urllib.request,sys      #for import urllib.request because some times error
loc=sys.argv[1]     # for getting input via command prompt  in loc variable , list of argv and second would be our location 
encode_loc=urllib.parse.quote(loc)     # encoded string 
url = "https://maps.googleapis.com/maps/api/geocode/json?address="+encode_loc  
#print(url)
response=urllib.request.urlopen(url)     #  to get httpresponse
if(response.code==200):                   # 200 for successfully getting response
 data=json.loads(response.read().decode())     # convert json string to dictionary 

 if(data['status']=='OK'):              # if input address is correct  then we would get status ok in geocode api 
  results=data['results']              # we have only two nodes results and second one results 
                                            # we have  only one child of results 
  print(results[0]['formatted_address'])           # for accessing formatted_address
  print(results[0]['geometry']['location'])        #  for getting lat and lng 
 else:
    print("wrongly typed address")
else:
    print("error")
  
