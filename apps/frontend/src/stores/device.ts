import { useDeviceProvider, type Device } from '@/providers/device'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useDeviceStore = defineStore('device', () => {
  const deviceProvider = useDeviceProvider()

  const objects = ref<Device[]>([])
  const isLoading = ref(false)

  const load = async () => {
    if (isLoading.value) return

    const searchResult = await deviceProvider.list()
    objects.value = searchResult
  }

  const create = async (description: string, status: string) => {
    const createResult = await deviceProvider.create({ description, status })

    load()
  }

  return { objects, isLoading, load, create }
})
