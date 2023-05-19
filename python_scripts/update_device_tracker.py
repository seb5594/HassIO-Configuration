inputEntity = data.get("entity_id")
inputLatitude = data.get("latitude")
inputLongitude = data.get("longitude")
inputStateObject = hass.states.get(inputEntity)

inputAttributesObject = inputStateObject.attributes.copy()

if inputLatitude is not None:
    inputAttributesObject["latitude"] = inputLatitude

if inputLongitude is not None:
    inputAttributesObject["longitude"] = inputLongitude

hass.states.set(inputEntity, inputStateObject.state, inputAttributesObject)