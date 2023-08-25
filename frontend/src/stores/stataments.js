import { defineStore } from "pinia";

export const useStatementStore = defineStore({
    id: 'statement',
    state: () => ({
        list_statements : [{"id":0,"oper1":"", "oper2":"", "operation":"", "condition":""}],
    }),
    actions: {
        add_statement(index, condition_type, operation_type, oper1, oper2) {

            const item_index = this.list_statements.findIndex(it => it.id === index);
            if (item_index !== -1) {
                this.update_statement(index, operation_type, oper1, condition_type, oper2);
            }
            let new_index = index + 1;
            let ele = {
                "id": new_index,
                "oper1": "",
                "oper2": "",
                "operation": "",
                "condition": ""
            };
            this.list_statements.push(ele);
        },
        remove_statement(index) {
            this.list_statements = this.list_statements.filter(it=> it.id != index)
        },
        update_statement(index, operation_type, oper1, condition_type, oper2) {
            let ele = {
                "id": index,
                "oper1": oper1,
                "oper2": oper2,
                "operation": operation_type,
                "condition": condition_type
            };
            const updateIndex = this.list_statements.findIndex(it => {
                return it.id === index
            });
            if (updateIndex !== -1)
                this.list_statements[updateIndex] = ele;
        },
        true_false_condition(condition_type) {
            return condition_type !== 'if_false' && condition_type !== 'if_true';
        }
    },
    getters: {

    }
})