<template>
  <table class="table">
    <thead>
    <tr>
      <th>ID</th>
      <th>Nombre</th>
      <th></th>
      <th>Fh. Ult Ejecucion</th>
      <th v-if="props.store.$id == 'flux'" style="text-align: center">Estado Ejecucion</th>
      <th v-if="props.store.$id == 'flux'"  style="text-align: center">Resultado</th>
      <th>Autor</th>
      <th>Acciones</th>

    </tr>
    </thead>
    <tbody>

    <tr v-for="item in items" :key="item.id">

      <td>{{ item.id }}</td>
      <td style="cursor:pointer; width: 20%" @click="go(item.name, item.id)">{{ item.name }} </td>
      <td style="cursor:pointer; width: 10%"> <img style="cursor:pointer; width: 15px;" src="../icons/pen-fill.svg" @click="editar(item.id, item.name)"/>
      </td>
      <td>{{ item.date }}</td>
      <td v-if="props.store.$id == 'flux'"  style="text-align: center;" ><img  :id="'img_estado_'+item.id" width="25" src="src/icons/senal-stop.png" ></td>
      <td v-if="props.store.$id == 'flux'"  style="text-align: center; cursor: pointer" ><img  @click="go_result(item.id)" :id="'img_resultado_'+item.id" width="25" src="src/icons/linea.png" ></td>
      <td>{{ item.author }}</td>

      <td>
        <div class="dropdown">
          <button class="btn" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="../icons/three-dots-vertical.svg" style="width: 15px;"/>
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" style="left: -80px">
            <li v-if="props.store.$id == 'flux'"><a class="dropdown-item"  @click="ejecutar_flujo(item.id)"><img style="width: 20px; margin-left: -3.5px" src="../icons/play-fill.svg"/> Ejecutar </a></li>
            <li v-if="props.store.$id == 'flux'"><a class="dropdown-item"  @click="stop(item.id)"><img style="width: 20px; margin-left: -3.5px" src="../icons/stop-fill.svg"/> Detener </a></li>

            <li><a class="dropdown-item"  @click="go(item.name, item.id)"><img style="width: 15px;  " src="../icons/go.svg"/> Ingresar </a></li>
            <li><a class="dropdown-item"  @click="editar(item.id, item.name)"><img style="width: 15px;" src="../icons/pen-fill.svg"/> Editar</a></li>
            <li><a class="dropdown-item"  @click="eliminar(item.id)"><img style="width: 15px;" src="../icons/delete.svg"/> Eliminar </a></li>
            </ul>
        </div>

      </td>

    </tr>
    </tbody>
  </table>

  <MDBModal
      id="modal_delete"
      tabindex="-1"
      v-model="result_modal"
  >
    <MDBModalHeader>
      <MDBModalTitle> Resultado de la ejecucion de:  <i>{{result_view.flux_name.split("-")[0]}}</i> </MDBModalTitle>
    </MDBModalHeader>
    <MDBModalBody>
      <ul class="list-group">
        <li  v-for="item in result_view.list_steps.steps" :key="item.id" :class="[item.status == 'OK' ? 'list-group-item list-group-item-success' : 'list-group-item list-group-item-danger']"  v-html=" '<h5>'+item.name +' </h5>'+item.description"></li>





      </ul>
    </MDBModalBody>
    <MDBModalFooter>
      <button @click="set_modal(false)" class="btn btn-danger">Cerrar</button>
    </MDBModalFooter>
  </MDBModal>

</template>

<script setup lang="ts">

import router from "@/router";
import axios from "axios";
import {useStepStore} from "@/stores/steps";
import {notify} from "@kyvg/vue3-notification";

import {ref} from "vue";
import {MDBCardText, MDBModal, MDBModalBody, MDBModalFooter, MDBModalHeader, MDBModalTitle} from "mdb-vue-ui-kit";

const props = defineProps({
  items: Array,
  store: Object,
  project_name: String
})
let step_store = useStepStore();
const emit = defineEmits(['onEdit', 'onDelete'])

let esta_detenido = false;
let flow_id = 0;
const estado_resultado = ref('')
const result_modal = ref();
const result_view = ref();

const set_modal = (valor: boolean) =>{
  result_modal.value = valor;
}
const go = (name:string, id:number)=> {
  if(props.store.$id == "project"){
    step_store.project_name = name + "-" + id;
    router.push({name:"home_flux"})
  }else{
    step_store.flux_name = name + "-" + id;
    reset_flux_result()
    abrir_flujo(id);
    router.push({name:"new_flux"})
  }
}

const go_result = (id:number)=> {
  let store_resul = JSON.parse(sessionStorage.getItem("result_"+id))
  result_view.value = store_resul
  set_modal(true)

}

const reset_flux_result=()=>{
  for(let st of step_store.list_steps.steps) {
    st.status = ""
  }
  return JSON.stringify(step_store)
}
const notificar = (type: string, title: string, text: string) =>{
  notify({
    type: type,
    title: title,
    text: text,
  });
}
const abrir_flujo= async (id:number)=>{
  const path = '/api/flow/abrir/'+id
  await axios.post(path).then((response) => {
    let json = JSON.parse(response.data)
    step_store.list_steps.steps = json.list_steps.steps
  }).catch((error) => {
    console.log(error)
  })
}


const ejecutar_flujo = async ( id:number)=>{
  estado_resultado.value='';
  let path = '/api/flow/abrir/'+id
  await axios.post(path).then((response) => {
    let json = JSON.parse(response.data)
    step_store = json
  }).catch((error) => {
    console.log(error)
  })
  document.getElementById('img_estado_'+id.toString()).setAttribute("src","src/icons/loading.gif")
    console.log(step_store.list_steps)
    //reset_flux_result()
    path = '/api/flow'
    let json
    //is_disabled.value = true;
    notificar("info", "Ejecucion iniciada", "Se inicio la ejecucion del flujo ")
    for (let st of step_store.list_steps.steps) {
      if(!esta_detenido) {
        st.data.flow_id = flow_id
        json = JSON.parse(JSON.stringify(st.data))
        await axios.post(path, json).then((response) => {
          flow_id = response.data.flow_id
          st.status = "OK"
          st.data.flow_id = flow_id
          if (estado_resultado.value!= "ERROR") {
            estado_resultado.value = "OK"
            document.getElementById('img_resultado_' + id.toString()).setAttribute("src", "src/icons/ok.png")
          }
          if (response.data.variable_data !== null)
            var type = "";
          if (st.id === 12)
            type = "img"
          else
            type = "text"
          update_var(st.data.arguments.var_name, response.data.variable_data, st.orden, type)

        }).catch((error) => {
          console.log(error)
          st.status = "ERROR"
          estado_resultado.value = "ERROR"
          document.getElementById('img_resultado_'+id.toString()).setAttribute("src","src/icons/error.png")
        })
      }
    }
    //is_disabled.value = false;
    notificar("info", "Ejecucion Finalizada", "Finalizo la ejecucion del flujo")
  document.getElementById('img_estado_'+id.toString()).setAttribute("src","src/icons/senal-stop.png")
  sessionStorage.setItem("result_"+id, JSON.stringify(step_store))

}

const update_var = (var_key: any, new_value: any, index: any, type: string) => {
  let item = step_store.list_vars.find(it =>
      it.key === var_key);
  if (item !== undefined) {
    item.value = new_value;
    item.index = index;
    item.type = type;
  }
}

const stop =( id:number)=>{

  esta_detenido = true;
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

<style>
a{
  cursor:pointer;
}
</style>