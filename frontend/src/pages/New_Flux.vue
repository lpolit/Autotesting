<template>
  <header class="navbar navbar-expand-md navbar-light bg-light">
    <a class="navbar-brand" href="#">
      <img src="logo.png" alt="Autotesting">
    </a>
    {{user_login}}
    <button class="btn btn-primary" @click="log_out">LOG OUT</button>
    <div  class="navbar-collapse collapse navbar-align " >
      <img width="50" src="avatar.png" alt="Autotesting">
    </div>
  </header>

  <div  class=" navbar-align" >
    <a title="Ejecutar flujo" >
      <button class="btn btn-primary" @click="ejecutar_flujo">
        <svg width="16" height="16" fill="currentColor"
             class="bi bi-play-fill" viewBox="0 0 16 16">
          <path
              d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"/>
        </svg>
      </button>

    </a>

    <a title="Detener flujo">
      <button class="btn btn-primary" @click="detener_flujo">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
             class="bi bi-stop-fill" viewBox="0 0 16 16">
          <path
              d="M5 3.5h6A1.5 1.5 0 0 1 12.5 5v6a1.5 1.5 0 0 1-1.5 1.5H5A1.5 1.5 0 0 1 3.5 11V5A1.5 1.5 0 0 1 5 3.5z"/>
        </svg>
      </button>
    </a>

    <a title="Guardar flujo">
      <button class="btn btn-primary"  @click="guardar_flujo">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
             class="bi bi-save-fill" viewBox="0 0 16 16">
          <path
              d="M8.5 1.5A1.5 1.5 0 0 1 10 0h4a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h6c-.314.418-.5.937-.5 1.5v7.793L4.854 6.646a.5.5 0 1 0-.708.708l3.5 3.5a.5.5 0 0 0 .708 0l3.5-3.5a.5.5 0 0 0-.708-.708L8.5 9.293V1.5z"/>
        </svg>
      </button>
    </a>
  </div>




  <main class="main">

    <MDBAccordion
        style="width: 20%"
    >
      <MDBAccordionItem
          v-for="action in list_actions"
          :key="action.name"
          :title=action.name
          :headerTitle="action.name"
          :collapseId="action.name"
      >
        <div class="action"
             v-for="act in action.value"
             :key="act.id"
             :id="act.id"
             draggable="true"
             @dragstart="start_drag($event, act.id)"
        >{{ act.name }}

        </div>

      </MDBAccordionItem>
    </MDBAccordion>
    <!--            PANEL-->

    <MDBCard class="fst-italic mb-0 mt-3 d-flex justify-content-center"
             @drop="on_drop($event)"
             @dragover="pos($event)"
             @dragenter.prevent
             @dragleave="clean($event)"
    >
      <MDBCardBody
      >
        <MDBCardText
            v-if=erase_epanel_text>
          Arrastrá acá tus pasos
        </MDBCardText>
        <div class="panel-header" id="panel-top"></div>
        <VueDraggableNext
            v-model="step_store.list_steps.steps"
            handle=".card-header"
            ghost-class="ghost"
            :sort="true"
        >
          <transition-group>
            <div class="card-image" v-for="(st, index) in step_store.list_steps.steps" :key="st.id">
              <div class="icon-position mx-4">
                <Icon v-if="st.status === 'OK'" icon="check_circle"/>
                <Icon v-if="st.status === 'ERROR'" icon="error"/>
                <Icon v-if="st.status === 'WARNING'" icon="warning"/>
                <Icon v-if="st.status === ''" icon="pending"/>
              </div>
              <MDBCard text="center"
                       :id="'card-'+st.orden"
                       :border="set_status(st.status)"
                       :class="['border-0','border-start']"
                       :header-html='"<b>"+ st.name +"</b>"'
                       @dblclick="show_modal(st.orden)"
                       style="border-left-width: 0.5rem !important">
                <MDBCardHeader :id="'card-'+st.orden+'-header'" >
                  {{ st.name }}
                </MDBCardHeader>
                <MDBCardBody class="cb" :id="'card-'+st.orden+'-body'">
                  <MDBCardText class="description" v-html="st.description">
                  </MDBCardText>

                  <a href="#" title="Eliminar paso">
                    <button class="btn btn-primary btn-align bin" @click="delete_card(index)">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                           fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                        <path
                            d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                      </svg>
                    </button>
                  </a>
                </MDBCardBody>
              </MDBCard>

            </div>
          </transition-group>
        </VueDraggableNext>
        <div class="panel-footer" id="panel-bottom"></div>
      </MDBCardBody>
    </MDBCard>


    <MDBModal
        id="modal"
        tabindex="-1"
        v-model="modal"
    >
      <MDBModalHeader>
        <MDBModalTitle> {{ step.name }}</MDBModalTitle>
      </MDBModalHeader>
      <MDBModalBody>
        <component ref="hijo" :is="component_modal" :step="step"></component>
      </MDBModalBody>
      <MDBModalFooter>
        <button @click="clear_step" class="btn btn-danger">Cancel</button>
        <button @click="set_step_data" class="btn btn-primary">Aceptar</button>
      </MDBModalFooter>
    </MDBModal>

  </main>


