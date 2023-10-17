<template>
  <header class="navbar navbar-expand-md navbar-light bg-light" style="border-bottom: 4px solid rgb(1 58 122); margin-bottom: 15px;height: 80px;">
    <a class="navbar-brand" href="#">
      <img src="logo.png" alt="Autotesting">
    </a>

    <div  class="navbar-collapse collapse navbar-align " >
      {{user_login}}
      <div class="dropdown">
        <button class="btn dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
          <img width="35" style="margin:0 15px 0 10px" src="../icons/avatar.png" alt="Autotesting">
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" style="left: -80px">
          <li><a class="dropdown-item" @click="log_out">Cambiar Contraseña</a></li>
          <li><a class="dropdown-item" @click="log_out">Salir</a></li>
        </ul>
      </div>
    </div>
  </header>

  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><a href="/#/home_project">{{project_name}}</a></li>
    </ol>
  </nav>

  <div class="page-container">
    <div class="page-content">
      <navbar class="flex-container" >
        <button class="btn btn-primary" style="margin:11px 130px 33px 3px" @click="new_flux"><img src="../icons/plus-circle.svg" style="width: 20px; margin-right: 10px; filter: invert(1);"/>Nuevo Flujo
        </button>
      </navbar>
      <div>
        <input v-model="filtroTabla" placeholder="Filtrar por nombre"/>
        <tablita @onEdit="edit_flux" @onDelete="delete_flux" :project_name="project_name" :items="filtrarElementos" :store="flux_store"/>
      </div>
      <MDBModal
          id="modal"
          tabindex="-1"
          v-model="modal"
      >
        <MDBModalHeader>
          <MDBModalTitle> Nombre del Flujo</MDBModalTitle>
        </MDBModalHeader>
        <MDBModalBody>
          <input style="width: 100%" placeholder="Ingrese el nombre del Flujo" :autofocus="true" v-model="flux_name"/>
        </MDBModalBody>
        <MDBModalFooter>
          <button @click="set_modal(false)" class="btn btn-danger">Cancel</button>
          <button @click="save_flux" class="btn btn-primary">Guardar</button>
<!--          <button @click="go_flux" class="btn btn-primary">Guardar e Ir</button>-->
        </MDBModalFooter>
      </MDBModal>
      <MDBModal
          id="modal_delete"
          tabindex="-1"
          v-model="modal_delete"
      >
        <MDBModalHeader>
          <MDBModalTitle> Eliminar Flujo </MDBModalTitle>
        </MDBModalHeader>
        <MDBModalBody>
          <label>¿Esta seguro que desea eliminar el Flujo?</label>
        </MDBModalBody>
        <MDBModalFooter>
          <button @click="set_modal_delete(false)" class="btn btn-danger">Cancel</button>
          <button @click="delete_flux_db" class="btn btn-primary">Aceptar</button>
        </MDBModalFooter>
      </MDBModal>

    </div>
  </div>
</template>

<script setup lang="ts">
import router from "@/router";
import {onMounted, ref, computed} from "vue";
import axios from "axios";
import Tablita from "@/components/Table.vue";
import {useFluxStore} from "@/stores/fluxs"

import {
  MDBModal,
  MDBModalHeader,
  MDBModalTitle,
  MDBModalBody,
  MDBModalFooter
} from "mdb-vue-ui-kit";
import {useStepStore} from "@/stores/steps";
import { notify } from "@kyvg/vue3-notification";
const modal = ref();
const modal_delete = ref();
const flux_store = useFluxStore();
const step_store = useStepStore();
const project_name = ref(step_store.project_name.split("-")[0]);
const project_id = ref(step_store.project_name.split("-")[1]);
const flux_name = ref("");
const flux_id = ref(0);
const list_fluxs = ref ([])
const user_login = ref(sessionStorage.getItem("user"));

const notificar = (type: string, title: string, text: string) =>{
  notify({
    type: type,
    title: title,
    text: text,
  });
}

