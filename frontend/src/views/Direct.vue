<template>
  <div id="direct">
    <b-row>
        <b-col md="4">
            <Profiles :profileChannels="profileChannels" :setCurrentChannel="setCurrentChannel" />
        </b-col>
        <b-col md="8">
            <Channel :messages="currentChannel.messages" :channelCode="currentChannel.id" :reRenderer="setCurrentChannel" />
        </b-col>
    </b-row>
  </div>
</template>

<script>
import Profiles from '../components/direct/Profiles.vue'
import Channel from '../components/direct/Channel.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
    components: {
        Channel, Profiles
    },
    methods: {
      ...mapActions({setCurrentChannel: 'setCurrentChannelMessages'})
    },
    data() {
        return {
            
        }
    },
    computed: {
      ...mapGetters({profileChannels: 'getProfileChannels', currentChannel: 'getCurrentChannelMessages'})
    }
}
</script>

<style>

</style>