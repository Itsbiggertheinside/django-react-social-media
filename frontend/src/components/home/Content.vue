<template>
    <div>
        <h3>Gönderiler</h3>
        <b-card-group columns class="my-4" :key="componentKey">
            <div v-for="followeds in followedsPosts" :key="followeds.slug">
                <b-card v-for="post in followeds.followed.posts" :key="post.slug">
                    <b-card-img @click="goDetailPage(post.slug)" :src="post.image" class="mb-2"></b-card-img>
                    <footer class="post-body">
                        <div class="post-footer">
                            <div>
                                <b-avatar :src="post.owner.picture" size="1.7rem"></b-avatar>
                                <span class="ml-2 profile-username">{{post.owner.username}}</span>
                            </div>
                            <div class="post-actions">
                                <div class="likes d-inline">
                                    <b-button variant="outline-light" @click="likePost({post_slug: post.slug}); forceRerender()"><b-avatar class="mr-1 align-top" variant="light" src="https://img.icons8.com/ios/24/000000/like--v1.png" size="1.4rem"></b-avatar><span>{{post.likes_set.length}}</span></b-button>
                                </div>
                                <div class="comments d-inline">
                                    <b-button variant="outline-light"><b-avatar class="mr-1 align-top" variant="light" src="https://img.icons8.com/ios/24/000000/topic.png" size="1.4rem"></b-avatar><span>{{post.comment_set.length}}</span></b-button>
                                </div>
                            </div>
                        </div>
                        <div class="post-content my-2">
                            <p>{{post.content.substring(0, 75)}} ...</p>
                        </div>
                    </footer>
                </b-card>
            </div>
        </b-card-group>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    methods: {
        ...mapActions(
            {likePost: 'setLikedPost'}
        ),
        goDetailPage(slug) {
            this.$router.push('/detail/' + slug)
        },
        makeToast(username) {
            this.$bvToast.toast(`@${username} tarafından paylaşılan bir gönderiyi beğendin!`, {
                title: '❤',
                solid: true
            })
        },
        handleLikeCount() {
            console.log('test')
        },
        forceRerender() {
            this.componentKey += 1;
            this.updateCount = 0;
        }
    },
    data: () => ({
        currentUser: sessionStorage.getItem('username'),
        updateCount: 0,
        componentKey: 0
    }),
    updated() {
        if(this.updateCount < 1) {
            this.$store.dispatch('setFollowedsPosts')
            this.updateCount += 1
        }
    },
    computed: {
        ...mapGetters({followedsPosts: 'getFollowedsPosts', likedPosts: 'getLikedPost'})
    },
}
</script>

<style scoped>
    img {
        width: 100%;
        min-height: 300px;
        max-height: 500px;
        border-radius: 1rem;
        filter: drop-shadow(.1rem .1rem .3rem rgb(192, 192, 192));
        object-fit: cover;
        object-position: center;
    }
</style>