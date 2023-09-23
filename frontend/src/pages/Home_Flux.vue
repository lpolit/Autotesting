<template>
  <header class="navbar navbar-expand-md navbar-light bg-light" style="border-bottom: 4px solid rgb(1 58 122); margin-bottom: 15px;height: 80px;">
    <a class="navbar-brand" href="#">
      <img src="logo.png" alt="Autotesting">
    </a>

    <div  class="navbar-collapse collapse navbar-align " >
      {{user_login}}
      <img width="35"  style="margin:0 15px 0 10px" src="avatar.png" alt="Autotesting">
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
        <button class="btn btn-primary" style="margin:11px 130px 33px 3px" @click="new_flux">Nuevo Flujo
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
          <input placeholder="Ingrese el nombre del Flujo" :autofocus="true" v-model="flux_name"/>
        </MDBModalBody>
        <MDBModalFooter>
          <button @click="modal.value=false" class="btn btn-danger">Cancel</button>
          <button @click="save_flux" class="btn btn-primary">Guardar</button>
<!--          <button @click="go_flux" class="btn btn-primary">Guardar e Ir</button>-->
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

const modal = ref();
const flux_store = useFluxStore();
const step_store = useStepStore();
const project_name = ref(step_store.project_name.split("-")[0]);
const project_id = ref(step_store.project_name.split("-")[1]);
const flux_name = ref("");
const flux_id = ref(0);
const list_fluxs = ref ([])
const user_login = ref(sessionStorage.getItem("user"));


const new_flux = () => {
  flux_name.value = "";
  flux_id.value = 0;
  modal.value = true;
}

const save_flux = ()=> {
  modal.value = false;
  let path = '';

  if (flux_id.value!=0) {
    path = '/api/flow/update/'+flux_id.value+'/'+ flux_name.value;
    axios.post(path).then((response) => {
      console.log(response.data)
      alert("Se Modifico Correctamente")
      load_table()
    }).catch((error) => {
      console.log(error)
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
      alert("Creacion Exitosa")
      load_table()
    }).catch((error) => {
      console.log(error)
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
  modal.value = state
}

const delete_flux = (id: any,) => {

  const path = '/api/flux/delete/'+id;

  axios.delete(path).then((response) => {
    console.log(response.data)
    alert("proceso Exitoso")

    load_table()
  }).catch((error) => {
    console.log(error)
  })


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
