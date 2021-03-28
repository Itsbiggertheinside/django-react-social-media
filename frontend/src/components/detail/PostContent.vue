<template>
    <div>
        <div>
            <b-avatar :src="info.owner.picture" size="1.7rem"></b-avatar>
            <span class="ml-2 profile-username">{{info.owner.username}}</span>
            <p class="mt-5 mb-4">{{info.content}}</p>
        </div>
        <b-input-group>
            <b-form-input v-model="commentData.content" required></b-form-input>
            <b-input-group-append>
                <b-button variant="info" @click="sendComment({post_slug: info.slug, content: commentData.content}); forceRerender()">Yorum Yap</b-button>
            </b-input-group-append>
        </b-input-group>
        <div  class="my-4">
            <Comments :key="componentKey" :comments="info.comment_set" />
        </div>
    </div>
</template>

<script>
import Comments from './Comments.vue'
import { mapActions } from 'vuex'

export default {
    props: ['info'],
    components: {
        Comments
    },
    methods: {
        ...mapActions({sendComment: 'setComments'}),
        forceRerender() {
            this.componentKey += 1;
            this.updateCount = 0;
        }
    },
    data() {
        return {
            commentData: {
                content: ''
            },
            updateCount: 0,
            componentKey: 0
        }
    },
    updated() {
        if(this.updateCount < 1) {
            this.$store.dispatch('setComments')
            this.updateCount += 1
        }
    }
}
</script>

<style>

</style>