</template>


<script setup lang="ts">


import OpenBrowser from '@/components/OpenBrowser.vue';
import SendKeys from '@/components/SendKeys.vue';
import Click from '@/components/Click.vue';
import AssertEquals from '@/components/AssertEquals.vue';
import AssertWebElementIs from '@/components/AssertWebElementIs.vue';
import Clear from '@/components/Clear.vue';
import Wait from '@/components/Wait.vue';
import CloseBrowser from '@/components/CloseBrowser.vue';
import GetText from '@/components/GetText.vue';
import GetWebElement from '@/components/GetWebElement.vue';
import SwitchIFrame from '@/components/SwitchIFrame.vue';
import SwitchWindow from '@/components/SwitchWindow.vue';
import SwitchAlert from '@/components/SwitchAlert.vue';
import Screenshot from '@/components/Screenshot.vue';
import SplitText from '@/components/SplitText.vue';
import JoinText from '@/components/JoinText.vue';
import ConvertText from '@/components/ConvertText.vue';
import ReplaceText from '@/components/ReplaceText.vue';
import SubText from '@/components/SubText.vue';
import SetVariable from '@/components/SetVariable.vue';
import CloseWindow from '@/components/CloseWindow.vue';
import If from '@/components/If.vue';


import {
  MDBAccordion,
  MDBAccordionItem,
  MDBCard,
  MDBCardHeader,
  MDBCardBody,
  MDBCardText,
  MDBModal,
  MDBModalHeader,
  MDBModalTitle,
  MDBModalBody,
  MDBModalFooter
} from "mdb-vue-ui-kit";
import list_actions from "../../actions.json";
import {ref, computed, nextTick, onMounted} from "vue";
import {VueDraggableNext} from 'vue-draggable-next';
import axios from "axios";

import {useStepStore} from "@/stores/steps";
import Icon from "@/components/Icon.vue";
import router from "@/router";


const step_store = useStepStore();

const modal = ref(false);
// const exampleModal = ref(false);
const excluded_steps = [7, 21];
let step = ref("");
let orden_step = ref(0);
let hijo = ref();
let flow_id = 0;
let card_pos = 0;
let show_sidebar = ref(false);
let type_sidebar = ref();

const list_components = [
  {"id": 1, "value": OpenBrowser},
  {"id": 2, "value": Click},
  {"id": 3, "value": SendKeys},
  {"id": 4, "value": GetText},
  {"id": 5, "value": GetWebElement},
  {"id": 6, "value": Wait},
  {"id": 7, "value": CloseBrowser},
  {"id": 8, "value": Clear},
  {"id": 9, "value": SwitchWindow},
  {"id": 10, "value": SwitchIFrame},
  {"id": 11, "value": SwitchAlert},
  {"id": 12, "value": Screenshot},
  {"id": 13, "value": AssertEquals},
  {"id": 14, "value": AssertWebElementIs},
  {"id": 15, "value": SplitText},
  {"id": 16, "value": JoinText},
  {"id": 17, "value": ReplaceText},
  {"id": 18, "value": SubText},
  {"id": 19, "value": ConvertText},
  {"id": 20, "value": SetVariable},
  {"id": 21, "value": CloseWindow},
  {"id": 22, "value": If}
];

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

const erase_epanel_text = computed(() => {
  return step_store.list_steps.steps.length === 0;
});

let component_modal = computed(() => {
  return list_components.find(it =>
      it.id === step.value.id)?.value;
});


const start_drag = (evt: any, id: number) => {
  evt.dataTransfer.dropEffect = 'move';
  evt.dataTransfer.effectAllowed = 'move';
  evt.dataTransfer.setData('stepID', id);
  clear_step();
}

const on_drop = (evt: any) => {
  clear_step();
  const stepID = evt.dataTransfer.getData('stepID');
  if (stepID == "") return;
  clean(evt);
  step.value = get_item(parseInt(stepID));
  step.value.orden = orden_step.value++;
  if (step.value !== undefined) {
    step_store.list_steps.steps.splice(card_pos, 0, step.value);
    check_modal_visibility();
  }

}

const check_modal_visibility = () => {
  if (excluded_steps.includes(step.value.id))
    nextTick(() => {
      set_step_data();
    });
  else
    show_modal(step.value.orden);
}

const set_step_data = () => {

  set_arguments();
  set_card_description();
  add_var_to_list();
  clear_step();
}

const add_var_to_list = () => {
  let new_key = step.value.data.arguments.var_name;
  if (new_key === undefined)
    return false
  if (step_store.list_vars.find(it => it.key === new_key) === undefined)
    step_store.list_vars.push({"key": new_key, "value": "", "index": "", "type": ""});
}

const set_card_description = () => {
  step.value.description = hijo.value.send_description();
}

const set_arguments = () => {
  step.value.data = hijo.value.send_arguments();
}

