<template>
    <div>
        <b-list-group>
            <router-link to="/settings/profile" custom v-slot="{ navigate }">
                <b-list-group-item button @click="navigate" @keypress.enter="navigate" role="link">Profil Ayarları</b-list-group-item>
            </router-link>
            <router-link to="/settings/password" custom v-slot="{ navigate }">
                <b-list-group-item button @click="navigate" @keypress.enter="navigate" role="link">Şifreni Değiştir</b-list-group-item>
            </router-link>
            <router-link to="/settings/blockeds" custom v-slot="{ navigate }">
                <b-list-group-item button @click="navigate" @keypress.enter="navigate" role="link">Engellenenler</b-list-group-item>
            </router-link>
        </b-list-group>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>