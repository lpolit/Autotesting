<template>
    <div class="mb-4">
        <label>Valor actual:</label>
        <input  class="form-control" placeholder="Ingrese el valor actual" v-model="actual_value">
    </div>

    <div class="mb-4">
    <label>Criterio de comparación:</label>
        <select class="form-select" v-model="operator_type">
            <option class="text-grey-20" v-for="operator in list_operators" :key="operator.key" :value="operator.key">{{ operator.value }}</option>
        </select>
    </div>

    <div class="mb-4">
        <label>Valor esperado:</label>
        <input class="form-control"  placeholder="Ingrese un valor esperado" v-model="expected_value">
    </div>
</template>

<script setup lang="ts">
    import {onMounted, ref} from "vue";
    import list_operators from "@/static/assert_operators";
    import {replace_description} from "@/utils/formatters";

    const actual_value = ref("");
    const operator_type = ref("assert_equal");
    const expected_value = ref("");
    const description = ref("Verifica que <b>{0}</b> {1} a <b>{2}</b>.");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            actual_value.value = props.step?.data?.arguments?.actual_value,
            expected_value.value = props.step?.data?.arguments?.expected_value,
            operator_type.value = props.step?.data?.arguments?.operator_type
        }
    })

    const get_value_from_list_operators = (ele: string) => {
        return list_operators.find(it => it.key === ele)?.value;
    }

    const get_identifier_value = () => {
        const operator = get_value_from_list_operators(operator_type.value).toLowerCase();

        if (operator_type.value == "assert_contains")
            return "<b>" + operator + "</b>";
        else
            return "sea <b>" + operator + "</b>";
    }

    const send_description = () => {
        description.value = replace_description(description.value, actual_value.value, "0");
        description.value = replace_description(description.value, get_identifier_value(), "1");
        description.value = replace_description(description.value, expected_value.value, "2");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":operator_type.value,
            "arguments":{
                "actual_value": actual_value.value,
                "expected_value":expected_value.value,
                "operator_type":operator_type.value},
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