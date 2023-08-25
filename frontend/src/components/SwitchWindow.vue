<template>
    <div class="mb-4">
        <label>Nombre de la ventana:</label>
        <input class="form-control" v-model="window_name" placeholder="Ej. afip">
    </div>
</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import {replace_description} from "@/utils/formatters";

    const window_name = ref("");
    const description = ref("Se cambia a la ventana cuyo título es <b>{0}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            window_name.value = props.step?.data?.arguments?.window_name;
        }
    })

    const send_description = () => {
        description.value = replace_description(description.value, window_name.value, "0");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":"switch_window",
            "arguments":{
                "window_name":window_name.value
            },
            "flow_id":null
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