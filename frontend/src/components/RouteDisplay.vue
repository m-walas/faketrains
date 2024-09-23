<template>
  <div class="route-display">
    <div v-if="route.first_leg && route.second_leg">
      <div class="leg">
        <p class="route-info" :class="{ active: isActive }">
          <v-icon small>mdi-train</v-icon> {{ route.first_leg.train_id }}
        </p>
        <p class="route_details">
          {{ route.first_leg.departure_city }} <v-icon small>mdi-arrow-right</v-icon> {{ route.first_leg.arrival_city }}
        </p>
        <p class="leg-time">
          <v-icon small>mdi-clock-outline</v-icon> {{ route.first_leg.departure_time }} - {{ route.first_leg.arrival_time }}
        </p>
        <p class="leg-price">
          <v-icon small>mdi-cash-multiple</v-icon> Cena: {{ route.first_leg.ticket_price }}
        </p>
      </div>
      <br>
      <div class="leg">
        <p class="route-info" :class="{ active: isActive }">
          <v-icon small>mdi-train</v-icon> {{ route.second_leg.train_id }}
        </p>
        <p class="route_details">
          {{ route.second_leg.departure_city }} <v-icon small>mdi-arrow-right</v-icon> {{ route.second_leg.arrival_city }}
        </p>
        <p class="leg-time">
          <v-icon small>mdi-clock-outline</v-icon> {{ route.second_leg.departure_time }} - {{ route.second_leg.arrival_time }}
        </p>
        <p class="leg-price">
          <v-icon small>mdi-cash-multiple</v-icon> Cena: {{ route.second_leg.ticket_price }}
        </p>
      </div>
    </div>
    <div v-else class="direct-route">
      <p class="route-info" :class="{ active: isActive }">
        <v-icon small>mdi-train</v-icon> {{ route.train_id }}
      </p>
      <p class="route_details">
        {{ route.departure_city }} <v-icon small>mdi-arrow-right</v-icon> {{ route.arrival_city }}
      </p>
      <p class="route-time">
        <v-icon small>mdi-clock-outline</v-icon> {{ route.departure_time }} - {{ route.arrival_time }}
      </p>
      <p class="route-price">
        <v-icon small>mdi-cash-multiple</v-icon> Cena: {{ route.ticket_price }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    route: {
      type: Object,
      required: true,
    },
    isActive: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped>
.route-display {
  border: 1px solid #e0e0e0;
  border-radius: 0.8vw;
  padding: 1vw;
  margin-bottom: 1vw;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.route_details {
  font-size: 1.2vw;
  color: #333; 
  display: flex; 
  align-items: center; 
  gap: 0.8vw;
  margin-bottom: 1vw;
}

.route-display:hover {
  transform: translateY(-0.5vw);
  box-shadow: 0 0.4vw 0.8vw rgba(0, 0, 0, 0.2);
}

.leg, .direct-route {
  margin-bottom: 1vw;
}

.route-info {
  font-weight: bold;
  color: grey; /* Domyślny kolor tekstu */
  margin-top: 1vw;
  font-size: 1.5vw;
  transition: color 0.3s ease;
}

.route-info.active {
  color: #ff2770; /* Różowy kolor dla aktywnej trasy */
}

.leg-time, .route-time, .leg-price, .route-price {
  color: #555;
  margin-left: 1.2vw;
  font-size: 1.2vw;
}

v-icon {
  vertical-align: bottom;
}
</style>
