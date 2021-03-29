<template>
    <b-nav vertical>
        <b-nav-item v-for="followed in followingList[0].followeds" :key="followed.id">
            <b-avatar class="mr-3 align-top" variant="light" :src="followed.picture" size="1.8rem"></b-avatar>
            <span>{{followed.username}}</span>
        </b-nav-item>
    </b-nav>
</template>

<script>
export default {
    props: ['followingList']
}
</script>

<style>

</style>