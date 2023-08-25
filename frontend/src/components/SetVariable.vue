<template>
    <div class="mb-4">
        <label>Nombre de la variable:</label>
        <input class="form-control"  v-model="var_name" placeholder="Ej. nombre_variable">
    </div>

    <div class="mb-4">
        <label>Valor:</label>
        <input class="form-control" v-model="var_value" placeholder="Ej. 'ejemplo', 1, {otra_variable}">
    </div>
</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import {replace_description} from "@/utils/formatters";

    const var_name = ref("{variable}");
    const var_value = ref("");
    const description = ref("Asigna a la variable <b>{0}</b> el valor <b>{1}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            var_name.value = props.step?.data?.arguments?.var_name;
            var_value.value = props.step?.data?.arguments?.var_value;
        }
    })

    const send_description = () => {
        description.value = replace_description(description.value, var_name.value, "0");
        description.value = replace_description(description.value, var_value.value, "1");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":"none",
            "arguments":{
                "var_name": var_name.value,
                "var_value":var_value.value
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