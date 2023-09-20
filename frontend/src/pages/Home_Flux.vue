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
      <li class="breadcrumb-item"><a>{{step_store.project_name}}</a></li>
      <li class="breadcrumb-item active" aria-current="page">{{step_store.flux_name}}</li>
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
        <tablita :items="filtrarElementos" :store="project"/>
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
          <button @click="go_new_flux" class="btn btn-primary">Aceptar</button>
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
const flux_name = ref("");
const project_name = ref(router.currentRoute.value.params.project_name);
const flux_store = useFluxStore();
const step_store = useStepStore();


const new_flux = () => {
  flux_name.value = "";
  modal.value = true;
}

const go_new_flux = () =>{
  step_store.flux_name = flux_name.value;
  router.push({name:"new_flux", params:{project_name:project_name.value, flux_name:flux_name.value}})
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

const filtroTabla = ref("");
const selectedItemId = ref(null);

const filtrarElementos = computed(() => {
  const filtro = filtroTabla.value.toLowerCase();
  return flux_store.list.filter((item) => {
    return (
        item.id?.toString().includes(filtro) ||
        item.name?.toLowerCase().includes(filtro) ||
        item.date?.toLowerCase().includes(filtro) ||
        item.state?.toLowerCase().includes(filtro) ||
        item.author?.toLowerCase().includes(filtro)
    );
  });
});

</script>
<style>
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
