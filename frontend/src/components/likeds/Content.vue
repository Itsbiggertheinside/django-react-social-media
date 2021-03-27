<template>
    <b-card-group columns class="my-4">
        <b-card v-for="post in followedsPosts" :key="post.slug" :img-src="post.image" img-top>
            <footer class="post-body">
                <div class="post-footer">
                    <div>
                        <b-avatar :src="post.owner.picture" size="1.7rem"></b-avatar>
                        <span class="ml-2 profile-username">{{post.owner.username}}</span>
                    </div>
                    <div class="post-actions">
                        <div class="likes d-inline">
                            <b-button variant="outline-light" @click="likePost(post.slug)"><b-avatar class="mr-1 align-top" variant="light" src="https://img.icons8.com/ios/24/000000/like--v1.png" size="1.4rem"></b-avatar><span>{{post.likes_set.length}}</span></b-button>
                        </div>
                        <div class="comments d-inline">
                            <b-button variant="outline-light"><b-avatar class="mr-1 align-top" variant="light" src="https://img.icons8.com/ios/24/000000/topic.png" size="1.4rem"></b-avatar><span>{{post.comment_set.length}}</span></b-button>
                        </div>
                    </div>
                </div>
                <div class="post-content my-2">
                    <p>{{post.content.substring(0, 45)}} ...</p>
                </div>
            </footer>
        </b-card>
    </b-card-group>
</template>

<script>
export default {

}
</script>

<style>

</style>