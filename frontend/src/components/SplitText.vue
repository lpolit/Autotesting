<template>
    <div class="mb-4">
        <label>Texto a separar:</label>
        <input class="form-control" v-model="text">
    </div>

    <div class="mb-4">
        <label>Delimitador:</label>
        <input class="form-control" v-model="delimiter"  placeholder="Ej: coma, punto, espacio en blanco">
    </div>

    <div class="mb-4">
        <label>Indice buscado:</label>
        <input class="form-control" v-model="index">
    </div>

    <div class="mb-4">
        <label class="me-4">Variable producida:</label>
        <input class="form-control" v-model="splitted_text">
    </div>

</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import {replace_description} from "@/utils/formatters";

    const text = ref();
    const delimiter = ref();
    const index = ref();
    const splitted_text = ref("{texto_separado}")
    const description = ref("Se separa el texto usando el delimitador <b>{0}</b> y guarda el valor en la variable <b>{1}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            text.value = props.step?.data?.arguments?.text;
            delimiter.value = props.step?.data?.arguments?.delimiter;
            index.value = props.step?.data?.arguments?.index;
            splitted_text.value = props.step?.data?.arguments?.var_name;
        }
    })

    const send_description = () => {
        description.value = replace_description(description.value, delimiter.value, "0");
        description.value = replace_description(description.value,splitted_text.value, "1");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":"text_split",
            "arguments":{
                "text":text.value,
                "delimiter":delimiter.value,
                "index":index.value,
                "var_name":splitted_text.value,
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