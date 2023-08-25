<template>
    <div class="mb-4">
        <label>Tipo de identificador:</label>
        <select v-model="identification_type" class="form-select" @change="clear_field()">
            <option class="text-grey-20" v-for="identifier in list_identificators" :key="identifier.key" :value="identifier.key">{{ identifier.value }}</option>
        </select>
    </div>

    <div class="mb-4" v-if="identification_type=='frame_name'">
        <label>Nombre del IFrame:</label>
        <input class="form-control" v-model="frame_name" placeholder="Ej. frame_modal">
    </div>

    <div class="mb-4" v-if="identification_type=='frame_index'">
        <label>Indice del IFrame:</label>
        <input class="form-control" v-model="frame_index" placeholder="Ej. 1">
    </div>

    <div class="row g-2 mb-4" v-if="identification_type=='frame_web_element'">
        <div class="col-5">
            <label>Tipo de selector:</label>
            <select v-model="selector_type" class="form-select">
                <option class="text-grey-20" v-for="selector in list_selectors" :key="selector" :value="selector.toLowerCase()">{{ selector }}</option>
            </select>
        </div>
        <div class="col-7" >
            <input class="form-control" v-model="path_element" placeholder="Ej. //*[@id='element']">
        </div>
    </div>

    <div class="mb-4">
        <label>Tiempo de espera (en segundos):</label>
        <input class="form-control" v-model="wait_timeout">
    </div>

</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_selectors from "@/static/selectors"
    import list_identificators from "@/static/switch_identificators";
    import {replace_description} from "@/utils/formatters";

    const identification_type = ref("frame_name");
    const selector_type = ref("xpath");
    const path_element = ref("");
    const wait_timeout = ref(10);
    const frame_name = ref();
    const frame_index = ref();
    const description = ref("Se cambia al iframe por medio de su <b>{0}</b> {1}.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            identification_type.value = props.step?.data?.arguments?.identification_type;
            selector_type.value = props.step?.data?.arguments?.selector_type;
            path_element.value = props.step?.data?.arguments?.path_element;
            wait_timeout.value = props.step?.data?.arguments?.wait_timeout;
            frame_name.value = props.step?.data?.arguments?.frame_name;
            frame_index.value = props.step?.data?.arguments?.frame_index;
        }
    })

    const get_value_from_list_clicks  = (ele: string) => {
        return list_identificators.find(it => it.key === ele)?.value;
    };

    const clear_field = () => {
        frame_name.value = "";
        frame_index.value = "";
        path_element.value = "";
        selector_type.value = "xpath";
    };

    const get_identifier_value = () => {
      if (identification_type.value == "frame_name")
          return "<b>" + frame_name.value + "</b>";
      else if (identification_type.value == "frame_index")
          return "<b>" + frame_index.value + "</b>";
      else
          return "<b>" + path_element.value + "</b> cuyo selector es <b>" + selector_type.value +"</b>";
    };

    const send_description = () => {
        description.value = replace_description(description.value, get_value_from_list_clicks(identification_type.value).toLowerCase(), "0");
        description.value = replace_description(description.value, get_identifier_value(), "1");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":"switch_frame",
            "arguments":{
                "identification_type":identification_type.value,
                "frame_name":frame_name.value,
                "frame_index":frame_index.value,
                "selector_type":selector_type.value,
                "path_element":path_element.value,
                "wait_timeout":wait_timeout.value
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