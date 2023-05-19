# Willkommen!

Dies ist meine Home Assistant Konfiguration für Version <b>2023.5.3</b>.

## Hardware
Die Produktions-Instanz von Home Assistant wird betrieben vom [Home Assistant Betriebssystem](https://github.com/home-assistant/operating-system) auf einem alten [Intel-NUC7i3BNK](https://ark.intel.com/content/www/de/de/ark/products/95069/intel-nuc-kit-nuc7i3bnk.html).

## Ein paar Statistiken über meine Installation:

Beschreibung | Wert
-- | --
Anzahl Entitäten | 1089
Anzahl Sensoren | 457
Entities in der [`person`](https://www.home-assistant.io/components/person) domain | 6
Entities in der [`update`](https://www.home-assistant.io/components/update) domain | 161
Entities in der [`binary_sensor`](https://www.home-assistant.io/components/binary_sensor) domain | 81
Entities in der [`group`](https://www.home-assistant.io/components/group) domain | 16
Entities in der [`sensor`](https://www.home-assistant.io/components/sensor) domain | 457
Entities in der [`calendar`](https://www.home-assistant.io/components/calendar) domain | 8
Entities in der [`light`](https://www.home-assistant.io/components/light) domain | 31
Entities in der [`persistent_notification`](https://www.home-assistant.io/components/persistent_notification) domain | 3
Entities in der [`switch`](https://www.home-assistant.io/components/switch) domain | 77
Entities in der [`scene`](https://www.home-assistant.io/components/scene) domain | 1
Entities in der [`counter`](https://www.home-assistant.io/components/counter) domain | 1
Entities in der [`sun`](https://www.home-assistant.io/components/sun) domain | 1
Entities in der [`timer`](https://www.home-assistant.io/components/timer) domain | 1
Entities in der [`zone`](https://www.home-assistant.io/components/zone) domain | 9
Entities in der [`input_number`](https://www.home-assistant.io/components/input_number) domain | 2
Entities in der [`input_select`](https://www.home-assistant.io/components/input_select) domain | 3
Entities in der [`input_boolean`](https://www.home-assistant.io/components/input_boolean) domain | 12
Entities in der [`input_text`](https://www.home-assistant.io/components/input_text) domain | 4
Entities in der [`schedule`](https://www.home-assistant.io/components/schedule) domain | 1
Entities in der [`media_player`](https://www.home-assistant.io/components/media_player) domain | 6
Entities in der [`climate`](https://www.home-assistant.io/components/climate) domain | 4
Entities in der [`proximity`](https://www.home-assistant.io/components/proximity) domain | 4
Entities in der [`camera`](https://www.home-assistant.io/components/camera) domain | 12
Entities in der [`script`](https://www.home-assistant.io/components/script) domain | 26
Entities in der [`select`](https://www.home-assistant.io/components/select) domain | 19
Entities in der [`stt`](https://www.home-assistant.io/components/stt) domain | 1
Entities in der [`lock`](https://www.home-assistant.io/components/lock) domain | 2
Entities in der [`remote`](https://www.home-assistant.io/components/remote) domain | 1
Entities in der [`weather`](https://www.home-assistant.io/components/weather) domain | 1
Entities in der [`automation`](https://www.home-assistant.io/components/automation) domain | 50
Entities in der [`device_tracker`](https://www.home-assistant.io/components/device_tracker) domain | 83
Entities in der [`button`](https://www.home-assistant.io/components/button) domain | 5

## Meine installierten Erweiterungen:

### Add-ons
- AdGuard Home (4.8.7)
- Advanced SSH & Web Terminal (15.0.0)
- AirCast (3.5.3)
- Arpspoof (1.0.0-2)
- CEC Scanner (3.0)
- Check Home Assistant configuration (3.11.0)
- chrony (2.6.0)
- Crowdsec (1.4.6)
- Crowdsec Firewall Bouncer (v0.0.26)
- Dasshio (0.3.8)
- DeepStack (2021.09.1)
- diyHue (2.0.8)
- Double Take (1.13.1)
- Duck DNS (1.15.0)
- Epic Games Free (c0dfe30ee94fa609a9efcb5eb2b8fd0c1dafe6e2-2023-05-03)
- ESPHome (2023.5.1)
- File editor (5.6.0)
- Frigate (0.12.0)
- Gitea (1.19.3)
- Glances (0.19.0)
- Home Assistant Google Drive Backup (0.110.4)
- MariaDB (2.6.1)
- Mosquitto broker (6.2.1)
- Music Assistant BETA (2.0.0b30)
- Network UPS Tools (0.11.2)
- Nginx Proxy Manager (0.12.3)
- Paperless NGX (1.14.4-2)
- Portainer (2.18.2)
- PS5 MQTT (1.3.1)
- RPC Shutdown (2.4)
- rsync local (1.6.0)
- Samba share (10.0.1)
- Scrutiny (Full Access) (v0.7.1)
- Studio Code Server (5.5.5)
- Teamspeak server (3.13.6-8)
- Vaultwarden (Bitwarden) (0.19.4)
- VLC (0.2.0)
- wgeasy (7)
- Whisper (0.2.0)
- Xiaomi Mi Scale (0.3.6)
- Zigbee2MQTT (1.30.4-1)

### Benutzerdefinierte Integrationen
- [Adaptive Lighting 1.11.0](https://github.com/basnijholt/adaptive-lighting)
- [Alexa Media Player v4.6.4](https://github.com/custom-components/alexa_media_player)
- [Anniversaries 5.2.0](https://github.com/pinkywafer/Anniversaries)
- [Average Sensor 2.3.0](https://github.com/Limych/ha-average)
- [Better Thermostat 1.0.3](https://github.com/KartoffelToby/better_thermostat)
- [Blitzortung.Org Lightning Detector v1.3.1](https://github.com/mrk-its/homeassistant-blitzortung)
- [Browser Mod 2.2.1](https://github.com/thomasloven/hass-browser_mod)
- [Config Editor 4.3](https://github.com/htmltiger/config-editor)
- [Deutsche Bahn 1.0.2](https://github.com/FaserF/ha-deutschebahn)
- [Deutscher Wetterdienst v1.2.27](https://github.com/FL550/dwd_weather)
- [Dwd Pollenflug 1.0.3](https://github.com/mampfes/hacs_dwd_pollenflug)
- [Entity Controller v9.6.0](https://github.com/danobot/entity-controller)
- [Feedparser 0.1.9](https://github.com/custom-components/feedparser)
- [Fontawesome 2.1.5](https://github.com/thomasloven/hass-fontawesome)
- [Frigate v4.0.0](https://github.com/blakeblackshear/frigate-hass-integration)
- [Garbage Collection 4.10.2](https://github.com/bruxy70/Garbage-Collection)
- [Generate Readme 0.5.0](https://github.com/custom-components/readme)
- [Google Tasks v0.6.1](https://github.com/myntath/gtasks-ha)
- [HACS 1.32.1](https://github.com/hacs/integration)
- [Healthchecks.Io 22.2.0](https://github.com/custom-components/healthchecksio)
- [Holidays 1.9.4](https://github.com/bruxy70/Holidays)
- [Local Tuya v5.1.0](https://github.com/rospogrigio/localtuya)
- [Lovelace Gen 0.1.1](https://github.com/thomasloven/hass-lovelace_gen)
- [Länderübergreifendes Hochwasser Portal v0.0.2](https://github.com/stephan192/hochwasserportal)
- [Microsoft Edge Tts None](https://github.com/hasscc/hass-edge-tts)
- [Midea Ac Lan v0.3.16](https://github.com/georgezhao2010/midea_ac_lan)
- [Monitor Docker 1.14](https://github.com/ualex73/monitor_docker)
- [Npm Switches v1.0.0](https://github.com/InTheDaylight14/nginx-proxy-manager-switches)
- [Places v2.3.5](https://github.com/custom-components/places)
- [Powercalc v1.6.1](https://github.com/bramstroker/homeassistant-powercalc)
- [Pyscript 1.4.0](https://github.com/custom-components/pyscript)
- [Qr Code Generator v.1.0.4](https://github.com/DeerMaximum/QR-Code-Generator)
- [Rewe Discounts 2023.04.0](https://github.com/FaserF/ha-rewe)
- [Rki Covid Numbers 1.5.8](https://github.com/thebino/rki_covid)
- [Sensor.Ssh 1.15](https://github.com/custom-components/sensor.ssh)
- [Snowtire Sensor 1.4.5](https://github.com/Limych/ha-snowtire)
- [Variable v0.15.0](https://github.com/snarky-snark/home-assistant-variables)
- [Waste Collection Schedule 1.39.0](https://github.com/mampfes/hacs_waste_collection_schedule)
- [Watchman v0.6.1](https://github.com/dummylabs/thewatchman)
- [Whatspie None](https://github.com/arifwn/homeassistant-whatspie-integration)
- [Xiaomi Miot Auto v0.7.8](https://github.com/al-one/hass-xiaomi-miot)
- [🧰 Zha Toolkit   Service For Advanced Zigbee Usage v0.8.39](https://github.com/mdeweerd/zha-toolkit)

### Lovelace plugins
- [Apexcharts Card v2.0.4](https://github.com/RomRider/apexcharts-card)
- [Auto Entities 1.12.1](https://github.com/thomasloven/lovelace-auto-entities)
- [Auto Reload None](https://github.com/ben8p/lovelace-auto-reload-card)
- [Badge Card None](https://github.com/thomasloven/lovelace-badge-card)
- [Bar Card 3.2.0](https://github.com/custom-cards/bar-card)
- [Battery Entity Row v1.3.1](https://github.com/benct/lovelace-battery-entity-row)
- [Battery State Card / Entity Row v2.1.1](https://github.com/maxwroc/battery-state-card)
- [Better Thermostat Ui 1.0.4](https://github.com/KartoffelToby/better-thermostat-ui-card)
- [Button Card v3.5.0](https://github.com/custom-cards/button-card)
- [Card Mod 3.2.2](https://github.com/thomasloven/lovelace-card-mod)
- [Card Tools 11](https://github.com/thomasloven/lovelace-card-tools)
- [Config Editor Card 4.6](https://github.com/htmltiger/config-editor-card)
- [Config Template Card 1.3.6](https://github.com/iantrich/config-template-card)
- [Custom Icons v0.3.7](https://github.com/Mariusthvdb/custom-icons)
- [Custom Ui 20221115](https://github.com/Mariusthvdb/custom-ui)
- [Dark Thermostat 0.0.5](https://github.com/ciotlosm/lovelace-thermostat-dark-card)
- [Datetime Card v1.0.2](https://github.com/a-p-z/datetime-card)
- [Digital Clock v1.2.4](https://github.com/wassy92x/lovelace-digital-clock)
- [Dual Gauge Card 0.5.3](https://github.com/custom-cards/dual-gauge-card)
- [Entity Attributes Card 0.1.2](https://github.com/custom-cards/entity-attributes-card)
- [Flex Table   Highly Customizable, Data Visualization v0.7.2](https://github.com/custom-cards/flex-table-card)
- [Flexible Horseshoe Card For Lovelace v1.2](https://github.com/AmoebeLabs/flex-horseshoe-card)
- [Fold Entity Row 2.2.0](https://github.com/thomasloven/lovelace-fold-entity-row)
- [Frigate Card v5.0.0](https://github.com/dermotduffy/frigate-hass-card)
- [Gauge Card 0.2.3](https://github.com/custom-cards/gauge-card)
- [Github Flexi Card / Entity Row v2.0.0](https://github.com/maxwroc/github-flexi-card)
- [Ha Floorplan 1.0.34](https://github.com/ExperienceLovelace/ha-floorplan)
- [Hass Hue Icons v1.2.51](https://github.com/arallsopp/hass-hue-icons)
- [Header Cards 0.0.10](https://github.com/gadgetchnnel/lovelace-header-cards)
- [Home Assistant Swipe Navigation v1.11.1](https://github.com/zanna-37/hass-swipe-navigation)
- [Hourly Weather Card 4.11.0](https://github.com/decompil3d/lovelace-hourly-weather)
- [Hue Like Light Card v1.3.0](https://github.com/Gh61/lovelace-hue-like-light-card)
- [Hui Element None](https://github.com/thomasloven/lovelace-hui-element)
- [Layout Card 2.4.4](https://github.com/thomasloven/lovelace-layout-card)
- [List Card 0.1.2](https://github.com/iantrich/list-card)
- [Logbook Card 1.10.1](https://github.com/royto/logbook-card)
- [Lovelace Card Preloader 0.0.5](https://github.com/gadgetchnnel/lovelace-card-preloader)
- [Midea Humidifier Card v1.0.8](https://github.com/sicknesz/midea-humidifier-card)
- [Mini Graph Card v0.11.0](https://github.com/kalkih/mini-graph-card)
- [Minimalistic Area Card v1.1.16](https://github.com/junalmeida/homeassistant-minimalistic-area-card)
- [Multiple Entity Row v4.4.1](https://github.com/benct/lovelace-multiple-entity-row)
- [Mushroom v2.7.1](https://github.com/piitaya/lovelace-mushroom)
- [Person v0.8.0](https://github.com/gerardag/person-entity-card)
- [Rmv Card None](https://github.com/custom-cards/rmv-card)
- [Room Card 1.07.22](https://github.com/marcokreeft87/room-card)
- [Sankey Chart Card v1.13.0](https://github.com/MindFreeze/ha-sankey-chart)
- [Search Card None](https://github.com/postlund/search-card)
- [Seventeen Track Card 1.6.1](https://github.com/KrX3D/seventeen-track-card)
- [Slider Button Card v1.10.10](https://github.com/custom-cards/slider-button-card)
- [Slider Entity Row 17.2.1](https://github.com/thomasloven/lovelace-slider-entity-row)
- [State Switch 1.9.5](https://github.com/thomasloven/lovelace-state-switch)
- [Tab Redirect Card None](https://github.com/ben8p/lovelace-tab-redirect-card)
- [Tankerkoenig Card v1.2.2](https://github.com/KrX3D/tankerkoenig-card)
- [Template Entity Row 1.3.2](https://github.com/thomasloven/lovelace-template-entity-row)
- [Tv Remote Card v0.2.1](https://github.com/marrobHD/tv-card)
- [Unused Card 1.1](https://github.com/custom-cards/unused-card)
- [Uptime Card v0.14.0](https://github.com/dylandoamaral/uptime-card)
- [Vertical Slider Cover Card v0.1.5](https://github.com/konnectedvn/lovelace-vertical-slider-cover-card)
- [Vertical Stack In Card v0.4.4](https://github.com/ofekashery/vertical-stack-in-card)
- [Weather Radar Card v2.1.0](https://github.com/Makin-Things/weather-radar-card)
- [Your Ha Digital Twin Floor3D Card v.1.5.3](https://github.com/adizanni/floor3d-card)

### Themen
- [Blue Night Theme](https://github.com/home-assistant-community-themes/blue-night)
- [Catppuccin Theme](https://github.com/catppuccin/home-assistant)
- [Google Theme   Based On The Android Light And Dark Interface](https://github.com/JuanMTech/google-theme)
- [Mushroom Themes](https://github.com/piitaya/lovelace-mushroom-themes)
- [Nordic Theme](https://github.com/coltondick/nordic-theme-main)
- [Whatsapp Theme](https://github.com/robinwittebol/whatsapp-theme)
- [Windows 10 Themes](https://github.com/mikosoft83/hass-windows10-themes)

***

![GitHub letzter commit](https://img.shields.io/github/last-commit/seb5594/HassIO-Configuration?style=flat-square)
![GitHub commit Aktivität](https://img.shields.io/github/commit-activity/w/seb5594/HassIO-Configuration?style=flat-square)