<template>
    <div class="row g-2 mb-4">
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
        <label>Criterio:</label>
        <select v-model="criteria_type" class="form-select">
            <option class="text-grey-20" v-for="criteria in list_criteria" :key="criteria.key" :value="criteria.key">{{ criteria.value }}</option>
        </select>
    </div>
</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_selectors from "@/static/selectors";
    import list_criteria from "@/static/assert_criteria";
    import {replace_description} from "@/utils/formatters";

    const selector_type = ref("xpath");
    const path_element = ref("");
    const criteria_type = ref("visible")
    const description = ref("Verifica que elemento web <b>{0}</b> usando el selector <b>{1}</b> <b>{2}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            selector_type.value = props.step?.data?.arguments?.selector_type;
            path_element.value = props.step?.data?.arguments?.path_element;
            criteria_type.value = props.step?.data?.arguments?.criteria_type;

        }
    })

    const get_value_from_list_criteria  = (ele: string) => {
        return list_criteria.find(it => it.key === ele)?.value;
    }

    const send_description = () => {
        description.value = replace_description(description.value, path_element.value, "0");
        description.value = replace_description(description.value, selector_type.value, "1");
        description.value = replace_description(description.value, get_value_from_list_criteria(criteria_type.value).toLowerCase(), "2");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":criteria_type.value,
            "arguments":{
                "selector_type": selector_type.value,
                "path_element": path_element.value,
                "criteria_type": criteria_type.value
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