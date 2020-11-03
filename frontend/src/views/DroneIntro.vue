<template>
  <div>
      <DroneSpec />
      <Reviews />
  </div>
</template>

<script>
import DroneSpec from '@/components/droneintro/DroneSpec'
import Reviews from '@/components/droneintro/Reviews'

export default {
    name: 'DroneIntro',
    components: {
        DroneSpec,
        Reviews
    }
}
</script>

<style>

</style>