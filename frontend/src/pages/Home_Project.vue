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
const list_projects = ref([])


const new_project = () => {
  project_name.value = "";
  modal.value = true;
}

const save_new_project = () => {

  const date_aux = new Date();
  const date = date_aux.toLocaleDateString() + " " + date_aux.toLocaleTimeString();
  const state = "-";
  const author = user_login;

  modal.value = false;

  const path = '/api/project/insert'
  const json = {
    "project_name": project_name.value,
    "date": date,
    "state": state,
    "user": user_login.value
  };

  axios.post(path, json).then((response) => {
    console.log(response.data)
    list_projects.value.push({
      "id": response.data,
      "name": project_name.value,
      "date": date,
      "state": state,
      "author": author
    });
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

  //LLEVAR A UNA FUNCION CARGAR TABLA
  axios.post('/api/project/getAll/'+ user_login.value).then((response) => {
    let list_aux = response.data;
    for (let proj of list_aux) {
      list_projects.value.push({
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











})

const filtroTabla = ref("");
const selectedItemId = ref(null);

const filtrarElementos = computed(() => {
  const filtro = filtroTabla.value.toLowerCase();
  return list_projects.value.filter((item) => {
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
