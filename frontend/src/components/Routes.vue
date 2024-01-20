<template>
    <v-container>
        <div class="route-info">
        <h2>{{ selectedRouteInfo }}</h2>
        </div>
        <div class="carousel-container">
        <v-btn icon class="carousel-button left" @click="prevCarouselItem" v-if="activeIndex > 0">
            <v-icon>mdi-chevron-left</v-icon>
        </v-btn>

        <div class="carousel-wrapper">
            <div class="carousel" :style="carouselStyle">
            <div v-for="(route, index) in schedules" :key="index" class="carousel-item" :class="{ active: index === activeIndex }">
                <v-card class="route-card" @click="toggleDetails(index)">
                <v-card-text>
                    <div class="route-summary">
                    <div class="route-time">
                        <v-icon small>mdi-clock-outline</v-icon>
                        {{ getDepartureTime(route) }} - {{ getArrivalTime(route) }}
                    </div>
                    <div class="route-duration">
                        <v-icon small>mdi-timer-sand</v-icon>
                        Czas podróży: {{ getTravelTime(route) }}
                    </div>
                    <div class="route-price">
                        <v-icon small>mdi-cash-multiple</v-icon>
                        Cena: {{ getTicketPrice(route) }}
                    </div>
                    <div class="route-direct">
                        <v-icon small>mdi-transfer-right</v-icon>
                        Bezpośredni: {{ isDirect(route) ? 'Tak' : 'Nie' }}
                    </div>
                    </div>
                </v-card-text>
                </v-card>
            </div>
            </div>
        </div>

        <v-btn icon class="carousel-button right" @click="nextCarouselItem" v-if="activeIndex != (schedules.length - 1)">
            <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
        </div>

        <div v-if="detailsIndex >= 0" class="details-panel" :id="`details-${detailsIndex}`">
            <div class="route-details">
                <h3>Szczegóły Trasy</h3>
                <p><strong>Odjazd:</strong> {{ getDepartureTime(schedules[detailsIndex]) }} z {{ schedules[detailsIndex].departure_city }}</p>
                <p><strong>Przyjazd:</strong> {{ getArrivalTime(schedules[detailsIndex]) }} do {{ schedules[detailsIndex].arrival_city }}</p>
                <p><strong>Czas podróży:</strong> {{ getTravelTime(schedules[detailsIndex]) }}</p>
                <p><strong>Cena biletu:</strong> {{ getTicketPrice(schedules[detailsIndex]) }}</p>
                <p><strong>Bezpośredni:</strong> {{ isDirect(schedules[detailsIndex]) ? 'Tak' : 'Nie' }}</p>
            </div>
            <div class="ticket-options">
                <h3>Wybór biletów</h3>
                <div class="option">
                <label>Ilość biletów:</label>
                <select v-model="selectedTicketCount">
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
                </div>
                <div class="option">
                <label>Ulga:</label>
                <select v-model="selectedDiscount">
                    <option value="normal">Normalny</option>
                    <!-- <option value="student">Student</option> -->
                </select>
                </div>
                <v-btn text small class="button-choose-seat" @click="selectSeats">Wybierz miejsce</v-btn>
            </div>
            </div>
    </v-container>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

body {
font-family: 'Roboto', sans-serif;
}

.route-info {
text-align: center;
margin-bottom: 20px;
margin-top: 50px;
}

.carousel-container {
overflow: hidden;
width: 640px; 
margin: 0 auto;
}

.carousel-wrapper {
width: 300px; 
margin-left: 170px; 
}

.carousel {
display: flex;
justify-content: flex-start;
transition: transform 0.5s ease-in-out;
}

.carousel-item {
flex: 0 0 300px;
opacity: 0.5;
transition: transform 0.5s ease, opacity 0.3s ease;
margin: 0 10px;
}

.carousel-item.active {
opacity: 1;
transform: scale(1.1);
}

.carousel-button {
position: absolute;
top: 50%;
transform: translateY(-50%);
}

