import { defineStore } from 'pinia'

const url = 'http://127.0.0.1:8000/api/v1/'

export const useDagsStore = defineStore("dagStore", {
    state: () => ({
        dags: [
        ],
    }),
    actions: {
        async getDags() {
            const res = await fetch(`${url}dags`)
            // .then(response => response.json())
            // .then(data => data.dags)
            // .catch(console.log('Error'))

            console.log(res)
            console.log(res.body)
            console.log(res.ok)
            const data = await res.json()
            console.log(data)
        }
    },
});