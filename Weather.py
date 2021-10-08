import requests

class Weather():
    def __init__(self,City):
        self.City=City

    def Find_Data(self):
        URL = "xxxxxx".format(self.City)
        Data = requests.get(URL).json()

        Longitude=Data['coord']['lon']
        Latitude=Data['coord']['lat']

        Weather_ID=Data['weather'][0]['id']
        Main=Data['weather'][0]['main']
        Description=Data['weather'][0]['description']
        Icon=Data['weather'][0]['icon']

        Base=Data['base']

        Temp=Data['main']['temp']
        Feels_Like=Data['main']['feels_like']
        Temp_Min=Data['main']['temp_min']
        Temp_Max=Data['main']['temp_max']
        Pressure=Data['main']['pressure']
        Humidity=Data['main']['humidity']

        Visibility=Data['visibility']

        Speed=Data['wind']['speed']
        Degree=Data['wind']['deg']

        Clouds=Data['clouds']['all']

        DT=Data['dt']

        Country=Data['sys']['country']
        Sunrise=Data['sys']['sunrise']
        Sunset=Data['sys']['sunset']

        Timezone=Data['timezone']
        ID=Data['id']
        Name=Data['name']
        Code=Data['cod']

        return({'Longitude':Longitude,'Latitude':Latitude,'Weather_ID':Weather_ID,'Main':Main,'Description':Description,'Icon':Icon,'Base':Base,'Temp':Temp,'Feels_Like':Feels_Like
        ,'Temp_Min':Temp_Min,'Temp_Max':Temp_Max,'Pressure':Pressure,'Humidity':Humidity,'Visibility':Visibility,'Speed':Speed,'Degree':Degree
        ,'Clouds':Clouds,'DT':DT,'Country':Country,'Sunrise':Sunrise,'Sunset':Sunset,'Timezone':Timezone,'ID':ID,'Name':Name,'Code':Code})
