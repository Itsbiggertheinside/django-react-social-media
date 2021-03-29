<template>
  <div id="direct">
    <b-row>
        <b-col md="3">
            <Friends :followingList="followingList" />
        </b-col>
        <b-col md="9">
            <Channel />
        </b-col>
    </b-row>
  </div>
</template>

<script>
import Friends from '../components/direct/Friends.vue'
import Channel from '../components/direct/Channel.vue'
import { mapGetters } from 'vuex'


export default {
    components: {
        Channel, Friends
    },
    data() {
        return {
            
        }
    },
    computed: {
      ...mapGetters({followingList: 'getFollowingList'})
    },
    mounted() {
        
    }
}
</script>

<style>

</style>