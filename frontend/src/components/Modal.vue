<template>
    <div>
    {{ name }}

    </div>
</template>

<script setup lang="ts">
import {onMounted, ref} from "vue";




const props = defineProps({
    name: String
})

onMounted (() => {

})

</script>