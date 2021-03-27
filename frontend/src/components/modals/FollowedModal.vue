<template>
    <div>
        <b-modal id="modal-followed-list" scrollable title="Takip Edilenler">
            <p v-for="followed in followeds" :key="followed.followed_id__user__username">
                {{followed.follower_id__user__username}}
            </p>
        </b-modal>
    </div>
</template>

<script>
export default {
    props: ['followeds']
}
</script>

<style>

</style>