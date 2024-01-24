<template>
    <div v-if="!purchaseComplete">
        <div v-if="timeLeft > 0">
            <div v-for="(seat, index) in selectedSeats" :key="index">
                <br>
                <h3>Miejsce: {{ seat.seat_number }}</h3>
                <v-text-field 
                    label="Imię" 
                    v-model="seat.passenger.firstName" 
                    :rules="[v => !!v || 'Imię jest wymagane']"
                ></v-text-field>
                <v-text-field 
                    label="Nazwisko" 
                    v-model="seat.passenger.lastName" 
                    :rules="[v => !!v || 'Nazwisko jest wymagane']"
                ></v-text-field>
            </div>
            <v-checkbox 
                label="Potwierdzam poprawność danych i chcę dokonać transakcji" 
                v-model="isConfirmed"
            ></v-checkbox>
            <div class="confirm-section">
                <v-btn color="success" @click="confirmPassengerDetails" :disabled="!isConfirmed || !allFieldsValid">
                    Kup
                </v-btn>
                <span class="timer">{{ formattedTimeLeft }}</span>
                <span class="reservation-message" :class="{ blinking: isBlinking }">{{ reservationMessage }}</span>
            </div>
        </div>
        <div v-else>
            <br>
            <h3>Czas na wypełnienie formularza minął</h3>
            <!-- Można dodać przycisk do ponownego wyboru miejsc TODO: -->
        </div>
    </div>
    <div v-else>
        <h3>Bilet został pomyślnie zakupiony</h3>
        <v-btn color="primary" @click="goToHomePage">Powrót do strony głównej</v-btn>
    </div>
</template>

<script>
import { useTicketStore } from "@/store/ticketStore";
import axios from "axios";

export default {
    data() {
        return {
            timeLeft: 120,
            isConfirmed: false,
            isBlinking: false,
            purchaseComplete: false,
            purchaseMessage: '',
        };
    },
    computed: {
        selectedSeats() {
            return useTicketStore().getSelectedSeats;
        },
        allFieldsValid() {
            return this.selectedSeats.every(seat => 
                seat.passenger.firstName && seat.passenger.lastName
            );
        },
        formattedTimeLeft() {
            const minutes = Math.floor(this.timeLeft / 60);
            const seconds = this.timeLeft % 60;
            return `${minutes}:${seconds.toString().padStart(2, '0')}`;
        },
        reservationMessage() {
            return this.timeLeft <=30 ? "Czas Twojej rezerwacji zaraz minie." : "Wybrane miejsca są tymczasowo zarezerwowane.";
        },
    },
    mounted() {
        this.startTimer();
    },
    methods: {
        startTimer() {
            const timerInterval = setInterval(() => {
                this.timeLeft--;
                if (this.timeLeft <= 30) {
                    this.isBlinking = true;
                }
                if (this.timeLeft <= 0) {
                    clearInterval(timerInterval);
                    this.isBlinking = false;
                }
            }, 1000);
        },
        confirmPassengerDetails() {
            const ticketStore = useTicketStore();

            const ticketsData = this.selectedSeats.map(seat => ({
                seat_number: seat.seat_number,
                passenger: seat.passenger, 
            }));

            axios.post('/api/confirm_reservation/', {
                tickets: ticketsData
            })
            .then(response => {
                this.purchaseComplete = true;
                this.purchaseMessage = 'Transakcja przebiegła pomyślnie';

                clearInterval(this.timerInterval);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        },
        goToHomePage() {
            this.$router.push('/');
            this.clearReservationData();
        },
        clearReservationData() {
            const ticketStore = useTicketStore();
            ticketStore.clearSelectedSeats();
            ticketStore.clearTicketsCount();
        }
    },
    watch: {
        selectedTicketCount(newCount) {
            if (newCount !== this.selectedSeatNumbers.length) {
                this.selectedSeatNumbers = [];
                this.passengerFormVisible = false;
            }
        }
    },
};
</script>

<style scoped>
.confirm-section {
    display: flex;
    align-items: center;
}

.timer {
    margin-left: 20px;
    margin-right: 20px;
    font-size: 1.2em;
    font-weight: bold;
}

.reservation-message {
    font-size: 12px;
    font-style: italic;
    color: #4f5154;
}

.blinking {
    animation: blinker 2s linear infinite;
}

@keyframes blinker {
    50% {
        opacity: 0;
    }
}
</style>
