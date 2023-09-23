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
      <td style="cursor:pointer;" @click="go(item.name, item.id)">{{ item.name }}</td>
      <td>

        <img style="cursor:pointer; width: 22px; margin-right: 25px;" src="../icons/go.svg"  @click="go(item.name, item.id)"/>
        <img style="cursor:pointer; width: 22px; margin-right: 25px;" src="../icons/pen-fill.svg" @click="editar(item.id, item.name)"/>
        <img style="cursor:pointer; width: 22px; margin-right: 25px;" src="../icons/delete.svg" @click="eliminar(item.id)" />
        <img v-if="props.store.$id == 'flux'" style="cursor:pointer; width: 22px; margin-right: 25px;" src="../icons/play-fill.svg" @click="ejecutar_flujo"/>
        <img v-if="props.store.$id == 'flux'" style="cursor:pointer; width: 22px; margin-right: 25px;" src="../icons/stop-fill.svg" @click="stop"/>


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
import {ref} from "vue/dist/vue";

const props = defineProps({
  items: Array,
  store: Object,
  project_name: String
})
const step_store = useStepStore();
const emit = defineEmits(['onEdit', 'onDelete'])


const go = (name:string, id:number)=> {
  if(props.store.$id == "project"){
    step_store.project_name = name + "-" + id;
    router.push({name:"home_flux"})
  }else{
    step_store.flux_name = name + "-" + id;

    const path = '/api/flow/abrir/'+id
    axios.post(path).then((response) => {
      sessionStorage.setItem("steps",response.data)
      step_store.$dispose()
      router.push("new_flux")
    }).catch((error) => {
      console.log(error)
    })
  }
}

const new_flux = () => {
  router.push("new_flux")
}






const editar = (id: any, name: any) => {
  emit('onEdit',true, id, name)
}

const eliminar = (id: any) => {
  emit('onDelete', id)
}
</script>