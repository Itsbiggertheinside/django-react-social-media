<template>
    <div class="my-4">
        <h3>Profil</h3>
        <b-card-group columns class="my-4">
            <b-card img-src="https://media.nature.com/lw800/magazine-assets/d41586-020-02779-3/d41586-020-02779-3_18481780.jpg" img-top></b-card>
            <b-card img-src="https://media.nature.com/lw800/magazine-assets/d41586-020-02779-3/d41586-020-02779-3_18481780.jpg" img-top></b-card>
            <b-card img-src="https://media.nature.com/lw800/magazine-assets/d41586-020-02779-3/d41586-020-02779-3_18481780.jpg" img-top></b-card>
            <b-card img-src="https://media.nature.com/lw800/magazine-assets/d41586-020-02779-3/d41586-020-02779-3_18481780.jpg" img-top></b-card>
            <b-card img-src="https://media.nature.com/lw800/magazine-assets/d41586-020-02779-3/d41586-020-02779-3_18481780.jpg" img-top></b-card>
            <b-card img-src="https://media.nature.com/lw800/magazine-assets/d41586-020-02779-3/d41586-020-02779-3_18481780.jpg" img-top></b-card>
        </b-card-group>
    </div>
</template>

<script>
export default {
    methods: {
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
        height: 300px;
        border-radius: .3rem;
        filter: drop-shadow(.1rem .1rem .3rem rgb(192, 192, 192));
    }
</style>