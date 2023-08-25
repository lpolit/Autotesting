<template>
    <div class="row g-2 mb-4">
        <div class="col-5">
            <label>Tipo de selector:</label>
            <select v-model="selector_type" class="form-select">
                <option class="text-grey-20" v-for="selector in list_selectors" :key="selector" :value="selector.toLowerCase()">{{ selector }}</option>
            </select>
        </div>
        <div>
            <input class="form-control" v-model="path_element" placeholder="Ej. //*[@id='element']">
        </div>
    </div>

    <div class="mb-4">
        <label>Tiempo de espera (en segundos):</label>
        <input class="form-control" v-model="wait_timeout">
    </div>

    <div class="mb-4">
        <label class="me-4">Variable producida</label>
        <input class="form-control" v-model="web_element">
    </div>

</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_selectors from "@/static/selectors";
    import {replace_description} from "@/utils/formatters";

    const selector_type = ref("xpath");
    const path_element = ref("");
    const wait_timeout = ref(10);
    const web_element = ref("{web_element}")
    const description = ref("Se obtiene el elemento web <b>{0}</b> usando el selector <b>{1}</b> y lo guarda en la variable <b>{2}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            selector_type.value = props.step?.data?.arguments?.selector_type;
            path_element.value = props.step?.data?.arguments?.path_element;
            wait_timeout.value = props.step?.data?.arguments?.wait_timeout;
            web_element.value = props.step?.data?.arguments?.var_name;
        }
    })

    const send_description = () => {
        description.value = replace_description(description.value, path_element.value, "0");
        description.value = replace_description(description.value, selector_type.value, "1");
        description.value = replace_description(description.value, web_element.value, "2");
        return description.value;
    };

    const send_arguments = () => {
        return {
            "command": "get_web_element",
            "arguments": {
                "selector_type": selector_type.value,
                "path_element": path_element.value,
                "wait_timeout": wait_timeout.value,
                "var_name": web_element.value
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