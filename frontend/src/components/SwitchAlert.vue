<template>
    <div class="mb-4">
        <label>Elegir el botón a cliquear:</label>
        <select v-model="button_type" class="form-select">
            <option class="text-grey-20" v-for="button in list_buttons" :key="button.key" :value="button.key">{{ button.value }}</option>
        </select>
    </div>
</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_buttons from "@/static/alert_buttons";
    import {replace_description} from "@/utils/formatters";
    
    const button_type = ref("alert_accept");
    const description = ref("Se cierra ventana de diálogo presionando el botón <b>{0}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            button_type.value = props.step?.data?.arguments?.button_type;
        }
    })

    const get_value_from_list_buttons  = (ele: string) => {
        return list_buttons.find(it => it.key === ele)?.value;
    }

    const send_description = () => {
        description.value = replace_description(description.value, get_value_from_list_buttons(button_type.value).toLowerCase(), "0");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":button_type.value,
            "arguments":{
                "button_type":button_type.value},
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