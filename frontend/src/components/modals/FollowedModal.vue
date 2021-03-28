<template>
    <div>
        <b-modal id="modal-followed-list" scrollable title="Takip Edilenler">
            <b-nav vertical>
                <b-nav-item v-for="followed in followeds" :key="followed.id">
                    <b-avatar class="mr-1 align-top" variant="light" :src="followed.picture" size="1.4rem"></b-avatar>
                    <span>{{followed.username}}</span>
                </b-nav-item>
            </b-nav>
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