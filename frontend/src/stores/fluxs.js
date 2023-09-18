import { defineStore } from "pinia";

export let useFluxStore = defineStore({
    id: 'flux',
    state: () => ({
        list : [],
        max:0
        }),
    persist: {
        storage: sessionStorage,
        paths: ['list', 'max'],
    },
})