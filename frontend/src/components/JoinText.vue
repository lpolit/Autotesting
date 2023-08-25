<template>
        <div class="mb-4">
            <label>Texto a unir:</label>
            <input v-model="text" class="form-control" placeholder="Ej: esto, es, para, unir">
        </div>

        <div class="mb-4">
            <label>Delimitador:</label>
            <input v-model="delimiter" class="form-control" placeholder="Ej: coma, punto, espacio en blanco">
        </div>

        <div class="mb-4">
            <label class="me-4">Variable producida:</label>
            <input class="form-control" v-model="joined_text">
        </div>
</template>

<script setup lang="ts">
import {onMounted, ref} from "vue";
import {replace_description} from "@/utils/formatters";

const text = ref();
const delimiter = ref();
const joined_text = ref("{texto_unido}")
const description = ref("Se une el texto usando el delimitador <b>{0}</b> y guarda el valor en la variable <b>{1}</b>.");

const props = defineProps({
    step: Object
})

onMounted(() => {
    if (props.step.data) {
        text.value = props.step?.data?.arguments?.text;
        delimiter.value = props.step?.data?.arguments?.delimiter;
        joined_text.value = props.step?.data?.arguments?.var_name;
    }
})

const send_description = () => {
    description.value = replace_description(description.value, delimiter.value, "0");
    description.value = replace_description(description.value, joined_text.value, "1");
    return description.value;
};

const send_arguments = () => {
    return {
        "command": "text_join",
        "arguments": {
            "text": text.value,
            "delimiter": delimiter.value,
            "var_name": joined_text.value,
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