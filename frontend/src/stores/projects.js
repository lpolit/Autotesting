import { defineStore } from "pinia";

export let useProjectStore = defineStore({
    id: 'project',
    state: () => ({
        list : [],
        max:0
        }),
    persist: {
        storage: sessionStorage,
        paths: ['list','max'],
    },
})