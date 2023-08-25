<template>
    <div class="mb-4">
        <label>Texto a analizar:</label>
        <input class="form-control" v-model="text_origin" >
    </div>

    <div class="mb-4">
        <label>Obtener texto:</label>
        <select v-model="option_type" class="form-select" @change="clear_field()">
            <option class="text-grey-20" v-for="option in list_options" :key="option.key" :value="option.key">{{ option.value }}</option>
        </select>
    </div>

    <div class="mb-4" v-if="option_type=='after'|| option_type=='between'">
        <label>Marca de inicio:</label>
        <input class="form-control" v-model="start_index" placeholder="Ej. 1">
    </div>

    <div class="mb-4" v-if="option_type=='before' || option_type=='between'">
        <label>Marca de fin:</label>
        <input  class="form-control" v-model="end_index" placeholder="Ej. 1">
    </div>

    <div class="mb-4">
        <label class="me-4">Variable producida:</label>
        <input class="form-control" v-model="sub_text">
    </div>
</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_options from "@/static/subtext_options";
    import {replace_description} from "@/utils/formatters";

    const text_origin = ref();
    const option_type = ref("after");
    const start_index = ref();
    const end_index = ref();
    const sub_text = ref("{texto_recortado}")
    const description = ref("Obtiene el texto {0} y lo almacena en la variable <b>{1}</b>");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            text_origin.value = props.step?.data?.arguments?.text_origin;
            option_type.value = props.step?.data?.arguments?.option_type;
            start_index.value = props.step?.data?.arguments?.start_index;
            end_index.value = props.step?.data?.arguments?.end_index;
            sub_text.value = props.step?.data?.arguments?.var_name;
        }
    })

    const get_identifier_value = () => {
        const option_value = get_value_from_list_options(option_type.value);

        if (option_type.value == "after")
            return option_value + " " + "<b>" +  start_index.value + "</b>";
        else if(option_type.value == "before")
            return option_value + " " + "<b>" +  end_index.value + "</b>";
        else
            return option_value + " " + "<b>" +  start_index.value + "</b> y <b>" +  end_index.value + "</b>";
    }

    const get_value_from_list_options  = (ele: string) => {
        return list_options.find(it => it.key === ele)?.value;
    };

    const clear_field = () => {
        start_index.value = null;
        end_index.value = null;
    };

    const send_description = () => {
        description.value = replace_description(description.value, get_identifier_value(), "0");
        description.value = replace_description(description.value, sub_text.value, "1");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":"sub_text",
            "arguments":{
                "text_origin":text_origin.value,
                "option_type":option_type.value,
                "start_index":start_index.value,
                "end_index":end_index.value,
                "var_name":sub_text.value,
            },
            "flow_id":"",
            "variable_data":""
        }
    };

    defineExpose({
        send_description,
        send_arguments
    });

    const test = () =>{
        console.log("tot")
    }

 </script>

<style scoped>
    i > b {
        color: blue;
    }
</style>