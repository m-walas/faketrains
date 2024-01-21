<template>
    <div class="route-display">
        <div v-if="route.first_leg && route.second_leg">

        <div class="leg">
            <v-icon small>mdi-train</v-icon>
            <p class="leg-info">{{ route.first_leg.departure_city }} <v-icon small>mdi-arrow-right</v-icon> {{ route.first_leg.arrival_city }}</p>
            <p class="leg-time"><v-icon small>mdi-clock-outline</v-icon> {{ route.first_leg.departure_time }} - {{ route.first_leg.arrival_time }}</p>
            <p class="leg-price"><v-icon small>mdi-cash-multiple</v-icon> Cena: {{ route.first_leg.ticket_price }}</p>
        </div>
        <div class="leg">
            <v-icon small>mdi-train</v-icon>
            <p class="leg-info">{{ route.second_leg.departure_city }} <v-icon small>mdi-arrow-right</v-icon> {{ route.second_leg.arrival_city }}</p>
            <p class="leg-time"><v-icon small>mdi-clock-outline</v-icon> {{ route.second_leg.departure_time }} - {{ route.second_leg.arrival_time }}</p>
            <p class="leg-price"><v-icon small>mdi-cash-multiple</v-icon> Cena: {{ route.second_leg.ticket_price }}</p>
        </div>
        </div>
        <div v-else class="direct-route">

        <p class="route-info"><v-icon small>mdi-train</v-icon> {{ route.departure_city }} <v-icon small>mdi-arrow-right</v-icon> {{ route.arrival_city }}</p>
        <p class="route-time"><v-icon small>mdi-clock-outline</v-icon> {{ route.departure_time }} - {{ route.arrival_time }}</p>
        <p class="route-price"><v-icon small>mdi-cash-multiple</v-icon> Cena: {{ route.ticket_price }}</p>
        </div>
    </div>
</template>

<script>
export default {
props: {
    route: Object,
},
};
</script>

<style scoped>
.route-display {
border: 1px solid #e0e0e0;
border-radius: 8px;
padding: 10px;
margin-bottom: 10px;
transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.route-display:hover {
transform: translateY(-5px);
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.leg, .direct-route {
margin-bottom: 10px;
}

.leg-info, .route-info {
font-weight: bold;
color: #1976d2;
}

.leg-time, .route-time, .leg-price, .route-price {
color: #555;
margin-left: 24px;
}

v-icon {
vertical-align: bottom;
}
</style>
