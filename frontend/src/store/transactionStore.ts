// stores/transactionStore.ts
import { defineStore } from 'pinia';

export const useTransactionStore = defineStore('transactionStore', {
    state: () => ({
        uuid: [],
        routeName: '',
        trainId: '',
        price: 0,
        selectedSeats: [],
    }),
    actions: {
        setTransactionDetails(routeName, trainId, price, selectedSeats) {
            this.routeName = routeName;
            this.trainId = trainId;
            this.price = price;
            this.selectedSeats = selectedSeats;
        },
        setTransactionUUID(uuid) {
            this.uuid = uuid;
        },
        clearTransactionDetails() {
            this.uuid = [];
            this.routeName = '';
            this.trainId = '';
            this.price = 0;
            this.selectedSeats = [];
        },
    },
});
