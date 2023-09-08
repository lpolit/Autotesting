<template>
  <input type="button" value="INGRESAR" @click="new_flux"/>
</template>

<script setup lang="ts">
import router from "@/router";

const new_flux = () => {
  router.push("new_flux")
}
</script>