const show_modal = (step_orden: number) => {
  step.value = step_store.list_steps.steps.filter(it =>
      it.orden === step_orden)[0];
  modal.value = true;
}

const get_item = (id: number) => {
  let item = null;
  list_actions.find(action_type =>
      item = action_type.value.find(action => action.id === id))
  return JSON.parse(JSON.stringify(item));
};

const set_status = (step_status: string): string => {
  if (step_status === "OK")
    return "success";
  else if (step_status === "ERROR")
    return "danger";
  else if (step_status === "WARNING")
    return "secondary"
  else
    return "";

};

const update_var = (var_key, new_value, index, type) => {
  let item = step_store.list_vars.find(it =>
      it.key === var_key);
  if (item !== undefined) {
    item.value = new_value;
    item.index = index;
    item.type = type;
  }
}

const ejecutar_flujo = async () => {
  console.log(step_store.list_steps)
  const path = '/api/flow'
  let json

  for (let st of step_store.list_steps.steps) {
    st.data.flow_id = flow_id
    json = JSON.parse(JSON.stringify(st.data))
    await axios.post(path, json).then((response) => {
      flow_id = response.data.flow_id
      st.status = "OK"
      st.data.flow_id = flow_id
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
    })
  }
}

const detener_flujo = () => {
  const path = '/api/flow'
  const json = {
    "command": "close_browser",
    "flow_id": flow_id,
    "arguments": {}
  };

  axios.post(path, json).then((response) => {
    console.log(response.data)
    flow_id = 0
  }).catch((error) => {
    console.log(error)
  })
}

const guardar_flujo = () => {
  const path = '/api/flow/save'
  const json = {
    "name": "prueba1",
    "flux": sessionStorage.getItem("steps")
  };

  axios.post(path, json).then((response) => {
    console.log(response.data)
    alert("guardado exitoso")
  }).catch((error) => {
    console.log(error)
  })
}


const log_out = () => {
  step_store.$reset()
  //sessionStorage.clear()
  router.push("/")
}

const delete_card = (index: number) => {
  step_store.list_steps.steps.splice(index, 1);
  let step_var = step_store.list_vars.find(it => it.index == index)
  if (step_var)
    step_store.list_vars.splice(index, 1);

  clear_step();
}

const pos = (evt: any) => {
  evt.preventDefault();
  let ele = evt.target;
  let index = parseInt(ele.id.split("-")[1]);

  if (ele.id.includes("header")) {
    ele.style.borderTop = "thick solid #706E6EFF"
    card_pos = step_store.list_steps.steps.findIndex(it => it.orden == index)
  } else if (ele.id.includes("body")) {
    ele.style.borderBottom = "thick solid #706E6EFF"
    card_pos = step_store.list_steps.steps.findIndex(it => it.orden == index) + 1;
  } else if (ele.id.includes("top")) {
    ele.style.borderBottom = "thick solid #706E6EFF"
    card_pos = 0;
  } else if (ele.id.includes("bottom")) {
    ele.style.borderTop = "thick solid #706E6EFF"
    card_pos = step_store.list_steps.steps.length + 1;
  }

}

const clean = (evt: any) => {
  evt.preventDefault();
  let ele = evt.target;
  if (ele.id.includes("header") || ele.id.includes("body") || ele.id.includes("top") || ele.id.includes("bottom")) {
    ele.style.borderWidth = "0"
  }
}

const clear_step = () => {
  step.value = "";
  modal.value=false;
}

const toogle_sidebar = (type: string) => {
  show_sidebar.value = !show_sidebar.value;
  type_sidebar.value = type;
}

</script>

<style>

body {
  height: 800px;
}

.flex-container {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}

.btn {
  margin-right: 10px;
}

.btn-content {
  display: flex;
  justify-content: space-between;
  word-break: break-word;
}

.btn-align {
  align-self: center;
}

.btn > [class*="material-icons"] {
  margin-right: 0 !important;
}

.e-footer-content {
  padding-bottom: 30px !important;
}

.card-header{
  color: whitesmoke;
  cursor: pointer;
}
.card-header-ok {
  background-color: green !important;
}

.card-header-error {
  background-color: darkred !important;
}

.panel-footer, .panel-header {
  height: 2.5rem;
}

.container {
  margin-left: 1rem !important;
  margin-right: 1rem !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
}

.e-accordion-tooltip {
  width: 100% !important;
}

.aux-button {
  margin-left: 2rem;
}

.card {
  width: 756px;
  margin-left: 10%;
}

.card-text {
  padding-top: 1%;
  padding-left: 1%;
}

.card-image {
  display: flex;
}

.icon-position {
  display: flex;
  align-items: center;
}

.action {
  height: 40px;
  padding: 5px 5px;
  cursor: pointer;
}

.action:hover {
  background-color: #F0F4FF;
}

.main {
  display: flex;
}

.bin {
  margin-right: 10px;
  justify-content: end;
}
.cb{
  display: flex;
  justify-content: space-between;
}
.navbar-brand img {
  width: 150px;
}

.navbar-align{
  justify-content: end;
  align-self: end;
}

</style>