<template>
    <div>
        <b-modal id="modal-follower-list" scrollable title="Takipçiler">
            <b-nav vertical>
                <b-nav-item v-for="follower in followers" :key="follower.id">
                    <b-avatar class="mr-1 align-top" variant="light" :src="follower.picture" size="1.4rem"></b-avatar>
                    <span>{{follower.username}}</span>
                </b-nav-item>
            </b-nav>
        </b-modal>
    </div>
</template>

<script>
export default {
    props: ['followers']
}
</script>

<style>

</style>