import { defineStore } from 'pinia'

const url = 'http://127.0.0.1:8000/api/v1/'

export const useDagsStore = defineStore("dagStore", {
    state: () => ({
        loader: false,
        data: [],
        newItem: {
            
            id: 0,
            name: '',
            context: '',
            interval: 0,
            create_at: '',
            update_at: '',
            status: false
            
        },
    }),
    actions: {
        async getDags() {            
            this.loader = true;
            const res = await fetch(`${url}dags`);
            const collections = await res.json();
            this.data = collections;
            console.log(collections)
            this.loader = false;
        },
        async addDag() {
            this.loader = true
            // const res = await fetch(`${url}dags`, {
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/json;charset=utf-8'
            //     },
            //     body: obj
            // });
            // const collections = await res.json();
            // this.data = collections;
            console.log("New item in state",this.newItem)
            this.cleanAddTableItem();
            this.loader = false
        },
        async delDag(id) {
            this.loader = true
            const res = await fetch(`${url}dags/${id}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
            });
            const collections = await res.json();
            this.data = collections;
            this.loader = false
        },
        async updateDag(id, event) {
            console.log(event)
            this.loader = true
            console.log('send update');
            this.loader = false
        },
        addTableItem() {            
            this.newItem.id = 0,
            this.newItem.name = 'New',
            this.newItem.context = 'print("Hello World")',
            this.newItem.interval = 0,
            this.newItem.create_at = Date.now(),
            this.newItem.update_at = Date.now(),
            this.newItem.status = false
            console.log(this.newItem)
        },
        updateTableItem(obj) {            
            this.newItem.id = obj.id,
            this.newItem.name = obj.name,
            this.newItem.context = obj.context,
            this.newItem.interval = obj.interval,
            this.newItem.create_at = obj.create_at,
            this.newItem.update_at = obj.update_at,
            this.newItem.status = obj.status
            console.log(this.newItem)
        },
        cleanAddTableItem() {
            this.newItem.id = undefined,
            this.newItem.name = undefined,
            this.newItem.context = undefined,
            this.newItem.interval = undefined,
            this.newItem.create_at = undefined,
            this.newItem.update_at = undefined,
            this.newItem.status = undefined
        }
    },
});