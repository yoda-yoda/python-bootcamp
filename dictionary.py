addressBook = {
	'Denis' : 'denis@deebeat.com',
	'Moses' : 'moses@huawei.org',
	'James' : 'james@deitel.org'
}

print'\nDictionary One:'
for name, address in addressBook.items():
	print "%s ->> %s" % (name, address)

print"Dictionary one has ",len(addressBook)," items"

print'\nDictionary two: '

userInp = raw_input("Enter a city or country: ")

dictionary = dict(
	nairobi = 'kenya',
 	cairo = 'egypt',
 	mogadishu = 'somalia',
 	kigali = 'rwanda',
 	capeTown = 'south africa',
 	paris = 'france',
 	rome = 'italy',
 	london = 'britain',
 	kampala = 'uganda',
 	lagos = 'nigeria',
 	daaresalaam = 'tanzania',
 	brasil = 'brazil',
 	dakar = 'senegal' 
  )

cityDictionary = dict(
	kenya = 'nairobi',
	egypt = 'cairo',
	somalia = 'mogadishu',
	nigeria= 'lagos',
	france = 'paris',
	brazil = 'brasil',
	britain = 'london',
	uganda = 'kampala',
	senegal = 'dakar',
	italy = 'rome',
	ghana = 'accra',
	algeria = 'algia',
	sudan = 'khartoum'
  )

print dictionary.keys()

if dictionary.__contains__(userInp.lower()):
	print "%s is the capital city of %s" % (userInp.capitalize(), dictionary.get(userInp.lower()).capitalize())

elif cityDictionary.__contains__(userInp.lower()):
	print "%s's capital city is %s" % (userInp.capitalize(), cityDictionary.get(userInp.lower()).capitalize())

else:
	print "No results found :( "



# for town, country in dictionary.items():
#  	print "%s -->> %s" % (town, country)

# if len(dictionary) > 1:
# 	suffix = 's\n'
# else:
# 	suffix = ''

# print"Dictionary Two has",len(dictionary),"item",suffix






