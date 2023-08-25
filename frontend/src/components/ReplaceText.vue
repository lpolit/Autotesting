<template>
    <div class="mb-4">
        <label>Texto a analizar:</label>
        <input class="form-control" v-model="text_origin">
    </div>

    <div class="mb-4">
        <label>Texto a buscar:</label>
        <input class="form-control" v-model="text_target">
    </div>

    <div class="mb-4">
        <label>Reemplazar con:</label>
        <input class="form-control" v-model="replace_with">
    </div>

    <div class="mb-4">
        <e-label>Ocurrencias:</e-label>
        <select v-model="occurrency_type" class="form-select">
            <option class="text-grey-20" v-for="occur in list_occurrencies" :key="occur" :value="occur">{{ occur }}</option>
        </select>
    </div>

    <div class="mb-4" v-if="occurrency_type=='Las primeras'">
        <label>Cantidad de ocurrencias:</label>
        <input class="form-control" v-model="occurrency_number" placeholder="Ej. frame_modal">
    </div>

    <div class="mb-4" >
        <label class="me-4">Ignorar mayúsculas o minúsculas:</label>
        <input class="form-check-input" type="checkbox" v-model="check_ignore"/>
    </div>

    <div class="mb-4">
        <label class="me-4">Variable producida:</label>
        <input class="form-control" v-model="replaced_text">
    </div>
</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import {replace_description} from "@/utils/formatters";

    const text_origin = ref();
    const text_target = ref();
    const replace_with = ref();
    const occurrency_number = ref(1);
    const occurrency_type = ref("Todas");
    const check_ignore = ref(true);
    const replaced_text = ref("{texto_reemplazado}")
    const description = ref("Reemplaza en el texto ingresado <b>{0}</b> con <b>{1}</b> para {2} ocurrencias y guarda el valor en la variable <b>{3}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            text_origin.value = props.step?.data?.arguments?.text_origin;
            text_target.value = props.step?.data?.arguments?.text_target;
            replace_with.value = props.step?.data?.arguments?.replace_with;
            occurrency_number.value = props.step?.data?.arguments?.occurrency_number;
            occurrency_type.value = props.step?.data?.arguments?.occurrency_type;
            check_ignore.value = props.step?.data?.arguments?.check_ignore;
            replaced_text.value = props.step?.data?.arguments?.var_name;
        }
    })

    const get_identifier_value = () => {
        if (occurrency_type.value == "Todas")
            return "<b>" + occurrency_type.value.toLowerCase() + "</b> las";
        else
            return "<b>" + occurrency_type.value.toLowerCase() + " " + occurrency_number.value + "</b>"
    }

    const list_occurrencies = ["Todas", "Las primeras"]

    const send_description = () => {
        description.value = replace_description(description.value, text_target.value, "0");
        description.value = replace_description(description.value, replace_with.value, "1");
        description.value = replace_description(description.value, get_identifier_value(), "2");
        description.value = replace_description(description.value, replaced_text.value, "3");


        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":"replace",
            "arguments":{
                "text_origin":text_origin.value,
                "text_target":text_target.value,
                "replace_with":replace_with.value,
                "occurrency_type":occurrency_type.value,
                "occurrency_number":occurrency_number.value,
                "check_ignore":check_ignore.value,
                "var_name":replaced_text.value,
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