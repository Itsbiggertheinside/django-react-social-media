<template>
    <div :key="componentKey">
        <b-card :img-src="post.image" img-top>
            <footer class="post-body">
                <div class="post-footer">
                    <div class="post-actions">
                        <div class="likes d-inline">
                            <b-button variant="outline-light" @click="likePost({post_slug: post.slug}); forceRerender()"><b-avatar class="mr-1 align-top" variant="light" src="https://img.icons8.com/ios/24/000000/like--v1.png" size="1.4rem"></b-avatar><span>{{post.likes_set.length}}</span></b-button>
                        </div>
                        <div class="comments d-inline">
                            <b-button variant="outline-light"><b-avatar class="mr-1 align-top" variant="light" src="https://img.icons8.com/ios/24/000000/topic.png" size="1.4rem"></b-avatar><span>{{post.comment_set.length}}</span></b-button>
                        </div>
                    </div>
                </div>
            </footer>
        </b-card>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    props: ['post'],
    methods: {
        ...mapActions({likePost: 'setLikedPost'}),
        forceRerender() {
            this.componentKey += 1;
            this.updateCount = 0;
        }
    },
    data() {
        return {
            updateCount: 0,
            componentKey: 0
        }
    },
    updated() {
        if(this.updateCount < 1) {
            this.$store.dispatch('setPostDetail', this.$route.params.slug)
            this.updateCount += 1
        }
    },
}
</script>

<style>

</style>