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
        <button class="btn btn-primary" style="margin:10px 0 35px" @click="new_flux">Nuevo flujo
        </button>
      </navbar>
      <div>
        <input v-model="filtroTabla" placeholder="Filtrar por nombre"/>
        <tabla-bootstrap :items="filtrarElementos"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import router from "@/router";
import {onMounted, ref, computed} from "vue";
import axios from "axios";
import {useStepStore} from "@/stores/steps";
import TablaBootstrap from "@/components/Table.vue";

const new_flux = () => {
  router.push("new_flux")
}

const step_store = useStepStore();



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

const datos = ref([
  {id: 1, nombre: "Elemento 1", fecha: "02/02/2023", estado: "Ejecutando", autor: "Lean P"},
  {id: 2, nombre: "Elemento 2", fecha: "03/02/2023", estado: "Terminado", autor: "Andy K"},
  // Agrega más datos según sea necesario
]);

const filtroTabla = ref("");
const selectedItemId = ref(null);

const filtrarElementos = computed(() => {
  const filtro = filtroTabla.value.toLowerCase();
  return datos.value.filter((item) => {
    return (
        item.id.toString().includes(filtro) ||
        item.nombre.toLowerCase().includes(filtro) ||
        item.fecha.toLowerCase().includes(filtro) ||
        item.estado.toLowerCase().includes(filtro) ||
        item.autor.toLowerCase().includes(filtro)
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
