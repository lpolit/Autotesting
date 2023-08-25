<template>
    <div class="row g-2 mb-4">
        <div class="col-5">
            <label>Tipo de selector:</label>
            <select v-model="selector_type" class="form-select">
                <option class="text-grey-20" v-for="selector in list_selectors" :key="selector" :value="selector.toLowerCase()">{{ selector }}</option>
            </select>
        </div>
        <div >
            <input class="form-control"  v-model="path_element" placeholder="Ej. //*[@id='element']">
        </div>
    </div>

    <div class="mb-4">
        <label>Tipo de clic:</label>
        <select v-model="click_type" class="form-select">
            <option class="text-grey-20" v-for="click in list_clicks" :key="click.key" :value="click.key">{{ click.value }}</option>
        </select>
    </div>

    <div class="mb-4">
        <label>Tiempo de espera (en segundos):</label>
        <input class="form-control"  v-model="wait_timeout">
    </div>

</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_selectors from "@/static/selectors";
    import list_clicks from "@/static/clicks";
    import {replace_description} from "@/utils/formatters";


    const selector_type = ref("xpath");
    const click_type = ref("left_click");
    const path_element = ref("");
    const wait_timeout = ref(10);
    const description = ref("Hace click <b>{0}</b> en el elemento web <b>{1}</b> usando el selector <b>{2}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            selector_type.value = props.step?.data?.arguments?.selector_type;
            click_type.value = props.step?.data?.arguments?.click_type;
            path_element.value = props.step?.data?.arguments?.path_element;
            wait_timeout.value = props.step?.data?.arguments?.wait_timeout;
        }
    })

    const get_value_from_list_clicks  = (ele: string) => {
        return list_clicks.find(it => it.key === ele)?.value;
    }

    const send_description = () => {
        description.value = replace_description(description.value, get_value_from_list_clicks(click_type.value), "0");
        description.value = replace_description(description.value, path_element.value, "1");
        description.value = replace_description(description.value, selector_type.value, "2");
        return description.value;
    };

    const send_arguments = () => {
        return  {"command":click_type.value,
            "arguments":{
                "selector_type":selector_type.value,
                "path_element":path_element.value,
                "click_type":click_type.value,
                "wait_timeout":wait_timeout.value
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