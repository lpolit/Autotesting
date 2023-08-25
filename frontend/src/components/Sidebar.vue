<template>
    <aside class="aux-container">
        <div class="aux">
            <div class="pt-1 px-2 animated slideInDown" style="font-size: x-large;color: #2c3e50">
                <label>{{ props.type_sidebar }}</label>
            </div>

            <div v-if="type_sidebar === 'img'">
                <div v-for="vars in list_vars_img()" :key="vars.key">
                    <div class="input-group mb-3">
                        <img :class="[img_value]"
                             v-bind:src="'data:image/png;base64;, ' + vars.value"
                             @mousedown="enlarge_img"
                             @mouseup="shrink_img"

                        >
                    </div>
                </div>
            </div>

            <div v-if="type_sidebar === 'txt'">
                <div v-for="vars in list_vars_text()" :key="vars.key">
                    <div class="input-group mb-3" v-if="vars.type === 'text'">
                        <div class="input-group-prepend" >
                            <span class="input-group-text" id="basic-addon1">{{vars.key}}</span>
                        </div>
                        <input type="text" class="form-control" v-model="vars.value" disabled>
                    </div>
                </div>
            </div>

        </div>
    </aside>

</template>

<script setup lang="ts">
import {useStepStore} from '@/stores/steps'
import {ref} from "vue";

const step_store = useStepStore();
const props = defineProps({
    title: String,
    type_sidebar: String
})
let img_value = ref("img-thumbnail")

const enlarge_img = () => {
    img_value.value = "img thumbnail"
}
const shrink_img = () => {
    img_value.value = "img-thumbnail"
}

const list_vars_img = () => {
    let imgs = step_store.list_vars.filter(it => it.type === 'img' );
    return imgs;
};

const list_vars_text = () => {
    let texts = step_store.list_vars.filter(it => it.type === 'text' );
    return texts;
};

</script>

<style scoped>

.aux-container {
    position: absolute;
    top: 70px;
    margin-top: 50px;
}

.aux-container, .aux{
    right: 0;
    width: 450px;
    height: 575px;
}

.aux {
    position: relative;
    /*background: #b7b7bd;*/
    background: #e2e2e2;
    color: white;
    transition: width 2s;
    border-radius: 0.25rem;
}

.input-group{
    width: 90% !important;
    margin-left: 1.5rem;
}

.img-thumbnail{
    transition: 0.5s ease;
    transition-delay: 0s;
    transition-duration: 1s;

}

.img.thumbnail{
    position: relative;
    top: -3rem;
    right: 60rem;
    border: 2px solid #0d658b;
    transform: translateX(-10%);
    transition: 0.5s ease;
    transform: scale(100%);
    }

.thumbnail:after{
    top: -3rem;
    right: 60rem;

}
</style>