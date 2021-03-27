<template>
    <main id='settings'>
        <h3>Ayarlar</h3>
        <b-row class="my-4">
            <b-col md="3">
                <Fields />
            </b-col>
            <b-col md="9">
                <ProfileSettings />
                <ChangePassword />
            </b-col>
        </b-row>
    </main>
</template>

<script>
import Fields from '../components/settings/Fields.vue'
import ProfileSettings from '../components/settings/sections/ProfileSettings.vue'
import ChangePassword from '../components/settings/sections/ChangePassword.vue'

export default {
    components: {
        Fields,
        ProfileSettings,
        ChangePassword
    }
}
</script>

<style>

</style>