.carousel-button.left {
left: 10px;
}

.carousel-button.right {
right: 10px;
}

.route-card {
max-width: 300px;
min-height: 400px;
text-align: left;
transition: transform 0.3s ease, box-shadow 0.3s ease;
box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
margin-top: 20px;
}

.route-card:hover {
transform: scale(1.03);
box-shadow: 0 6px 12px 0 rgba(0,0,0,0.3);
}

.v-btn:hover {
background-color: #0056b3;
color: white;
}

@media only screen and (max-width: 600px) {
.carousel-wrapper {
    width: 100%;
}

.carousel-item {
    width: 100%;
}
}

.details-panel {
padding: 20px;
background-color: #f2f2f2;
border-radius: 8px;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
margin-top: 20px;
} 

.ticket-options {
display: flex;
justify-content: space-between;
margin-bottom: 10px;
background-color: white;
padding: 15px;
border-radius: 8px;
}

.ticket-options h3 {
margin-top: 0;
}

.route-details {
background-color: white;
padding: 15px;
border-radius: 8px;
margin-bottom: 20px;
}

.route-details h3 {
margin-top: 0;
}

.option {
margin-bottom: 15px;
}

option {
padding: 10px;
}

select {
padding: 8px 12px;
border: 1px solid #ccc;
border-radius: 4px;
background-color: white;
cursor: pointer;
appearance: none;
width: 100%;
}

select:focus {
outline: none;
border-color: #0056b3;
}

.v-btn {
background-color: #0056b3;
color: white;
text-transform: uppercase;
font-weight: bold;
}

.v-btn:hover {
background-color: #003d82;
}

.button-choose-seat {
margin-top: 25px;
}
</style>

<script>
import { defineComponent, computed, ref } from 'vue';
import { useRoutesStore } from '../store/routes';

export default defineComponent({
setup() {
    const routesStore = useRoutesStore();
    const schedules = computed(() => routesStore.schedules);
    const activeIndex = ref(0);
    const detailsIndex = ref(-1);
    const selectedTicketCount = ref(0);
    const selectedDiscount = ref('normal');

    const getDepartureTime = (route) => route.departure_time || 'Nieznany';
    const getArrivalTime = (route) => route.arrival_time || 'Nieznany';
    const getTravelTime = (route) => route.travel_time || 'Nieznany';
    const getTicketPrice = (route) => route.ticket_price || 'Nieznany';
    const isDirect = (route) => !route.is_transfer;

    const selectedRouteInfo = computed(() => {
    if (schedules.value.length > 0) {
        return `${schedules.value[0].departure_city} - ${schedules.value[0].arrival_city}`;
    }
    return 'Wybierz trasę';
    });

    const scrollToDetails = () => {
        const element = document.getElementById(`details-${detailsIndex.value}`);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    };

    const toggleDetails = (index) => {
        detailsIndex.value = detailsIndex.value === index ? -1 : index;
        scrollToDetails(index);
    };

    const nextCarouselItem = () => {
        if (activeIndex.value < (schedules.value?.length - 1)) {
            activeIndex.value++;
        }
    };

    const prevCarouselItem = () => {
        if (activeIndex.value > 0) {
            activeIndex.value--;
        }
    };

    const selectSeats = () => {
        // Logika do wyboru miejsc
    };

    const proceedToNextStep = () => {
        // Logika do przejścia do następnego kroku
    };

    return {
    schedules,
    getDepartureTime,
    getArrivalTime,
    getTravelTime,
    getTicketPrice,
    isDirect,
    selectedRouteInfo,
    nextCarouselItem,
    prevCarouselItem,
    activeIndex,
    toggleDetails,
    detailsIndex,
    selectSeats,
    proceedToNextStep,
    selectedTicketCount,
    selectedDiscount,
    scrollToDetails,
    };
},
computed: {
    carouselStyle() {
        const offset = this.activeIndex * 320;
        return { transform: `translateX(${-offset}px)` };
    },
},
});
</script>