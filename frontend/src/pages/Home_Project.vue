<template>
  <header class="navbar navbar-expand-md navbar-light bg-light" style="border-bottom: 4px solid rgb(1 58 122); margin-bottom: 15px;height: 80px;">
    <a class="navbar-brand" href="#">
      <img src="logo.png" alt="Autotesting">
    </a>

    <div  class="navbar-collapse collapse navbar-align " >
      {{user_login}}
      <div class="dropdown">
        <img width="35" style="margin:0 15px 0 10px" src="../icons/avatar.png" alt="Autotesting">
        <button class="btn dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">

        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" style="left: -100px">
          <li><a class="dropdown-item" @click="change_passw">Cambiar Contraseña</a></li>
          <li><a class="dropdown-item" @click="log_out">Salir</a></li>
        </ul>
      </div>
    </div>
  </header>

  <div class="page-container">
    <div class="page-content">
      <navbar class="flex-container" >
        <button class="btn btn-primary" style="margin:11px 130px 33px 3px" @click="new_project"><img src="../icons/plus-circle.svg" style="width: 20px; margin-right: 10px; filter: invert(1);"/>Nuevo Proyecto
        </button>
      </navbar>
      <div>
        <input v-model="filtroTabla" placeholder="Filtrar por nombre"/>
        <tablita @onEdit="edit_project" @onDelete="delete_project" :items="filtrarElementos"  :store="project_store" />
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
          <input style="width: 100%" placeholder="Ingrese el nombre del Projecto" :autofocus="true" v-model="project_name"/>
        </MDBModalBody>
        <MDBModalFooter>
          <button @click="set_modal(false)" class="btn btn-danger">Cancel</button>
          <button @click="save_project" class="btn btn-primary">Aceptar</button>
        </MDBModalFooter>
      </MDBModal>

      <MDBModal
          id="modal_delete"
          tabindex="-1"
          v-model="modal_delete"
      >
        <MDBModalHeader>
          <MDBModalTitle> Eliminar Proyecto </MDBModalTitle>
        </MDBModalHeader>
        <MDBModalBody>
          <label>Puede que el proyecto tenga flujos asociados. ¿Esta seguro que desea eliminar el proyecto?</label>
        </MDBModalBody>
        <MDBModalFooter>
          <button @click="set_modal_delete(false)" class="btn btn-danger">Cancel</button>
          <button @click="delete_project_db" class="btn btn-primary">Aceptar</button>
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
import { notify } from "@kyvg/vue3-notification";
import {useStepStore} from "@/stores/steps";


const modal = ref();
const modal_delete = ref();
const project_name = ref("");
const project_id = ref (0);
const project_store = useProjectStore();
const step_store = useStepStore();
const list_projects = ref([])
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
  load_table();

})

const notificar = (type: string, title: string, text: string) =>{
  notify({
    type: type,
    title: title,
    text: text,
  });
}

const new_project = () => {
  project_name.value = "";
  project_id.value=0
  set_modal(true);
}

const save_project = () => {
  const date_aux = new Date();
  const date = date_aux.toLocaleDateString() + " " + date_aux.toLocaleTimeString();
  const state = "-";

  set_modal(false);
  let path = '/api/project/insert';

  if (project_id.value!=0) {
    path = '/api/project/update/'+project_id.value;
  }
  const json = {
      "project_name": project_name.value,
      "date": date,
      "state": state,
      "user": user_login.value
    };

    axios.post(path, json).then((response) => {
      console.log(response.data)
      load_table()
      notificar("success", "Operacion exitosa", "La operacion sobre el proyecto "+response.data+" se realizo con exito")
    }).catch((error) => {
      console.log(error)
      notificar("error", "Fallo", "Fallo al insertar o modificar el Proyecto!")
    })

}

const load_table = () =>{
  list_projects.value = []
  axios.post('/api/project/getAll/'+ user_login.value).then((response) => {
    let list_aux = response.data;
    for (let proj of list_aux) {
      list_projects.value.push({
        "id": proj[0],
        "name": proj[1],
        "date": proj[2],
        "author": proj[4],
      });
    }
  }).catch((error) => {
    console.log(error)
  })
}


const filtroTabla = ref("");

const filtrarElementos = computed(() => {
  const filtro = filtroTabla.value.toLowerCase();
  return list_projects.value.filter((item) => {
    return (
        item.id?.toString().includes(filtro) ||
        item.name?.toLowerCase().includes(filtro) ||
        item.date?.toLowerCase().includes(filtro) ||
        item.author?.toLowerCase().includes(filtro)
    );
  });
});

const edit_project = (state: any, id: any, pjt_name: any) => {
  project_name.value = pjt_name;
  project_id.value = id;
  set_modal(state)
}
const set_modal = (valor: boolean) =>{
  modal.value = valor;
}

const set_modal_delete = (valor: boolean) =>{
  modal_delete.value = valor;
}

const delete_project = (id: any,) => {
  project_id.value = id;
  set_modal_delete(true);
}
const delete_project_db = () => {
  const path = '/api/project/delete/' + project_id.value;

  axios.delete(path).then((response) => {
    console.log(response.data)
    load_table()
    notificar("success", "Operacion exitosa", "La eliminacion del proyecto "+response.data+" se realizo con exito")
  }).catch((error) => {
    console.log(error)
    notificar("error", "Fallo", "Fallo al Eliminar el Proyecto!")
  })
  set_modal_delete(false)
}

const log_out = () => {
  step_store.$reset()
  sessionStorage.clear()
  router.push("/")
}

const change_passw = () =>{
  router.push("change")
}

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
