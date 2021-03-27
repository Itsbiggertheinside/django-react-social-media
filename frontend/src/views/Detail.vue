<template>
    <div id="detail">
        <b-row>
            <b-col md="7">
                <PostImage :post="detail" />
            </b-col>
            <b-col md="5">
                <PostContent :info="detail" />
            </b-col>
        </b-row>
    </div>
</template>

<script>
import PostImage from '../components/detail/PostImage.vue'
import PostContent from '../components/detail/PostContent.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
    components: {
        PostImage, PostContent
    },
    methods: {
        ...mapActions({getDetail: 'setPostDetail'})
    },
    data() {
        return {
            postSlug: this.$route.params.slug
        }
    },
    computed: {
        ...mapGetters({detail: 'getPostDetail'})
    },
    mounted() {
        this.getDetail(this.postSlug)
    }
}
</script>

<style>

</style>