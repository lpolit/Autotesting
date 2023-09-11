<template>
  <table class="table">
    <thead>
    <tr>
      <th>ID</th>
      <th>Nombre</th>
      <th>Acciones</th>
      <th>Modificado</th>
      <th>Estado</th>
      <th>Autor</th>

    </tr>
    </thead>
    <tbody>
    <tr v-for="item in items" :key="item.id">
      <td>{{ item.id }}</td>
      <td>{{ item.nombre }}</td>
      <td>
        <img style="cursor:pointer; width: 22px; margin-right: 8px;" src="../icons/play-fill.svg" @click="ejecutar_flujo"/>
        <img style="cursor:pointer; width: 22px; margin-right: 12px;" src="../icons/stop-fill.svg" @click="stop"/>
        <img style="cursor:pointer" src="../icons/pen-fill.svg" @click="editar"/>
      </td>
      <td>{{ item.fecha }}</td>
      <td>{{ item.estado }}</td>
      <td>{{ item.autor }}</td>


    </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">

import router from "@/router";
import axios from "axios";
import {useStepStore} from "@/stores/steps";

const props = defineProps({
  items: Array
})
const step_store = useStepStore();

const playAccion = (id) => {
  // Implementa la lógica para la acción "play"
  console.log("Acción Play para el elemento con ID:", id);
};

const stopAccion = (id) => {
  // Implementa la lógica para la acción "stop"
  console.log("Acción Stop para el elemento con ID:", id);
};

const editAccion = (id) => {
  // Implementa la lógica para la acción "edit"
  console.log("Acción Edit para el elemento con ID:", id);
};

const new_flux = () => {
  router.push("new_flux")
}

const editar = () => {
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
</script>