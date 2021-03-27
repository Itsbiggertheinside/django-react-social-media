<template>
    <div id="profile">
        <h3>Profil</h3>
        <Information 
            :username="profile.get_username" 
            :name="profile.name" 
            :picture="profile.picture"
            :biography="profile.biography" 
            :webpage="profile.webpage"
            :posts="profile.posts"
        />

        <Content :posts="profile.posts" />
    </div>
</template>

<script>
import Information from "../components/profile/Information.vue"
import Content from "../components/profile/Content.vue"
import { mapGetters } from 'vuex'

export default {
    components: { 
        Information, Content
    },
    computed: {
        ...mapGetters({profile: 'getProfile'})
    }
}
</script>

<style>

</style>