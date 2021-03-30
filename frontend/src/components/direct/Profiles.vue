<template>
    <b-nav vertical>
        <h5 class="mb-2">Son Mesajlaştığın Kişiler</h5>
        <b-nav-item v-for="room in profileChannels" :key="room.id" @click="setCurrentChannel(room.id)">
            <b-avatar class="mr-3 align-center" variant="light" :src="room.creater_info.picture" size="2rem"></b-avatar>
            <span class="text-bold">{{room.creater_info.username}}</span>
        </b-nav-item>
    </b-nav>
</template>

<script>
export default {
    props: ['profileChannels', 'setCurrentChannel']
}
</script>

<style>

</style>