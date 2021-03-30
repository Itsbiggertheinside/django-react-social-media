<template>
  <div id="direct">
    <b-row>
        <b-col md="4">
            <Profiles :profileChannels="profileChannels" :setCurrentChannel="connect" />
        </b-col>
        <b-col md="8">
            <Channel :messages="getMessages" :sendMessage="sendMessage" />
        </b-col>
    </b-row>
  </div>
</template>

<script>
import Profiles from '../components/direct/Profiles.vue'
import Channel from '../components/direct/Channel.vue'
import { 
  mapActions, 
  mapGetters 
  } from 'vuex'


export default {
    components: {
        Channel, Profiles
    },
    data() {
        return {
          
        }
    },
    methods: {
      // ...mapActions({setCurrentChannel: 'setCurrentChannelMessages'}),
      ...mapActions({connect: 'setDirectWebSocketConnect', sendMessage: 'wsSendDirectMessage'})
    },
    computed: {
      ...mapGetters({
        profileChannels: 'getProfileChannels',
        //, currentChannel: 'getCurrentChannelMessages'
        getMessages: 'wsGetDirectMessages'
        })
    }
}
</script>

<style>

</style>