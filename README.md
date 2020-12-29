# WeatherPi

Weather Station for Raspberry Pi and Small LCDs  

![](https://github.com/SWhardfish/WeatherPiDisplay/blob/master/WeatherDisplayExample.png)

---


## Features

- Modularized display parts 
- Heat Index color / UV Index color support  
- Custom module support
  [External modules](#external-modules)
- i18n (internationalization) support
- Historical graphs for Temperature, Pressure, Precipitation and Windspeed  


## Installation

### Install and update tools

```bash
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install rng-tools gettext -y
sudo apt-get install python3-pygame python3-pillow -y
```

### Install WeatherPi

```bash
git clone https://github.com/SWhardfish/WStationDisplay
cd WeatherPi
```

### Copy config file and customise it

Replace the XXXXXXX for the OpenWeathermap appid and optionally the Google Maps API key. Also update the address and long/lat for your location.

```bash
cp example.480x800.config.json config.json
```

#### config.json

| Name                    |          | Default                                  | Description                                                                                                        |
| ----------------------- | -------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| openweather_appid       | required |                                          | **[OpenWeather API Key](https://openweathermap.org/api)**                                                          |
| google_api_key          | optional |                                          | [Google Geocoding API key](https://developers.google.com/maps/documentation/geocoding/start)                       |
| address                 | optional |                                          | The address of a location. <br> latitude and longitude can be omitted if google_api_key and address are specified. |
| latitude <br> longitude | required |                                          | The latitude and longitude of a location (in decimal degrees). Positive is east, negative is west.                 |
| locale                  | required | en_GB.UTF-8                              | Locale. Specify the display language of time and weather information.                                              |
| units                   | required | metric                                   | Unit of weather 　 information. (imperial: Fahrenheit, metric: Celsius)                                            |
| SDL_FBDEV               | required | /dev/fb0                                 | Frame buffer device to use in the linux fbcon driver.                                         |
| display                 | required |                                          | Display size. [Width, Height]                                                                                      |
| fonts.name              | required | ARIALUNI                                 | Font name.                                                                                                         |
| fonts.size              | required | {xlarge": 40, "mlarge": 35, "large": 30, "medium": 22, "smallmedium": 18, "small": 16, "xsmall": 12} | Font size list. (Style name and point)                                                                             |

- for language-support, units, latitude and longitude please refer to -> **[OpenWeather API Docs](https://openweathermap.org/api/one-call-api)**

### Setting up the services

```bash
cd
cd WeatherPi
sudo cp WeatherPi_Service.sh /etc/init.d/WeatherPi
sudo chmod +x /etc/init.d/WeatherPi
sudo chmod +x WeatherPi.py
sudo systemctl enable WeatherPi
```

### Run python with root privileges

- this is useful if you like to run your python scripts on boot and with sudo support in python

```bash
sudo chown -v root:root /usr/bin/python3
sudo chmod -v u+s /usr/bin/python3
```

### sStting up python3 as default interpreter

- this should start your wanted python version just by typing `python` in the terminal
- helps if you have projects in python2 and python3 and don't want to hassle with the python version in your service scripts

```bash
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
```

- if you use DHT11, DHT22 and AM2302 sensor, install Adafruit_DHT

```bash
sudo pip3 install Adafruit_DHT
```

- if you use DigistampTemper, install pyusb

```bash
sudo pip3 install pyusb
```

- You must install matplotlib to be able to generate the Weather historical graphs.

```bash
sudo pip3 install matplotlib
```

### Test

```bash
./WeatherPi.py [--debug]
```

## Customize weather icons

By default, the OpenWeather icons are resised to the display, but you can change the to any icon you like.
To change the icons, place the following 18 icons in the icons folder:  


- 01d.pnng, 01n.png, 02d.pnng, 02n.png, 03d.pnng, 03n.png, 04d.pnng, 04n.png, 09d.pnng, 09n.png, 10d.pnng, 10n.png, 11d.pnng, 11n.png, 13d.pnng, 13n.png, 50d.pnng, 50n.png,

| Day icon name | Default                                                             | Night icon name | Default                                                             | Description      |
| ------------- | ------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------- | ---------------- |
| 01d.png       | <img width="100" src="http://openweathermap.org/img/wn/01d@2x.png"> | 01n.png         | <img width="100" src="http://openweathermap.org/img/wn/01n@2x.png"> | clear sky        |
| 02d.png       | <img width="100" src="http://openweathermap.org/img/wn/02d@2x.png"> | 02n.png         | <img width="100" src="http://openweathermap.org/img/wn/02n@2x.png"> | few clouds       |
| 03d.png       | <img width="100" src="http://openweathermap.org/img/wn/03d@2x.png"> | 03n.png         | <img width="100" src="http://openweathermap.org/img/wn/03n@2x.png"> | scattered clouds |
| 04d.png       | <img width="100" src="http://openweathermap.org/img/wn/04d@2x.png"> | 04n.png         | <img width="100" src="http://openweathermap.org/img/wn/04n@2x.png"> | broken clouds    |
| 09d.png       | <img width="100" src="http://openweathermap.org/img/wn/09d@2x.png"> | 09n.png         | <img width="100" src="http://openweathermap.org/img/wn/09n@2x.png"> | shower rain      |
| 10d.png       | <img width="100" src="http://openweathermap.org/img/wn/10d@2x.png"> | 10n.png         | <img width="100" src="http://openweathermap.org/img/wn/10n@2x.png"> | rain             |
| 11d.png       | <img width="100" src="http://openweathermap.org/img/wn/11d@2x.png"> | 11n.png         | <img width="100" src="http://openweathermap.org/img/wn/11n@2x.png"> | thunderstorm     |
| 13d.png       | <img width="100" src="http://openweathermap.org/img/wn/13d@2x.png"> | 13n.png         | <img width="100" src="http://openweathermap.org/img/wn/13n@2x.png"> | snow             |
| 50d.png       | <img width="100" src="http://openweathermap.org/img/wn/50d@2x.png"> | 50n.png         | <img width="100" src="http://openweathermap.org/img/wn/50n@2x.png"> | mist             |

## I18n

You can change the display language of dates and information.  

<img width="480" alt="480x320 ja" src="https://user-images.githubusercontent.com/129797/82272445-9b308500-99b5-11ea-86bb-f590bd726338.png">

fig 480x320 ja

<img width="240" alt="240x320 ja" src="https://user-images.githubusercontent.com/129797/82272447-9d92df00-99b5-11ea-8e67-c972453e346e.png">

fig 240x320 ja

### Font

Install the font for your locale. I recommend using the [Google Fonts](https://fonts.google.com/) and [Google ARIALUNI](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/ipwn/arialuni.ttf) as used in this build.  

[How to install fonts](https://www.google.com/get/noto/help/install/)

### Translation files

- init message.po file

```bash
cd locale
cp -Rp en <your language>
```

- edit messages.po (msgstr section).

```bash
msgfmt <your language>/LC_MESSAGES/messages.po -o <your language>/LC_MESSAGES/messages.po
```

## Modules

All modules require the following configuration:

```
"modules": [
  {
    "module": "<Module Name>",
    "config": {
      "rect": [<x>, <y>, <width>, <height>]
    }
  }
```

### Built-in Modules

| Name                | Description                         | Options                                 | Size              |
| ------------------- | ----------------------------------- | --------------------------------------- | ----------------- |
| Alerts              | Any severe weather alerts pertinent | None                                    | 240x15 - 480x15   |
| Clock               | Current Time                        | None                                    | 140x60            |
| Location            | Current location                    |                                         | 140x15            |
| Weather             | Current Weather                     | icon_size (default 100)                 | 240x100 - 480x100 |
| WeatherForecast     | Weather Forecast                    | forecast_days<br>icon_size (default 50) | 240x80 - 480x80   |
| WeatherHistoryGraph | Weather History                     | history is set to store the last 24h    | 450x480           |
|SunriseSunset        | Sunrise, Sunset time                | icon_size (default 40)                  | 80x80             |
| MoonPhase           | Moon Phase                          | icon_size (default 50)                  | 80x80             |
| Wind                | Wind direction, speed               | icon_size (default 30)                  | 80x80             |

### External modules

| Name                                                            | Description                                                             | Options                                                                                                                                                                               | Size              |
| --------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| DHT                                                             | Adafruit temperature/humidity sensor                                    | pin: pin number<br>correction_value: (調整値)                                                                                                                                         | 60x60 - 70x120    |
| [DigistampTemper](https://github.com/miyaichi/DigisparkTemper)  | DigisparkTemper (usb temperature/humidity sensor)                       | correction_value: (調整値)                                                                                                                                                            | 60x60 - 70x120    |
| [IrMagitianT](http://www.omiya-giken.com/?page_id=837)          | Temperature sensor on the infrared remote control system "irMagician-T" | correction_value: (調整値)                                                                                                                                                            | 60x35 - 70x60     |
| [JMAAlerts](http://xml.kishou.go.jp/xmlpull.html)               | JMA weather alerts<br>(気象庁の注意報、警報、特別警報を表示)            | prefecture: (都道府県)<br>city: (市区町村)                                                                                                                                            | 240x15 - 480x15   |
| [NatureRemo](https://nature.global/jp/landing-page-dm-g/)       | Temperature and humidity sensor on Nature Remo/Remo mini                | token: (access tokens to access Nature API)<br>name: (device name)                                                                                                                    | 100x60            |
| PIR                                                             | PIR(Passive Infrared Ray）Motion Sensor                                 | pin: pin number<br>power_save_delay: delay (in seconds) before the monitor will be turned off.                                                                                        | None              |
| SelfUpdate                                                      | Update and restart if there is a newer version on GitHub                | check_interval (default 86400 # once a day)                                                                                                                                           | -                 |
| [TEMPer](http://www.pcsensor.com/usb-hygrometer/temperhum.html) | TEMPerHUM/TEMPer thermometer & hygrometer                               | correction_value: (調整値)                                                                                                                                                            | 60x60 - 70x120    |
| WeatherForcustGraph                                             | Plots weather condition data for the next 48 hours.                     | conditions: Weather conditions to display.<br>Available weather conditions is following:<br>temperature, apparentTemperature, dewPoint, humidity, pressure, windSpeed, uvIndex, ozone | The size you want |

## Plots a graph

Temperature and humidity sensors and weather forecast data can be displayed in a graph.

- Temperature and humidity sensor modules (DHT, DigisparkTemper, IrMagitianT, NatureRemo, TEMPer)
  Each module holds the last 6 hours of sensor data and can display it graphically. To plot the graph, define the graph drawing area with "graph_rect" parameter in the module config.


  example config:

  ```
  {
    "module": "<Module name>",
    "config": {
      "rect": [x, y, width, height],
      ...
      "graph_rect": [x, y, width, height]
    }
  }
  ```

- WeatherForcastGraph module
  It can graphically display the weather data for the next 48 hours or 7 days provided by OpenWeather. To plot the graph, define up to two weather condition names with the conditions parameter in the module's config.

  ![fig](https://user-images.githubusercontent.com/129797/74575281-b4e2ba80-4fc9-11ea-8b8b-72ca6b28c418.png)

  example config:

  ```
  {
    "module": "WeatherForcustGraph",
    "config": {
      "rect": [x, y, width, height],
      "block": "hourly",
      "conditions": ["temperature", "humidity"]
    }
  }
  ```

  - Available block and conditions are following:
    hourly:
    temperature, apparentTemperature, dewPoint, humidity,
    pressure, windSpeed, uvIndex, ozone
    daily:
    precipIntensity, precipIntensityMax, precipProbability,
    temperatureHigh, temperatureLow, apparentTemperatureHigh,
    apparentTemperatureLow, dewPoint, humidity, pressure,
    windSpeed, windGust, cloudCover, uvIndex, uvIndexTime,
    visibility, ozone, temperatureMin, temperatureMax,
    apparentTemperatureMin, "apparentTemperatureMax

    Refer: **[OpenWeather API Docs](https://openweathermap.org/api/one-call-api)**

## Credit

- [WeatherPi_TFT](https://github.com/LoveBootCaptain/WeatherPi_TFT) His python application is what got me started working on this.
- [WeatherPi](https://github.com/miyaichi/WeatherPi) For his excellent coding skills and modularising the original [WeatherPi_TFT](https://github.com/LoveBootCaptain/WeatherPi_TFT) and inspiration.
- [adafruit](https://github.com/adafruit) for [hardware](https://www.adafruit.com/) and [tutorials](https://learn.adafruit.com/)
- [OpenWeather](https://openweathermap.org/) weather api and [documentation](https://openweathermap.org/api/one-call-api)
- [Google Fonts](https://fonts.google.com/)
- [Google NotoFonts](https://www.google.com/get/noto/)
