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
      <td style="cursor:pointer;" @click="go_flux(item.name)">{{ item.name }}</td>
      <td>
        <img style="cursor:pointer; width: 22px; margin-right: 8px;" src="../icons/play-fill.svg" @click="ejecutar_flujo"/>
        <img style="cursor:pointer; width: 22px; margin-right: 12px;" src="../icons/stop-fill.svg" @click="stop"/>
        <img style="cursor:pointer" src="../icons/pen-fill.svg" @click="editar(item.name)"/>
      </td>
      <td>{{ item.date }}</td>
      <td>{{ item.state }}</td>
      <td>{{ item.author }}</td>


    </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">

import router from "@/router";
import axios from "axios";
import {useStepStore} from "@/stores/steps";

const props = defineProps({
  items: Array,
  store: Object
})
const step_store = useStepStore();



const go_flux = (name:string)=> {
  if(props.store.$id == "project"){
    step_store.project_name = name;
    router.push({name:"home_flux", params:{project_name: name}})
  }
}

const new_flux = () => {
  router.push("new_flux")
}






const editar = (nombre_flujo: any) => {
  const path = '/api/flow/abrir'
  const json = {
    "name": nombre_flujo,
    "flux": "",
    "user":sessionStorage.getItem("user")
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