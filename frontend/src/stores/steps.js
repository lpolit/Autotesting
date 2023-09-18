import { defineStore } from "pinia";

export let useStepStore = defineStore({
    id: 'steps',
    state: () => ({
        flux_name : '',
        project_name : '',
        list_steps : {steps:[]},
        list_vars : [],
        }),
    persist: {
        storage: sessionStorage,
        paths: ['flux_name','project_name','list_steps', 'list_vars'],
    },
})