<template>
    <div>
        <b-modal id="modal-follower-list" scrollable title="Takipçiler">
            <p v-for="follower in followers" :key="follower.followed_id__user__username">
                {{follower.follower_id__user__username}}
            </p>
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