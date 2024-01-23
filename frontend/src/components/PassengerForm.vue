<template>
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
        <!-- Można dodać przycisk do ponownego wyboru miejsc -->
    </div>
</template>

<script>
import { useTicketStore } from "@/store/ticketStore";

export default {
    data() {
        return {
            timeLeft: 45,
            isConfirmed: false,
            isBlinking: false,
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
            return this.timeLeft <=15 ? "Czas Twojej rezerwacji zaraz minie." : "Wybrane miejsca są tymczasowo zarezerwowane.";
        },
    },
    mounted() {
        this.startTimer();
    },
    methods: {
        startTimer() {
            const timerInterval = setInterval(() => {
                this.timeLeft--;
                if (this.timeLeft <= 15) {
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
            // Logika potwierdzenia danych pasażera
            // Możesz tutaj wywołać API, aby zaktualizować status miejsc
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
