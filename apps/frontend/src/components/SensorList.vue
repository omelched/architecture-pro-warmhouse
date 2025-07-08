<script setup lang="ts">
import { useDeviceStore } from '@/stores/device';


const deviceStore = useDeviceStore()
deviceStore.load()

const onAddDevice = () => {
  deviceStore.create('Новый датчик', "on")
}
</script>

<template>
  <button @click="onAddDevice">
    Добавить датчик
  </button>
  <ul>
    <li v-for="device in deviceStore.objects">
      <div>
        id={{ device.id }}
      </div>
      <div>
        description={{ device.description }}
      </div>
      <div>
        house={{ device.house_id }}
      </div>
      <div>
        state={{ device.state.filter(state => state.property_name === 'value') }}
      </div>
      <div>
        status={{ device.status }}
      </div>

    </li>
  </ul>
</template>

<style scoped></style>