<template>
    <div></div>
</template>

<script setup lang="ts">
    import { ref } from "vue";

    const description = ref("Cierra la instancia del navegador en ejecución.");

    const send_description = () => {
        return description.value;
    };

    const send_arguments = () => {
        return  {"command":"close_browser",
                 "arguments":{},
                  "flow_id":"",
                  "variable_data":""
                }
    };

    defineExpose({
        send_description,
        send_arguments
    });

</script>
