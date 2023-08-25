<template>
    <div class="row g-2 mb-4">
        <div class="col-5">
            <e-label>Tipo de selector:</e-label>
            <select v-model="selector_type" class="form-select">
                <option class="text-grey-20" v-for="selector in list_selectors" :key="selector" :value="selector.toLowerCase()">{{ selector }}</option>
            </select>
        </div>
        <div>
            <input class="form-control" v-model="path_element" placeholder="Ej. //*[@id='element']">
        </div>
    </div>

    <div class="mb-4">
        <label>Texto a enviar:</label>
        <input class="form-control" placeholder="Ingrese aqui el texto" v-model="text_to_send">
    </div>

  <div class="mb-4" >
    <input class="form-check-input" type="checkbox" v-model="enter_key"/>
    <label class="me-4">Presionar enter luego de escribir el texto</label>
  </div>

    <div class="mb-4">
        <label>Tiempo de espera (en segundos):</label>
        <input v-model="wait_timeout">
    </div>
</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_selectors from "@/static/selectors"
    import {replace_description} from "@/utils/formatters";

    const selector_type = ref("xpath");
    const path_element = ref("");
    const text_to_send = ref("");
    const wait_timeout = ref(10);
    const description = ref("Se popula el elemento web <b>{0}</b> usando el selector <b>{1}</b> con el texto <b>{2}</b>.");
    let enter_key = ref(false);

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            selector_type.value = props.step?.data?.arguments?.selector_type;
            path_element.value = props.step?.data?.arguments?.path_element;
            text_to_send.value = props.step?.data?.arguments?.text_to_send;
            wait_timeout.value = props.step?.data?.arguments?.wait_timeout;
            enter_key.value = props.step?.data?.arguments?.enter_key;
        }
    })

    const send_description = () => {
        description.value = replace_description(description.value, path_element.value, "0");
        description.value = replace_description(description.value, selector_type.value, "1");
        description.value = replace_description(description.value, text_to_send.value, "2");
        return description.value;
    };

    const send_arguments = () => {
        return  {"command":"send_keys",
                "arguments":{
                    "selector_type":selector_type.value,
                    "path_element":path_element.value,
                    "text_to_send":text_to_send.value,
                    "wait_timeout":wait_timeout.value,
                    "enter_key":enter_key.value
                },
            "flow_id":"",
            "variable_data":""
        }
    };

    defineExpose({
        send_description,
        send_arguments
    });
 </script>

<style scoped>
    i > b {
        color: blue;
    }
</style>