<template>
  <input type="button" value="INGRESAR" @click="new_flux"/>
  el usuario es ... {{user_login}}
  <input type="button" value="CARGAR FLUJO PRUEBA1" @click="abrir"/>

  <div class="page-container">
    <div class="page-content">
      <navbar class="flex-container">
        <button class="btn" action="secondary" @click="newflux">
          <icon icon="add"/>
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

</style>
