<template>
    <if-statement class="statement modal-dialog-if" v-for="(statement, index) in statementStore.list_statements" :key="index" :index="index">
    </if-statement>
</template>

<script setup lang="ts">
import { ref } from "vue";
    import IfStatement from '@/components/IfStatement.vue';
    import { useStatementStore } from '@/stores/stataments.js';

    const statementStore = useStatementStore();

    const description = ref("Se borra el contenido del elemento web <b>{0}</b> usando el selector <b>{1}</b>.");

    const send_arguments = () => {
        return  {
            "command":"clear",
            "arguments":{
                // "selector_type": selector_type,
                // "path_element":path_element,
                // "wait_timeout": wait_timeout
            },
          "flow_id":"",
          "variable_data":""
        }
    };

    // const replace_description = (value: string, index: string): string => {
    //     if (value !== "")
    //         description.value = description.value.replace("{"+index+"}", value);
    //     return description.value;
    // };

    defineExpose({
        send_arguments
    });

</script>

<style>
    .statement{
        display: flex;
        justify-content: flex-end;
    }

    i > b {
        color: blue;
    }

    .modal-dialog-if {
        max-width: 60rem !important;
        padding: 0.875rem 2.875rem 0 0.875rem !important;
    }

</style>