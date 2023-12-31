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
        actionAddItem: false,
        pushAlertSuccess: false,
        pushAlertError: false,
    }),
    getters: {
        getNewItem() {
            return this.newItem
        }
    },
    actions: {
        async getDags() {            
            const res = await fetch(`${url}dags`);
            const collections = await res.json();
            this.data = collections;
            this.loader = false
        },
        async addDag() {
            this.loader = true
            const res = await fetch(`${url}dags`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify(this.newItem)
            });
            const collections = await res.json();
            this.data = collections;
            this.sendAlertMsg(res)
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
            this.sendAlertMsg(res);
            this.loader = false
        },
        async updateDag(index) {
            this.loader = true
            const res = await fetch(`${url}dags/${this.data.dags[index].id}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify(this.data.dags[index])
            });
            const collections = await res.json();
            this.data = collections;;
            this.sendAlertMsg(res)
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
            this.actionAddItem = true
        },
        cleanAddTableItem() {
            this.newItem.name = '',
            this.actionAddItem = false
        },
        closeAlert(targetAlert) {
            if (targetAlert === "success") {
                this.pushAlertSuccess = false;
            } else {
                this.pushAlertError = false;
            }            
        },
        sendAlertMsg(res) {
            if (res.status === 200 || res.status === 201) {
                this.pushAlertSuccess = true
            } else {
                this.pushAlertError = true
            }
        }
        
    },
});