import { defineStore } from "pinia";

export let useStepStore = defineStore({
    id: 'steps',
    state: () => ({
        list_steps : {steps:[]},
        list_vars : [],
        }),
    persist: {
        storage: sessionStorage,
        paths: ['list_steps', 'list_vars'],
    },
})