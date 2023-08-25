<template>
    <div class="mb-4">
        <label>Tipo de navegador:</label>
        <select id="browser_type" v-model="browser_type" class="form-select">
            <option class="text-grey-20" v-for="browser in list_browsers" :key="browser" :value="browser">{{ browser }}</option>
        </select>
    </div>

    <div class="mb-4">
        <label>Url inicial:</label>
        <input class="form-control" id="url" placeholder="Ej: https://www.afip.gob.ar" v-model="url">
    </div>

    <div class="mb-4">
        <label>Estado de ventana:</label>
        <select class="form-select" v-model="window_state_type">
            <option hidden class="text-grey-80">Seleccione un criterio</option>
            <option class="text-grey-20" v-for="win in list_window_state" :key="win" :value="win"> {{ win }}</option>
        </select>
    </div>

    <div class="mb-4">
        <label>Tiempo de espera (en segundos):</label>
        <input class="form-control" v-model="wait_timeout">
    </div>

    <div class="mb-4" >
        <input class="form-check-input" type="checkbox" v-model="headless"/>
        <label class="me-4">Headless</label>
    </div>

</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_browsers from "@/static/browsers";
    import list_window_state from "@/static/window_states";
    import {capitalize, replace_description} from "@/utils/formatters";

    const browser_type = ref("Chrome");
    const url = ref("");
    const window_state_type = ref("Normal");
    let headless = ref(false);
    let wait_timeout = ref(10);
    const description = ref("Instancia una ventana de <b>{0}</b>, navega a <b>{1}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            browser_type.value = capitalize(props.step?.data?.arguments?.browser);
            url.value = props.step?.data?.arguments?.url;
            window_state_type.value = capitalize(props.step?.data?.arguments?.window_state);
            headless.value = props.step?.data?.arguments?.headless;
            wait_timeout.value = props.step?.data?.arguments?.wait_timeout;
        }
    })

    const send_description = () => {
        description.value = replace_description(description.value, browser_type.value, "0");
        description.value = replace_description(description.value, url.value, "1");
        return description.value;
    };

    const send_arguments = () => {
        return  {"command":"open_browser",
                 "arguments":{
                     "browser":browser_type.value.toLowerCase(),
                     "url":url.value,
                     "window_state":window_state_type.value.toLowerCase(),
                     "wait_timeout":wait_timeout.value,
                     "headless":headless.value,
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

<style>
.description > b {
    color: #0D658BFF;
}
</style>