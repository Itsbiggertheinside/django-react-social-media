<template>
    <div>
        <h3>Gönderiler</h3>
        <b-card-group columns class="my-4">
            <div v-for="followed in followedsPosts" :key="followed.user">
                <b-card v-for="post in followed" :key="post.slug" :img-src="post.image" img-top>
                    <footer class="post-body">
                        <div class="post-footer">
                            <div>
                                <b-avatar size="1.7rem"></b-avatar>
                                <span class="ml-2 profile-username"></span>
                            </div>
                            <div class="post-actions">
                                <div class="likes d-inline">
                                    <b-button variant="outline-light" @click="likePost({post_slug: post.slug})"><b-avatar class="mr-1 align-top" variant="light" src="https://img.icons8.com/ios/24/000000/like--v1.png" size="1.4rem"></b-avatar><span></span></b-button>
                                </div>
                                <div class="comments d-inline">
                                    <b-button variant="outline-light"><b-avatar class="mr-1 align-top" variant="light" src="https://img.icons8.com/ios/24/000000/topic.png" size="1.4rem"></b-avatar><span></span></b-button>
                                </div>
                            </div>
                        </div>
                        <div class="post-content my-2">
                            <p>{{post.content}} ...</p>
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
        makeToast(username) {
        this.$bvToast.toast(`@${username} tarafından paylaşılan bir gönderiyi beğendin!`, {
            title: '❤',
            solid: true
        })
        }
    },
    data: () => ({
        currentUser: sessionStorage.getItem('username')
    }),
    computed: {
        ...mapGetters({followedsPosts: 'getFollowedsPosts', likedPosts: 'getLikedPost'})
    }
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