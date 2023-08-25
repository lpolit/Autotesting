<template>
    <div class="mb-4">
        <label>Tipo de espera:</label>
        <select class="form-select" v-model="wait_type">
            <option class="text-grey-20" v-for="wait in list_waits" :key="wait.key" :value="wait.key">{{ wait.value.replace("{0}", "") }}</option>
        </select>
    </div>

    <div class="row g-2 mb-4" v-if="locator_field">
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

    <div class="mb-4" v-if="text_field">
        <label>Valor del campo:</label>
        <input class="form-control" placeholder="Ingrese aquí el texto" v-model="text_value">
    </div>

    <div class="mb-4" v-if="state_field">
        <label>Estado:</label>
        <select v-model="state_type" class="form-select">
            <option class="text-grey-20" v-for="st in list_states" :key="st" :value="st">{{ st }}</option>
        </select>
    </div>

    <div class="mb-4">
        <label>Tiempo de espera:</label>
        <input class="form-control" v-model="wait_timeout" placeholder="2">
    </div>
</template>

<script setup lang="ts">
    import {computed, onMounted, ref} from "vue";
    import list_selectors from "@/static/selectors";
    import list_waits from "@/static/waits";
    import {replace_description} from "@/utils/formatters";

    const wait_type = ref("");
    const selector_type = ref("xpath");
    const path_element = ref();
    const text_value = ref("");
    const state_type = ref();
    const wait_timeout = ref(10);
    const description = ref("Espera a {0}");

    const props = defineProps({
        step: Object
    })

    onMounted (() => {
        if (props.step.data) {
            wait_type.value = props.step?.data?.arguments?.wait_type;
            selector_type.value = props.step?.data?.arguments?.selector_type;
            path_element.value = props.step?.data?.arguments?.path_element;
            text_value.value = props.step?.data?.arguments?.text_value;
            state_type.value = props.step?.data?.arguments?.state_type;
            wait_timeout.value = props.step?.data?.arguments?.wait_timeout;
        }
    })

    const list_states = ["Seleccionado", "No seleccionado"];

    const text_field = computed(() =>{
        return wait_type.value=='wait_title_is' || wait_type.value=='wait_title_contains' ||
                wait_type.value=='wait_url_contains' || wait_type.value=='wait_url_matches' ||
            wait_type.value=='wait_url_changes' || wait_type.value=='wait_url_to_be' ||
            wait_type.value=='wait_element_to_be_text_is_present' || wait_type.value=='wait_element_text_value_is_present' ||
            wait_type.value=='wait_for_number_of_windows_to_be'
    })

    const locator_field = computed(() =>{
        return wait_type.value=='wait_element_is_presence' || wait_type.value=='wait_element_to_be_visible' ||
            wait_type.value=='wait_all_elements_is_presence' || wait_type.value=='wait_any_element_to_be_visible' ||
            wait_type.value=='wait_all_elements_to_be_visible' || wait_type.value=='wait_frame_to_be_available_and_switch_to_it' ||
            wait_type.value=='wait_element_to_be_invisible' || wait_type.value=='wait_element_to_be_clickable' ||
            wait_type.value=='wait_staleness_of' || wait_type.value=='wait_element_to_be_selected' ||
            wait_type.value=='wait_element_to_be_text_is_present' || wait_type.value=='wait_element_text_value_is_present' ||
            wait_type.value=='wait_element_selection_to_be_state'
    })

    const state_field = computed(() =>{
        return wait_type.value === 'wait_element_selection_to_be_state'
    })

    const get_identifier_value = () => {
        const value = get_value_from_list_waits(wait_type.value);
        if (wait_type.value === 'wait_element_to_be_text_is_present')
            return "que el elemento <b>" + path_element.value + " </b> con selector <b>" + selector_type.value +"</b> tenga presente el texto " +
                "<b>" + text_value.value + "</b>."
        else if(wait_type.value === 'wait_element_text_value_is_present')
            return "que el elemento <b>" + path_element.value + " </b> con selector <b>" + selector_type.value +"</b> tenga presente en el atributo value el texto " +
                "<b>" + text_value.value + "</b>."
        else if (state_field.value){
            const desc = "<b>" + path_element.value + " </b> con selector <b>" + selector_type.value +"</b>";
            return value?.replace("{0}", desc) + " " + "<b>" + state_type.value.toLowerCase() + "</b>";
        }
        else if(text_field.value)
            return "<b>" + value + " " + text_value.value.toLowerCase() +"</b>";
        else if (locator_field.value){
            const desc = "<b>" + path_element.value + " </b> con selector <b>" + selector_type.value +"</b>";
            return value?.replace("{0}", desc );
        }else{
            return "<b>" + value + "</b>."
        }

    };

    const get_value_from_list_waits  = (ele: string) => {
        return list_waits.find(it => it.key === ele)?.value;
    };

    const send_description = () => {
        description.value = replace_description(description.value, get_identifier_value(), "0");
        return description.value;
    };

    const send_arguments = () => {
        return  {
            "command":wait_type.value,
            "arguments":{
                "wait_type":wait_type.value,
                "selector_type":selector_type.value,
                "path_element":path_element.value,
                "text_value":text_value.value,
                "state_type":state_type.value,
                "wait_timeout":wait_timeout
            }
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