<template>
    <div>
        <swiper class="swiper" :options="swiperOption">
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=13"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=14"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=15"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=16"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=17"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=18"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=19"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=20"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=21"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=22"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=23"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=24"></b-avatar></swiper-slide>
            <swiper-slide><b-avatar size="4.5rem" src="https://loremflickr.com/320/240?random=25"></b-avatar></swiper-slide>
        </swiper>
    </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import "swiper/swiper-bundle.css"

export default {
    components: {
        Swiper, SwiperSlide
    },
    data() {
        return {
            swiperOption: {
                autoHeight: true,
                slidesPerView: 10,
                spaceBetween: 3,
                breakpoints: {
                    320: {
                        slidesPerView: 4.7,
                        spaceBetween: 10
                    },
                    480: {
                        slidesPerView: 7.5,
                        spaceBetween: 20
                    },
                    1120: {
                        slidesPerView: 11.6
                    }
                }
            }
        }
    }
}
</script>

<style scoped>
</style>