const new_flux = () => {
  flux_name.value = "";
  flux_id.value = 0;
  set_modal(true);
}

const save_flux = ()=> {
  set_modal(false);
  let path = '';

  if (flux_id.value!=0) {
    path = '/api/flow/update/'+flux_id.value+'/'+ flux_name.value;
    axios.post(path).then((response) => {
      console.log(response.data)
      notificar("success", "Operacion exitosa", "La Modificacion sobre el flujo "+response.data+" se realizo con exito")
      load_table()
    }).catch((error) => {
      console.log(error)
      notificar("error", "Fallo", "Fallo al modificar el Flujo!")
    })
  }else{
    const date_aux = new Date();
    const date = date_aux.toLocaleDateString() + " " + date_aux.toLocaleTimeString();
    const state = "-";
    path = '/api/flow/insert';

    const json = {
      "flux_name": flux_name.value,
      "date": date,
      "state": state,
      "flux": " ",
      "user": user_login.value,
      "project_id": project_id.value
    };

    axios.post(path, json).then((response) => {
      console.log(response.data)
      notificar("success", "Operacion exitosa", "La Creacion del flujo "+response.data+" se realizo con exito")
      load_table()
    }).catch((error) => {
      console.log(error)
      notificar("error", "Fallo", "Fallo la creacion del flujo!")
    })
  }
}

const load_table =() =>{
  list_fluxs.value=[]
  axios.post('/api/flow/getAll/'+ project_id.value.toString()).then((response) => {
    let list_aux = response.data;
    for (let proj of list_aux) {
      list_fluxs.value.push({
        "id": proj[0],
        "name": proj[1],
        "date": proj[2],
        "state": proj[3],
        "author": proj[4],
      });
    }

  }).catch((error) => {
    console.log(error)
  })
}

onMounted (() => {
  try {
    if (user_login.value == "" || user_login.value == null){
      router.push("/")
    }
  } catch (error) {
    router.push("/")
    console.log(error, 'error from decoding token')
  }
  load_table();
})

const filtroTabla = ref("");
const filtrarElementos = computed(() => {
  const filtro = filtroTabla.value.toLowerCase();
  return list_fluxs.value.filter((item) => {
    return (
        item.id?.toString().includes(filtro) ||
        item.name?.toLowerCase().includes(filtro) ||
        item.date?.toLowerCase().includes(filtro) ||
        item.state?.toLowerCase().includes(filtro) ||
        item.author?.toLowerCase().includes(filtro)
    );
  });
});


const edit_flux = (state: any, id: any, flx_name: any) => {
  flux_name.value = flx_name;
  flux_id.value = id;
  set_modal(state)
}

const set_modal = (valor: boolean) =>{
  modal.value = valor;
}

const set_modal_delete = (valor: boolean) =>{
  modal_delete.value = valor;
}

const delete_flux = (id: any) => {
  flux_id.value = id;
  set_modal_delete(true);
}

const delete_flux_db = () => {

  const path = '/api/flow/delete/'+ flux_id.value;

  axios.delete(path).then((response) => {
    console.log(response.data)
    load_table()
    notificar("success", "Operacion exitosa", "La eliminacion del Flujo "+response.data+" se realizo con exito")
  }).catch((error) => {
    console.log(error)
    notificar("error", "Fallo", "Fallo al eliminar el flujo!")
  })

  set_modal_delete(false);

}

const log_out = () => {
  step_store.$reset()
  sessionStorage.clear()
  router.push("/")
}


</script>
<style>
a {
  text-decoration: none;
}
.page-container {
  display: flex;
  flex-direction: column;
  min-height: 70vh;
  margin-top: 20px;
}

.page-content {
  flex: 1;
}
.navbar-brand img {
  width: 150px;
}

.navbar-align{
  justify-content: end;
  align-self: end;
  margin-bottom: 1%;
}
.breadcrumb {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 0.75rem 1rem;
  margin-top: -16px;
  list-style: none;
  background-color: #e9ecef;
  border-radius: 0.25rem;
  color:#007bff;
}

</style>
