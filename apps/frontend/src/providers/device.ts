interface Reference {
  id: string
  repr: string
}

interface DeviceStateValue {
  state_property_id: Reference
  serialized_value: string
  timestamp: string
}

interface DeviceState {
  state: DeviceStateValue[]
}

export interface Device {
  id: string
  device_type_id: Reference
  house_id: Reference
  status: string
  description: string
  state: DeviceState
}

export const useDeviceProvider = () => {
  const baseUrl = 'http://localhost:8001/api/devices/'

  const list = async (): Promise<Device[]> => {
    const responseData = await fetch(baseUrl).then((response) => response.json())
    return responseData
  }

  const create = async (deviceData: Partial<Device>): Promise<Device> => {
    const responseData = await fetch(baseUrl, {
      method: 'post',
      body: JSON.stringify(deviceData),
      headers: new Headers({ 'content-type': 'application/json' }),
    }).then((response) => response.json())
    return responseData
  }

  return { list, create }
}
