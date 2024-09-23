<template>
  <v-container fill-height fluid class="routes-container">
    <div class="routes-info" v-if="schedules.length > 0">
      <h2>{{ schedules[0].departure_city }} - {{ schedules[0].arrival_city }}</h2>
    </div>

    <div class="routes-carousel-container" v-if="schedules.length > 0">
      <div
        class="routes-carousel-button prev"
        :class="{ disabled: isPrevDisabled }"
        @mousemove="handlePrevMouseMove"
        @mouseleave="handlePrevMouseLeave"
      >
        <v-icon>mdi-chevron-left</v-icon>
      </div>
      <div
        class="routes-carousel-button next"
        :class="{ disabled: isNextDisabled }"
        @mousemove="handleNextMouseMove"
        @mouseleave="handleNextMouseLeave"
      >
        <v-icon>mdi-chevron-right</v-icon>
      </div>

      <Swiper
        ref="swiper"
        :modules="swiperModules"
        :slides-per-view="visibleItems"
        :space-between="30"
        :centered-slides="!isMobile"
        :navigation="!isMobile ? {
          nextEl: '.routes-carousel-button.next',
          prevEl: '.routes-carousel-button.prev'
        } : false"
        :pagination="isMobile ? { clickable: true, el: '.routes-carousel-indicators' } : false"
        :effect="'coverflow'"
        :coverflowEffect="coverflowEffect"
        :speed="700"
        @slideChange="onSlideChange"
        class="routes-carousel"
      >
        <SwiperSlide
          v-for="(route, index) in schedules"
          :key="index"
          @click="setActiveIndex(index)"
          :class="getItemClasses(index)"
        >
          <v-card class="routes-route-card">
            <v-card-text>
              <RouteDisplay :route="route" :isActive="index === activeIndex"></RouteDisplay>
            </v-card-text>
          </v-card>
        </SwiperSlide>

        <div class="routes-carousel-indicators" v-if="isMobile"></div>
      </Swiper>
    </div>

    <div v-if="detailsIndex >= 0" class="routes-details-panel">
      <RouteDetails :route="schedules[detailsIndex]"></RouteDetails>
    </div>
  </v-container>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/swiper-bundle.css';
import { Navigation, Pagination, EffectCoverflow } from 'swiper/modules';
import RouteDisplay from './RouteDisplay.vue';
import RouteDetails from './RouteDetails.vue';
import { useRoutesStore } from '../store/routes';
import debounce from 'lodash/debounce';

export default {
  components: {
    RouteDisplay,
    RouteDetails,
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      routesStore: useRoutesStore(),
      activeIndex: 0,
      detailsIndex: -1,
      isMobile: window.innerWidth <= 600,
      coverflowEffect: {
        rotate: -25,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: false,
      },
      swiperModules: [Navigation, Pagination, EffectCoverflow],
    };
  },
  computed: {
    schedules() {
      return this.routesStore.schedules || [];
    },
    visibleItems() {
      return this.isMobile ? 1 : 3;
    },
    maxIndex() {
      // FIXME: 
      // console.log('schedules', this.schedules.length);
      // console.log('visibleItems', this.visibleItems);
      // console.log('MaxIndex', Math.max(this.schedules.length - this.visibleItems, 0));
      return Math.max(this.schedules.length, 0);
      // was:
      // return Math.max(this.schedules.length - this.visibleItems, 0);
      // why?
    },
    isPrevDisabled() {
      return this.activeIndex === 0;
    },
    isNextDisabled() {
      // console.log('isNextDisabled', this.activeIndex === this.maxIndex);
      // console.log('activeIndex', this.activeIndex);
      // console.log('maxIndex', this.maxIndex);
      // starting index from 0 that's why subtract 1
      return this.activeIndex === (this.maxIndex - 1);
    },
  },
  methods: {
    setActiveIndex(index) {
      this.activeIndex = index;
      this.detailsIndex = index;
      this.$refs.swiper.swiper.slideTo(index);
    },
    onSlideChange(swiper) {
      this.activeIndex = swiper.realIndex;
      this.detailsIndex = swiper.realIndex;
    },
    getItemClasses(index) {
      const classes = [];
      const offset = index - this.activeIndex;

      if (index === this.activeIndex) {
        classes.push('active');
      } else if (offset === -1) {
        classes.push('prev-slide');
      } else if (offset === 1) {
        classes.push('next-slide');
      } else if (offset < -1) {
        classes.push('far-prev-slide');
      } else if (offset > 1) {
        classes.push('far-next-slide');
      }
      return classes;
    },
    updateDimensions() {
      this.isMobile = window.innerWidth <= 600;
      if (this.activeIndex > this.maxIndex) {
        this.activeIndex = this.maxIndex;
        this.$refs.swiper.swiper.slideTo(this.maxIndex);
      }
    },
    debouncedHandleResize: debounce(function () {
      this.updateDimensions();
    }, 200),
    handleMouseMove(event) {
      const btn = event.currentTarget;
      const rect = btn.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      btn.style.setProperty('--mouse-x', `${x}%`);
      btn.style.setProperty('--mouse-y', `${y}%`);
    },
    resetMousePosition(event) {
      const btn = event.currentTarget;
      btn.style.removeProperty('--mouse-x');
      btn.style.removeProperty('--mouse-y');
    },
    handlePrevMouseMove(event) {
      if (!this.isPrevDisabled) {
        this.handleMouseMove(event);
      }
    },
    handlePrevMouseLeave(event) {
      if (!this.isPrevDisabled) {
        this.resetMousePosition(event);
      }
    },
    handleNextMouseMove(event) {
      if (!this.isNextDisabled) {
        this.handleMouseMove(event);
      }
    },
    handleNextMouseLeave(event) {
      if (!this.isNextDisabled) {
        this.resetMousePosition(event);
      }
    },
  },
  mounted() {
    this.updateDimensions();
    window.addEventListener('resize', this.debouncedHandleResize);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.debouncedHandleResize);
  },
};
</script>

