<template>
    <div class="my-4">
        <b-card-group columns class="my-4">
            <b-card v-for="post in posts" :key="post.slug" @click="likePost({post_slug: post.slug})" :img-src="post.image" img-top></b-card>
        </b-card-group>
        <b-button @click="setAuthToken({email: 'tufankilinc@outlook.com', password: 'admin'})">Giriş Yap</b-button>
        <b-button @click="setAuthenticatedUser()">Get Current User</b-button>
        <p>{{token}}</p>
        <p>{{authenticatedUser}}</p>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  props: ['posts'],
  methods: {
    ...mapActions(
      {likePost: 'setLikedPost', setAuthToken: 'setAuthToken', setAuthenticatedUser: 'setAuthenticatedUser'}
    ),
    makeToast(username) {
      this.$bvToast.toast(`@${username} tarafından paylaşılan bir gönderiyi beğendin!`, {
        title: '❤',
        solid: true
      })
    }
  },
  computed: {
    ...mapGetters({likedPosts: 'getLikedPost', token: 'getAuthToken', authenticatedUser: 'getAuthenticatedUser'})
  }
}
</script>

<style scoped>
    img {
        width: 100%;
        height: 350px;
        border-radius: .3rem;
        filter: drop-shadow(.1rem .1rem .3rem rgb(192, 192, 192));
        object-fit: cover;
        object-position: center;
    }
</style>