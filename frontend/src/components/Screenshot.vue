<template>
    <div class="mb-4">
        <label>Capturar:</label>
        <select v-model="screenshot_type" class="form-select" @change="clear_field()">
            <option class="text-grey-20" v-for="sshot in list_screenshots" :key="sshot.key" :value="sshot.key">{{ sshot.value }}</option>
        </select>
    </div>

    <div class="row g-2 mb-4" v-if="screenshot_type=='screenshot_web_element'">
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
        <input class="form-control"  v-model="wait_timeout">
    </div>

    <div class="mb-4">
        <label class="me-4">Variable producida:</label>
        <input class="form-control" v-model="screenshot">
    </div>

</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_selectors from "@/static/selectors";
    import list_screenshots from "@/static/screenshots";
    import {replace_description} from "@/utils/formatters";

    const screenshot_type = ref();
    const selector_type = ref("xpath");
    const path_element = ref("");
    const wait_timeout = ref(10);
    const screenshot = ref("{screenshot}")
    const description = ref("Se realiza la captura {0}.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            screenshot_type.value = props.step?.data?.arguments?.screenshot_type;
            selector_type.value = props.step?.data?.arguments?.selector_type;
            path_element.value = props.step?.data?.arguments?.path_element;
            wait_timeout.value = props.step?.data?.arguments?.wait_timeout;
            screenshot.value = props.step?.data?.arguments?.var_name;
        }
    })


    const get_value_from_list_screenshots  = (ele: string) => {
        return list_screenshots.find(it => it.key === ele)?.value;
    };

    const clear_field = () => {
        path_element.value = "";
        selector_type.value = "xpath";
    };

    const get_identifier_value = () => {
      if (screenshot_type.value == "screenshot_page")
          return "de la <b>" + get_value_from_list_screenshots(screenshot_type.value)?.toLowerCase() + "</b>";
      else if (screenshot_type.value == "screenshot_full_page")
          return "de la <b>" + get_value_from_list_screenshots(screenshot_type.value)?.toLowerCase() + "</b>";
      else
          return "del <b>" + get_value_from_list_screenshots(screenshot_type.value)?.toLowerCase() + " " + path_element.value + "</b> cuyo selector es <b>" + selector_type.value +"</b>";
    };

    const send_description = () => {
        description.value = replace_description(description.value, get_identifier_value(), "0");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":screenshot_type.value,
            "arguments":{
                "screenshot_type":screenshot_type.value,
                "selector_type":selector_type.value,
                "path_element":path_element.value,
                "wait_timeout":wait_timeout.value,
                "var_name":screenshot.value
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