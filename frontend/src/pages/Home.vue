<template>
  <input type="button" value="INGRESAR" @click="new_flux"/>
  el usuario es ... {{user_login}}
  <input type="button" value="CARGAR FLUJO PRUEBA1" @click="abrir"/>
</template>

<script setup lang="ts">
import router from "@/router";
import {onMounted, ref} from "vue";
import axios from "axios";
import {useStepStore} from "@/stores/steps";

const new_flux = () => {
  router.push("new_flux")
}

const step_store = useStepStore();

const abrir = () => {
  const path = '/api/flow/abrir'
  const json = {
    "name": "prueba1",
    "flux": ""
  };

  axios.post(path, json).then((response) => {
    sessionStorage.setItem("steps",response.data)
    step_store.$dispose()
    router.push("new_flux")
  }).catch((error) => {
    console.log(error)
  })

}

const user_login = ref(String);

onMounted (() => {
  try {
    let user = sessionStorage.getItem("user")
    if (user == "" || user == null){
      router.push("/")
    }
    user_login.value=user
  } catch (error) {
    router.push("/")
    console.log(error, 'error from decoding token')
  }
})

</script>
