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

  <div class="page-container">
    <div class="page-content">
      <navbar class="flex-container" >
        <button class="btn btn-primary" style="margin:11px 130px 33px 3px" @click="new_project">Nuevo Proyecto
        </button>
      </navbar>
      <div>
        <input v-model="filtroTabla" placeholder="Filtrar por nombre"/>
        <tablita :items="filtrarElementos" :store="project_store"/>
      </div>
      <MDBModal
          id="modal"
          tabindex="-1"
          v-model="modal"
      >
        <MDBModalHeader>
          <MDBModalTitle> Nombre del Projecto</MDBModalTitle>
        </MDBModalHeader>
        <MDBModalBody>
          <input placeholder="Ingrese el nombre del Projecto" :autofocus="true" v-model="project_name"/>
        </MDBModalBody>
        <MDBModalFooter>
          <button @click="modal.value=false" class="btn btn-danger">Cancel</button>
          <button @click="save_new_project" class="btn btn-primary">Aceptar</button>
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
import {useProjectStore} from "@/stores/projects"
import {
  MDBModal,
  MDBModalHeader,
  MDBModalTitle,
  MDBModalBody,
  MDBModalFooter
} from "mdb-vue-ui-kit";

const modal = ref();
const project_name = ref("");
const project_store = useProjectStore();


const new_project = () => {
  project_name.value = "";
  modal.value = true;
}

const save_new_project = () =>{
  const name = project_name.value;
  const date_aux = new Date();
  const date = date_aux.toLocaleDateString() + " " + date_aux.toLocaleTimeString();
  const state = "-";
  const author = user_login;
  project_store.max++;
  project_store.list.push({"id": project_store.max, "name":name, "date":date, "state":state, "author": author});
  modal.value = false;
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
  return project_store.list.filter((item) => {
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

</style>
