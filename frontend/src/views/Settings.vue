<template>
    <main id='settings'>
        <h3>Ayarlar</h3>
        <b-row class="my-4">
            <b-col md="3">
                <Fields />
            </b-col>
            <b-col md="9">
                <router-view></router-view>
            </b-col>
        </b-row>
    </main>
</template>

<script>
import Fields from '../components/settings/Fields.vue'

export default {
    components: {
        Fields
    }
}
</script>

<style>

</style>