<template>
    <div class="my-4">
        <b-card-group columns class="my-4">
            <b-card v-for="post in posts" :key="post.slug">
              <b-card-img @click="goDetailPage(post.slug)" :src="post.image"></b-card-img>
            </b-card>
        </b-card-group>
    </div>
</template>

<script>
export default {
  props: ['posts'],
  methods: {
    goDetailPage(slug) {
      this.$router.push('/detail/' + slug)
    },
    makeToast(username) {
      this.$bvToast.toast(`@${username} tarafından paylaşılan bir gönderiyi beğendin!`, {
        title: '❤',
        solid: true
      })
    }
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