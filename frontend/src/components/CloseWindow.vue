<template>
    <div></div>
</template>

<script setup lang="ts">
    import { ref } from "vue";

    const description = ref("Cierra la ventana o solapa que está en foco.");

    const send_description = () => {
        return description.value;
    };

    const send_arguments = () => {
        return  {"command":"close_window",
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
