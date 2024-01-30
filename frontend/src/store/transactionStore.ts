// stores/transactionStore.ts
import { defineStore } from 'pinia';

export const useTransactionStore = defineStore('transactionStore', {
    state: () => ({
        uuid: '',
        routeName: '',
        trainId: '',
        price: 0,
        selectedSeats: [],
    }),
    actions: {
        setTransactionDetails(uuid, routeName, trainId, price, selectedSeats) {
            this.uuid = uuid;
            this.routeName = routeName;
            this.trainId = trainId;
            this.price = price;
            this.selectedSeats = selectedSeats;
        },
        clearTransactionDetails() {
            this.uuid = '';
            this.routeName = '';
            this.trainId = '';
            this.price = 0;
            this.selectedSeats = [];
        },
    },
});
