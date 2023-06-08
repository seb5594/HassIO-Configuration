# Herzlich Willkommen!

Dies ist meine Konfiguration der Smart-Home Plattform <b>Home Assistant</b> für die Version <b>2023.5.3</b>.

## Hardware
Die Produktions-Instanz von Home Assistant wird betrieben vom [Home Assistant Betriebssystem](https://github.com/home-assistant/operating-system) auf einem alten [Intel-NUC7i3BNK](https://ark.intel.com/content/www/de/de/ark/products/95069/intel-nuc-kit-nuc7i3bnk.html) mit 16GB RAM.

Über die USB-Schnittstelle sind folgende Geräte angeschlossen:
  - [Google Coral USB-Beschleuniger](https://coral.ai/products/accelerator/) zur Objekt-Erkennung
  - [Phoscon Conbee 2 Stick](https://phoscon.de/en/conbee2) für das Zigbee-Protokol
  - USB-Stick für tägliche Sicherung.

## Sicherungen
Der Server wurde so konfiguriert, dass Sicherungen auf 2 Wegen funktionieren.
Als Hauptsicherungsspeicher dient ein alter 8GB großer USB-Stick, auf dem täglich die wichtigsten Daten lokal gespiegelt werden mithilfe vom R-Sync Addon.
Bei der zweiten Sicherung verlasse ich mich auf Google's Drive Dienst und dem Addon "Home Assistant Google Drive Backup".

## Ordnerstruktur
Die Haupt-Konfiguration dieses Servers befindet sich in der Datei [configuration.yaml](configuration.yaml). Die restliche Konfiguration ist im Ordner [includes](/includes) vorzufinden.
Die übrig verbleibenden YAML-Dateien sind Addon-Konfigurationen.

## Ein paar Statistiken über meine Installation:

Beschreibung | Wert
-- | --
Anzahl Sensoren | 553
Anzahl Entitäten | 1320
Anzahl Entitäten nach Domäne
  [`automation`](https://www.home-assistant.io/components/automation) | 50
  [`binary_sensor`](https://www.home-assistant.io/components/binary_sensor) | 82
  [`button`](https://www.home-assistant.io/components/button) | 8
  [`calendar`](https://www.home-assistant.io/components/calendar) | 8
  [`camera`](https://www.home-assistant.io/components/camera) | 13
  [`climate`](https://www.home-assistant.io/components/climate) | 4
  [`counter`](https://www.home-assistant.io/components/counter) | 1
  [`device_tracker`](https://www.home-assistant.io/components/device_tracker) | 90
  [`geo_location`](https://www.home-assistant.io/components/geo_location) | 100
  [`group`](https://www.home-assistant.io/components/group) | 16
  [`input_boolean`](https://www.home-assistant.io/components/input_boolean) | 12
  [`input_number`](https://www.home-assistant.io/components/input_number) | 2
  [`input_select`](https://www.home-assistant.io/components/input_select) | 3
  [`input_text`](https://www.home-assistant.io/components/input_text) | 4
  [`light`](https://www.home-assistant.io/components/light) | 34
  [`lock`](https://www.home-assistant.io/components/lock) | 2
  [`media_player`](https://www.home-assistant.io/components/media_player) | 12
  [`persistent_notification`](https://www.home-assistant.io/components/persistent_notification) | 1
  [`person`](https://www.home-assistant.io/components/person) | 6
  [`proximity`](https://www.home-assistant.io/components/proximity) | 4
  [`remote`](https://www.home-assistant.io/components/remote) | 1
  [`scene`](https://www.home-assistant.io/components/scene) | 1
  [`schedule`](https://www.home-assistant.io/components/schedule) | 1
  [`script`](https://www.home-assistant.io/components/script) | 26
  [`select`](https://www.home-assistant.io/components/select) | 19
  [`sensor`](https://www.home-assistant.io/components/sensor) | 553
  [`stt`](https://www.home-assistant.io/components/stt) | 1
  [`sun`](https://www.home-assistant.io/components/sun) | 1
  [`switch`](https://www.home-assistant.io/components/switch) | 109
  [`timer`](https://www.home-assistant.io/components/timer) | 1
  [`update`](https://www.home-assistant.io/components/update) | 145
  [`weather`](https://www.home-assistant.io/components/weather) | 1
  [`zone`](https://www.home-assistant.io/components/zone) | 9

## Meine installierten Erweiterungen / Addons:

### Erweiterungen / Add-ons
- AdGuard Home (4.8.7)
- Advanced SSH & Web Terminal (15.0.2)
- AirCast (3.5.3)
- Arpspoof (1.0.0-2)
- CEC Scanner (3.0)
- Check Home Assistant configuration (3.11.0)
- chrony (2.6.0)
- Crowdsec (1.5.2-ha1)
- Crowdsec Firewall Bouncer (v0.0.26-ha2)
- Dasshio (0.3.8)
- DeepStack (2021.09.1)
- diyHue (2.0.8)
- Double Take (1.13.1)
- Duck DNS (1.15.0)
- Epic Games Free (c0dfe30ee94fa609a9efcb5eb2b8fd0c1dafe6e2-2023-05-03-2)
- ESPHome (2023.5.5)
- File editor (5.6.0)
- Frigate (0.12.0)
- Gitea (1.19.3)
- Glances (0.19.2)
- Home Assistant Google Drive Backup (0.110.4)
- MariaDB (2.6.1)
- Mosquitto broker (6.2.1)
- Music Assistant BETA (2.0.0b32)
- Network UPS Tools (0.11.2)
- Nginx Proxy Manager (0.12.3)
- Paperless NGX (1.14.5)
- Portainer (2.18.3)
- PS5 MQTT (1.3.1)
- RPC Shutdown (2.4)
- rsync local (1.6.0)
- Samba share (10.0.2)
- Scrutiny (Full Access) (v0.7.1)
- Studio Code Server (5.5.5)
- Teamspeak server (3.13.6-8)
- Vaultwarden (Bitwarden) (0.19.4)
- VLC (0.2.0)
- wgeasy (7)
- Whisper (0.2.0)
- Xiaomi Mi Scale (0.3.6)
- Zigbee2MQTT (1.31.0-1)

### Benutzerdefinierte Integrationen
- [<img src="https://brands.home-assistant.io/_/adaptive_lighting/icon.png" height="24"/>](https://brands.home-assistant.io/_/adaptive_lighting/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/adaptive_lighting/icon.png" height="24"/>](https://brands.home-assistant.io/_/adaptive_lighting/icon.png#gh-light-mode-only) [Adaptive Lighting (1.12.0)](https://github.com/basnijholt/adaptive-lighting)
- [<img src="https://brands.home-assistant.io/_/alexa_media/icon.png" height="24"/>](https://brands.home-assistant.io/_/alexa_media/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/alexa_media/icon.png" height="24"/>](https://brands.home-assistant.io/_/alexa_media/icon.png#gh-light-mode-only) [Alexa Media Player (v4.6.4)](https://github.com/custom-components/alexa_media_player)
- [<img src="https://brands.home-assistant.io/_/anniversaries/icon.png" height="24"/>](https://brands.home-assistant.io/_/anniversaries/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/anniversaries/icon.png" height="24"/>](https://brands.home-assistant.io/_/anniversaries/icon.png#gh-light-mode-only) [Anniversaries (5.2.0)](https://github.com/pinkywafer/Anniversaries)
- [<img src="https://brands.home-assistant.io/_/average/icon.png" height="24"/>](https://brands.home-assistant.io/_/average/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/average/icon.png" height="24"/>](https://brands.home-assistant.io/_/average/icon.png#gh-light-mode-only) [Average Sensor (2.3.0)](https://github.com/Limych/ha-average)
- [<img src="https://brands.home-assistant.io/_/better_thermostat/icon.png" height="24"/>](https://brands.home-assistant.io/_/better_thermostat/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/better_thermostat/icon.png" height="24"/>](https://brands.home-assistant.io/_/better_thermostat/icon.png#gh-light-mode-only) [Better Thermostat (1.0.3)](https://github.com/KartoffelToby/better_thermostat)
- [<img src="https://brands.home-assistant.io/_/blitzortung/icon.png" height="24"/>](https://brands.home-assistant.io/_/blitzortung/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/blitzortung/icon.png" height="24"/>](https://brands.home-assistant.io/_/blitzortung/icon.png#gh-light-mode-only) [Blitzortung.Org Lightning Detector (v1.3.1)](https://github.com/mrk-its/homeassistant-blitzortung)
- [<img src="https://brands.home-assistant.io/_/browser_mod/icon.png" height="24"/>](https://brands.home-assistant.io/_/browser_mod/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/browser_mod/icon.png" height="24"/>](https://brands.home-assistant.io/_/browser_mod/icon.png#gh-light-mode-only) [Browser Mod (2.2.2)](https://github.com/thomasloven/hass-browser_mod)
- [<img src="https://brands.home-assistant.io/_/config_editor/icon.png" height="24"/>](https://brands.home-assistant.io/_/config_editor/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/config_editor/icon.png" height="24"/>](https://brands.home-assistant.io/_/config_editor/icon.png#gh-light-mode-only) [Config Editor (4.3)](https://github.com/htmltiger/config-editor)
- [<img src="https://brands.home-assistant.io/_/dwd_weather/icon.png" height="24"/>](https://brands.home-assistant.io/_/dwd_weather/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/dwd_weather/icon.png" height="24"/>](https://brands.home-assistant.io/_/dwd_weather/icon.png#gh-light-mode-only) [Deutscher Wetterdienst (v1.2.27)](https://github.com/FL550/dwd_weather)
- [<img src="https://brands.home-assistant.io/_/dwd_pollenflug/icon.png" height="24"/>](https://brands.home-assistant.io/_/dwd_pollenflug/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/dwd_pollenflug/icon.png" height="24"/>](https://brands.home-assistant.io/_/dwd_pollenflug/icon.png#gh-light-mode-only) [Dwd Pollenflug (1.0.3)](https://github.com/mampfes/hacs_dwd_pollenflug)
- [<img src="https://brands.home-assistant.io/_/feedparser/icon.png" height="24"/>](https://brands.home-assistant.io/_/feedparser/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/feedparser/icon.png" height="24"/>](https://brands.home-assistant.io/_/feedparser/icon.png#gh-light-mode-only) [Feedparser (0.1.9)](https://github.com/custom-components/feedparser)
- [<img src="https://brands.home-assistant.io/_/fontawesome/icon.png" height="24"/>](https://brands.home-assistant.io/_/fontawesome/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/fontawesome/icon.png" height="24"/>](https://brands.home-assistant.io/_/fontawesome/icon.png#gh-light-mode-only) [Fontawesome (2.1.5)](https://github.com/thomasloven/hass-fontawesome)
- [<img src="https://brands.home-assistant.io/_/frigate/icon.png" height="24"/>](https://brands.home-assistant.io/_/frigate/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/frigate/icon.png" height="24"/>](https://brands.home-assistant.io/_/frigate/icon.png#gh-light-mode-only) [Frigate (v4.0.0)](https://github.com/blakeblackshear/frigate-hass-integration)
- [<img src="https://brands.home-assistant.io/_/garbage_collection/icon.png" height="24"/>](https://brands.home-assistant.io/_/garbage_collection/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/garbage_collection/icon.png" height="24"/>](https://brands.home-assistant.io/_/garbage_collection/icon.png#gh-light-mode-only) [Garbage Collection (4.10.2)](https://github.com/bruxy70/Garbage-Collection)
- [<img src="https://brands.home-assistant.io/_/readme/icon.png" height="24"/>](https://brands.home-assistant.io/_/readme/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/readme/icon.png" height="24"/>](https://brands.home-assistant.io/_/readme/icon.png#gh-light-mode-only) [Generate Readme (0.5.0)](https://github.com/custom-components/readme)
- [<img src="https://brands.home-assistant.io/_/gtasks/icon.png" height="24"/>](https://brands.home-assistant.io/_/gtasks/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/gtasks/icon.png" height="24"/>](https://brands.home-assistant.io/_/gtasks/icon.png#gh-light-mode-only) [Google Tasks (v0.6.1)](https://github.com/myntath/gtasks-ha)
- [<img src="https://brands.home-assistant.io/_/hacs/icon.png" height="24"/>](https://brands.home-assistant.io/_/hacs/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/hacs/icon.png" height="24"/>](https://brands.home-assistant.io/_/hacs/icon.png#gh-light-mode-only) [HACS (1.32.1)](https://github.com/hacs/integration)
- [<img src="https://brands.home-assistant.io/_/healthchecksio/icon.png" height="24"/>](https://brands.home-assistant.io/_/healthchecksio/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/healthchecksio/icon.png" height="24"/>](https://brands.home-assistant.io/_/healthchecksio/icon.png#gh-light-mode-only) [Healthchecks.Io (22.2.0)](https://github.com/custom-components/healthchecksio)
- [<img src="https://brands.home-assistant.io/_/holidays/icon.png" height="24"/>](https://brands.home-assistant.io/_/holidays/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/holidays/icon.png" height="24"/>](https://brands.home-assistant.io/_/holidays/icon.png#gh-light-mode-only) [Holidays (1.9.6)](https://github.com/bruxy70/Holidays)
- [<img src="https://brands.home-assistant.io/_/localtuya/icon.png" height="24"/>](https://brands.home-assistant.io/_/localtuya/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/localtuya/icon.png" height="24"/>](https://brands.home-assistant.io/_/localtuya/icon.png#gh-light-mode-only) [Local Tuya (v5.1.0)](https://github.com/rospogrigio/localtuya)
- [<img src="https://brands.home-assistant.io/_/lovelace_gen/icon.png" height="24"/>](https://brands.home-assistant.io/_/lovelace_gen/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/lovelace_gen/icon.png" height="24"/>](https://brands.home-assistant.io/_/lovelace_gen/icon.png#gh-light-mode-only) [Lovelace Gen (0.1.1)](https://github.com/thomasloven/hass-lovelace_gen)
- [<img src="https://brands.home-assistant.io/_/hochwasserportal/icon.png" height="24"/>](https://brands.home-assistant.io/_/hochwasserportal/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/hochwasserportal/icon.png" height="24"/>](https://brands.home-assistant.io/_/hochwasserportal/icon.png#gh-light-mode-only) [Länderübergreifendes Hochwasser Portal (v0.0.2)](https://github.com/stephan192/hochwasserportal)
- [<img src="https://brands.home-assistant.io/_/edge_tts/icon.png" height="24"/>](https://brands.home-assistant.io/_/edge_tts/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/edge_tts/icon.png" height="24"/>](https://brands.home-assistant.io/_/edge_tts/icon.png#gh-light-mode-only) [Microsoft Edge Tts (None)](https://github.com/hasscc/hass-edge-tts)
- [<img src="https://brands.home-assistant.io/_/midea_ac_lan/icon.png" height="24"/>](https://brands.home-assistant.io/_/midea_ac_lan/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/midea_ac_lan/icon.png" height="24"/>](https://brands.home-assistant.io/_/midea_ac_lan/icon.png#gh-light-mode-only) [Midea Ac Lan (v0.3.16)](https://github.com/georgezhao2010/midea_ac_lan)
- [<img src="https://brands.home-assistant.io/_/monitor_docker/icon.png" height="24"/>](https://brands.home-assistant.io/_/monitor_docker/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/monitor_docker/icon.png" height="24"/>](https://brands.home-assistant.io/_/monitor_docker/icon.png#gh-light-mode-only) [Monitor Docker (1.14)](https://github.com/ualex73/monitor_docker)
- [<img src="https://brands.home-assistant.io/_/places/icon.png" height="24"/>](https://brands.home-assistant.io/_/places/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/places/icon.png" height="24"/>](https://brands.home-assistant.io/_/places/icon.png#gh-light-mode-only) [Places (v2.4.1)](https://github.com/custom-components/places)
- [<img src="https://brands.home-assistant.io/_/powercalc/icon.png" height="24"/>](https://brands.home-assistant.io/_/powercalc/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/powercalc/icon.png" height="24"/>](https://brands.home-assistant.io/_/powercalc/icon.png#gh-light-mode-only) [Powercalc (v1.6.5)](https://github.com/bramstroker/homeassistant-powercalc)
- [<img src="https://brands.home-assistant.io/_/pyscript/icon.png" height="24"/>](https://brands.home-assistant.io/_/pyscript/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/pyscript/icon.png" height="24"/>](https://brands.home-assistant.io/_/pyscript/icon.png#gh-light-mode-only) [Pyscript (1.4.0)](https://github.com/custom-components/pyscript)
- [<img src="https://brands.home-assistant.io/_/qr_generator/icon.png" height="24"/>](https://brands.home-assistant.io/_/qr_generator/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/qr_generator/icon.png" height="24"/>](https://brands.home-assistant.io/_/qr_generator/icon.png#gh-light-mode-only) [Qr Code Generator (v.1.0.4)](https://github.com/DeerMaximum/QR-Code-Generator)
- [<img src="https://brands.home-assistant.io/_/rewe/icon.png" height="24"/>](https://brands.home-assistant.io/_/rewe/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/rewe/icon.png" height="24"/>](https://brands.home-assistant.io/_/rewe/icon.png#gh-light-mode-only) [Rewe Discounts (2023.04.0)](https://github.com/FaserF/ha-rewe)
- [<img src="https://brands.home-assistant.io/_/rki_covid/icon.png" height="24"/>](https://brands.home-assistant.io/_/rki_covid/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/rki_covid/icon.png" height="24"/>](https://brands.home-assistant.io/_/rki_covid/icon.png#gh-light-mode-only) [Rki Covid Numbers (1.5.8)](https://github.com/thebino/rki_covid)
- [<img src="https://brands.home-assistant.io/_/ssh/icon.png" height="24"/>](https://brands.home-assistant.io/_/ssh/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/ssh/icon.png" height="24"/>](https://brands.home-assistant.io/_/ssh/icon.png#gh-light-mode-only) [Sensor.Ssh (1.15)](https://github.com/custom-components/sensor.ssh)
- [<img src="https://brands.home-assistant.io/_/snowtire/icon.png" height="24"/>](https://brands.home-assistant.io/_/snowtire/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/snowtire/icon.png" height="24"/>](https://brands.home-assistant.io/_/snowtire/icon.png#gh-light-mode-only) [Snowtire Sensor (1.4.5)](https://github.com/Limych/ha-snowtire)
- [<img src="https://brands.home-assistant.io/_/waste_collection_schedule/icon.png" height="24"/>](https://brands.home-assistant.io/_/waste_collection_schedule/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/waste_collection_schedule/icon.png" height="24"/>](https://brands.home-assistant.io/_/waste_collection_schedule/icon.png#gh-light-mode-only) [Waste Collection Schedule (1.40.0)](https://github.com/mampfes/hacs_waste_collection_schedule)
- [<img src="https://brands.home-assistant.io/_/watchman/icon.png" height="24"/>](https://brands.home-assistant.io/_/watchman/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/watchman/icon.png" height="24"/>](https://brands.home-assistant.io/_/watchman/icon.png#gh-light-mode-only) [Watchman (v0.6.1)](https://github.com/dummylabs/thewatchman)
- [<img src="https://brands.home-assistant.io/_/xiaomi_miot/icon.png" height="24"/>](https://brands.home-assistant.io/_/xiaomi_miot/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/xiaomi_miot/icon.png" height="24"/>](https://brands.home-assistant.io/_/xiaomi_miot/icon.png#gh-light-mode-only) [Xiaomi Miot Auto (v0.7.9)](https://github.com/al-one/hass-xiaomi-miot)
- [<img src="https://brands.home-assistant.io/_/zha_toolkit/icon.png" height="24"/>](https://brands.home-assistant.io/_/zha_toolkit/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/zha_toolkit/icon.png" height="24"/>](https://brands.home-assistant.io/_/zha_toolkit/icon.png#gh-light-mode-only) [🧰 Zha Toolkit   Service For Advanced Zigbee Usage (v0.8.39)](https://github.com/mdeweerd/zha-toolkit)

### Lovelace plugins
- [Apexcharts Card (v2.0.4)](https://github.com/RomRider/apexcharts-card)
- [Auto Entities (1.12.1)](https://github.com/thomasloven/lovelace-auto-entities)
- [Badge Card (None)](https://github.com/thomasloven/lovelace-badge-card)
- [Bar Card (3.2.0)](https://github.com/custom-cards/bar-card)
- [Battery Entity Row (v1.3.1)](https://github.com/benct/lovelace-battery-entity-row)
- [Battery State Card / Entity Row (v2.1.1)](https://github.com/maxwroc/battery-state-card)
- [Better Thermostat Ui (1.0.4)](https://github.com/KartoffelToby/better-thermostat-ui-card)
- [Button Card (v3.5.0)](https://github.com/custom-cards/button-card)
- [Card Mod (3.2.2)](https://github.com/thomasloven/lovelace-card-mod)
- [Card Tools (11)](https://github.com/thomasloven/lovelace-card-tools)
- [Config Editor Card (4.6)](https://github.com/htmltiger/config-editor-card)
- [Config Template Card (1.3.6)](https://github.com/iantrich/config-template-card)
- [Custom Icons (v0.3.7)](https://github.com/Mariusthvdb/custom-icons)
- [Dark Thermostat (0.0.5)](https://github.com/ciotlosm/lovelace-thermostat-dark-card)
- [Digital Clock (v1.2.4)](https://github.com/wassy92x/lovelace-digital-clock)
- [Dual Gauge Card (0.5.3)](https://github.com/custom-cards/dual-gauge-card)
- [Entity Attributes Card (0.1.2)](https://github.com/custom-cards/entity-attributes-card)
- [Flex Table   Highly Customizable, Data Visualization (v0.7.2)](https://github.com/custom-cards/flex-table-card)
- [Flexible Horseshoe Card For Lovelace (v1.2)](https://github.com/AmoebeLabs/flex-horseshoe-card)
- [Fold Entity Row (2.2.0)](https://github.com/thomasloven/lovelace-fold-entity-row)
- [Frigate Card (v5.1.1)](https://github.com/dermotduffy/frigate-hass-card)
- [Gauge Card (0.2.3)](https://github.com/custom-cards/gauge-card)
- [Github Flexi Card / Entity Row (v2.0.0)](https://github.com/maxwroc/github-flexi-card)
- [Ha Floorplan (1.0.34)](https://github.com/ExperienceLovelace/ha-floorplan)
- [Header Cards (0.0.10)](https://github.com/gadgetchnnel/lovelace-header-cards)
- [Home Assistant Swipe Navigation (v1.11.1)](https://github.com/zanna-37/hass-swipe-navigation)
- [Hourly Weather Card (4.11.0)](https://github.com/decompil3d/lovelace-hourly-weather)
- [Layout Card (2.4.4)](https://github.com/thomasloven/lovelace-layout-card)
- [Logbook Card (1.11.0)](https://github.com/royto/logbook-card)
- [Midea Humidifier Card (v1.0.8)](https://github.com/sicknesz/midea-humidifier-card)
- [Mini Graph Card (v0.11.0)](https://github.com/kalkih/mini-graph-card)
- [Minimalistic Area Card (v1.1.16)](https://github.com/junalmeida/homeassistant-minimalistic-area-card)
- [Mushroom (v2.7.1)](https://github.com/piitaya/lovelace-mushroom)
- [Person (v0.8.0)](https://github.com/gerardag/person-entity-card)
- [Rmv Card (None)](https://github.com/custom-cards/rmv-card)
- [Room Card (1.07.23)](https://github.com/marcokreeft87/room-card)
- [Sankey Chart Card (v1.14.0)](https://github.com/MindFreeze/ha-sankey-chart)
- [Search Card (None)](https://github.com/postlund/search-card)
- [Seventeen Track Card (1.6.1)](https://github.com/KrX3D/seventeen-track-card)
- [Slider Button Card (v1.10.10)](https://github.com/custom-cards/slider-button-card)
- [Slider Entity Row (17.2.1)](https://github.com/thomasloven/lovelace-slider-entity-row)
- [State Switch (1.9.5)](https://github.com/thomasloven/lovelace-state-switch)
- [Tab Redirect Card (None)](https://github.com/ben8p/lovelace-tab-redirect-card)
- [Tankerkoenig Card (v1.2.2)](https://github.com/KrX3D/tankerkoenig-card)
- [Tv Remote Card (v0.2.1)](https://github.com/marrobHD/tv-card)
- [Unused Card (1.1)](https://github.com/custom-cards/unused-card)
- [Uptime Card (v0.14.0)](https://github.com/dylandoamaral/uptime-card)
- [Vertical Slider Cover Card (v0.1.5)](https://github.com/konnectedvn/lovelace-vertical-slider-cover-card)
- [Weather Radar Card (v2.1.0)](https://github.com/Makin-Things/weather-radar-card)
- [Your Ha Digital Twin Floor3D Card (v.1.5.3)](https://github.com/adizanni/floor3d-card)

### Themen
- [Blue Night Theme](https://github.com/home-assistant-community-themes/blue-night)
- [Catppuccin Theme](https://github.com/catppuccin/home-assistant)
- [Google Theme   Based On The Android Light And Dark Interface](https://github.com/JuanMTech/google-theme)
- [Mushroom Themes](https://github.com/piitaya/lovelace-mushroom-themes)
- [Nordic Theme](https://github.com/coltondick/nordic-theme-main)
- [Whatsapp Theme](https://github.com/robinwittebol/whatsapp-theme)
- [Windows 10 Themes](https://github.com/mikosoft83/hass-windows10-themes)


### Github
![Letzter commit](https://img.shields.io/github/last-commit/seb5594/HassIO-Configuration?style=flat-square)
![Commit Aktivität](https://img.shields.io/github/commit-activity/w/seb5594/HassIO-Configuration?style=flat-square)

***

Wie alle anderen Home Assistant-Instanzen oder Smart-Home Systeme ist auch diese Konfiguration eine laufende Arbeit, die niemals zu 100 % erfüllt sein wird :D