<style scoped>
.routes-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 2vw;
  background-color: transparent;
}

.routes-info {
  text-align: center;
  margin-bottom: 2vw;
  margin-top: 5vw;
  color: #ffffff;
  font-size: 2vw;
}

.routes-info h2 {
  color: #ff2770;
  font-weight: bold;
}

.routes-carousel-container {
  position: relative;
  overflow: hidden;
  margin-bottom: 2vw;
}

.routes-carousel-button {
  position: absolute;
  top: 50%;
  color: #fff;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 4;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s ease-out, background-color 0.2s ease-out;
  box-shadow: none !important;
  padding: 4px;
}

.routes-carousel-button:hover {
  background-color: rgba(0, 0, 0, 0.5);
  box-shadow: none !important;
  background-image: none !important;
  transform: translate(
    calc((var(--mouse-x, 50%) - 50%) / 5),
    calc((var(--mouse-y, 50%) - 50%) / 5)
  );
  cursor: none;
}

.routes-carousel-button.prev {
  left: 10px;
}

.routes-carousel-button.next {
  right: 10px;
}

.routes-carousel-button::before {
  content: '';
  position: absolute;
  top: -5px;
  left: -5px;
  width: calc(100% + 10px);
  height: calc(100% + 10px);
  border: 1px solid rgba(255, 255, 255, 0);
  border-radius: 50%;
  box-sizing: border-box;
  transform: rotate(0deg);
  transition: border-color 0.3s ease, opacity 0.3s ease;
  opacity: 0;
  pointer-events: none;
}

.routes-carousel-button:hover::before {
  border-color: rgba(255, 255, 255, 0.5);
  opacity: 1;
  animation: routes-rotateBorder 10s linear infinite;
}

@keyframes routes-rotateBorder {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.routes-carousel-button.disabled {
  opacity: 0.4;
  cursor: not-allowed;
  pointer-events: none;
  background-color: rgba(0, 0, 0, 0.2);
}

.routes-carousel-button.disabled:hover {
  background-color: rgba(0, 0, 0, 0.2);
  transform: none;
}

.routes-carousel-button.disabled::before {
  border-color: rgba(255, 255, 255, 0);
  opacity: 0;
  animation: none;
}

.routes-route-card {
  background-color: rgba(30, 30, 30, 0.8);
  backdrop-filter: blur(10px);
  color: #fff;
  border-radius: 10px;
  box-shadow: none;
  transition: transform 0.3s ease, opacity 0.3s ease;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.routes-route-card:hover {
  transform: translateY(-5px);
}

.routes-route-card .v-card-text {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.routes-carousel-item {
  opacity: 0.5;
  transition: transform 0.7s ease, opacity 0.7s ease;
  position: relative;
  transform-origin: center;
}

.routes-carousel-item.active {
  opacity: 1;
  transform: perspective(1000px) rotateY(0deg) scale(1);
  z-index: 3;
}

.routes-carousel-item.prev-slide {
  opacity: 0.7;
  transform: perspective(1000px) rotateY(30deg) scale(0.8);
  z-index: 2;
}

.routes-carousel-item.next-slide {
  opacity: 0.7;
  transform: perspective(1000px) rotateY(-30deg) scale(0.8);
  z-index: 2;
}

.routes-carousel-item.far-prev-slide,
.routes-carousel-item.far-next-slide {
  opacity: 0.3;
  transform: perspective(1000px) rotateY(45deg) scale(0.6);
  z-index: 1;
}

.routes-carousel-item:hover {
  cursor: pointer;
}

.routes-carousel-indicators {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.routes-carousel-indicators :deep(.swiper-pagination-bullet) {
  width: 8px;
  height: 8px;
  background-color: #ffffff;
  opacity: 0.5;
  border-radius: 50%;
  margin: 0 5px;
  transition: opacity 0.3s ease;
}

.routes-carousel-indicators :deep(.swiper-pagination-bullet-active) {
  opacity: 1;
}

@media (max-width: 600px) {
  .routes-carousel-item {
    flex: 0 0 60%;
    margin: 0 20%;
  }

  .routes-carousel-button {
    display: none;
  }
}
</style>
