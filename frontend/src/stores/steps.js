import { defineStore } from "pinia";

export let useStepStore = defineStore({
    id: 'steps',
    state: () => ({
        name_flux : '',
        list_steps : {steps:[]},
        list_vars : [],
        }),
    persist: {
        storage: sessionStorage,
        paths: ['name_flux','list_steps', 'list_vars'],
    },
})