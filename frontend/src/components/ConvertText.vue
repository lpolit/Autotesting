<template>
    <div class="mb-4">
        <label>Texto a convertir:</label>
        <input class="form-control" v-model="text">
    </div>

    <div class="mb-4">
        <label>Convertir a:</label>
        <select v-model="convertion_type" class="form-select">
            <option class="text-grey-20" v-for="convert in list_convertions" :key="convert.key" :value="convert.key">{{ convert.value }}</option>
        </select>
    </div>

    <div class="mb-4">
        <label class="me-4">Variable producida:</label>
        <input class="form-control" v-model="converted_text">
    </div>

</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_convertions from "@/static/convertions";
    import {replace_description} from "@/utils/formatters";

    const text = ref();
    const convertion_type = ref();
    const converted_text = ref("{texto_convertido}")
    const description = ref("Convierte el texto  a <b>{0}</b> y guarda el valor en la variable <b>{1}</b>.");

    const props = defineProps({
        step: Object
    })


    onMounted (() => {
        if (props.step.data) {
            text.value = props.step?.data?.arguments?.text;
            convertion_type.value = props.step?.data?.arguments?.convertion_type;
            converted_text.value = props.step?.data?.arguments?.var_name;
        }
    })

    const get_value_from_list_convertions = (ele: string) => {
        return list_convertions.find(it => it.key === ele)?.value;
    }

    const send_description = () => {
        description.value = replace_description(description.value, get_value_from_list_convertions(convertion_type.value).toLowerCase(), "0");
        description.value = replace_description(description.value, converted_text.value, "1");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":convertion_type.value,
            "arguments":{
                "text":text.value,
                "convertion_type":convertion_type.value,
                "var_name": converted_text.value,

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