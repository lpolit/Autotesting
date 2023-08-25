<template>
    <div class="row g-2">
        <div class="col-2" v-if="props.index > 0">
            <label>Algo</label>
            <select v-model="operation_type" class="form-select" @change="statementStore.update_statement(index, operation_type, oper1, condition_type, oper2)">
                <option
                    class="text-grey-20"
                    v-for="operation in list_operators"
                    :key="operation.key"
                    :value="operation.key"
                >{{ operation.value }}</option>
            </select>
        </div>

        <div class="col-3">
            <label>Valor 1:</label>
            <input class="form-control" v-model="oper1" @change="statementStore.update_statement(index, operation_type, oper1, condition_type, oper2)">
        </div>

        <div class="col-3">
            <label>Condición:</label>
            <select v-model="condition_type" class="form-select" @change="statementStore.update_statement(index, operation_type, oper1, condition_type, oper2)">
                <option
                    class="text-grey-20"
                    v-for="condition in list_conditions"
                    :key="condition.key"
                    :value="condition.key"
                >{{ condition.value }}</option>
            </select>
        </div>

        <div class="col-3" v-if="statementStore.true_false_condition(condition_type)">
            <label>Valor 2:</label>
            <input class="form-control" v-model="oper2" @change="statementStore.update_statement(index, operation_type, oper1, condition_type, oper2)">
        </div>

        <div class="col-1 add">
            <button
                v-if="statementStore.list_statements.length-1 == props.index"
                icon="add"
                class="p-2"
                @click="statementStore.add_statement(props.index, condition_type, operation_type, oper1, oper2)"
            ></button>

            <button
                v-if="props.index > 0"
                icon="remove"
                class="p-2"
                @click="statementStore.remove_statement(index)"
            ></button>
        </div>
    </div>

</template>

<script setup lang="ts">
    import { ref } from "vue";
    import { useStatementStore } from "@/stores/stataments";
    import list_conditions from "@/static/ifstatement_conditions"
    const statementStore = useStatementStore();
    const oper1 = ref();
    const oper2 = ref();
    const condition_type = ref();
    const operation_type = ref();

    const props = defineProps({
        index: Number
    })

    const description = ref("Se borra el contenido del elemento web <b>{0}</b> usando el selector <b>{1}</b>.");

    const list_operators = [
        {"key":"if_and","value":"Y"},
        {"key":"if_or","value":"O"},
    ];

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

    const replace_description = (value: string, index: string): string => {
        if (value !== "")
            description.value = description.value.replace("{"+index+"}", value);
        return description.value;
    };

    defineExpose({
        send_arguments
    });

</script>

<style>
.add {
    display: flex;
    align-items: flex-end;
}
</style>