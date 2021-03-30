<template>
    <b-row>
        <b-col sm="12">
            <b-card border="dark" id="channelMessageContainer">
                <b-card-body>
                    <b-row>
                        <b-container>
                            <b-col v-for="message in messages" :key="message.id" sm="12" class="mb-2 py-1 pl-1 pr-2 message">
                                <b-avatar class="mr-2 align-top" variant="light" :src="message.picture" size="1.5rem"></b-avatar>
                                <span>{{message.message}}</span>
                            </b-col>
                        </b-container>
                    </b-row>
                </b-card-body>
            </b-card>
        </b-col>
        <b-col sm="12">
            <b-input-group id="channelSendMessagePanel">
                <b-form-input type="text" v-model="message" placeholder="Mesajınız"></b-form-input>

                <b-input-group-append>
                    <b-button @click="sendMessage({directChannelCode: channelCode, directMessage: message}); reRenderer(channelCode)" variant="outline-info">Gönder</b-button>
                </b-input-group-append>
            </b-input-group>
        </b-col>
    </b-row>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    props: ['channelCode', 'messages', 'reRenderer'],
    methods: {
        ...mapActions({sendMessage: 'setSendDirectMessage'})
    },
    data() {
        return {
            message: ''
        }
    }
}
</script>

<style scoped>
    #channelMessageContainer {
        height: 73vh;
        overflow-y: scroll;
        overflow-x: hidden;
        scroll-behavior: smooth;
    }

    #channelSendMessagePanel {
        margin-top: 1.5rem;
    }

    .message {
        width: fit-content;
        border-radius: 1rem;
        border: 1px solid #579b9b3b;
        font-weight: 500;
    }
</style>