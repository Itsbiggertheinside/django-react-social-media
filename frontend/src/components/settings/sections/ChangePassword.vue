<template>
    <div>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Eski Şifren: " label-for="input-oldpassword">
            <b-form-input v-model="passwordData.old_password" type="password" id="input-oldpassword"></b-form-input>
        </b-form-group>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Yeni Şifre: " label-for="input-newpassword">
            <b-form-input v-model="passwordData.new_password1" type="password" id="input-newpassword"></b-form-input>
        </b-form-group>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Yeni Şifre Tekrarı: " label-for="input-newpassword2">
            <b-form-input v-model="passwordData.new_password2" type="password" id="input-newpassword2"></b-form-input>
        </b-form-group>
        <b-form-group class="my-5 text-right">
            <b-button @click="setChangePassword({passwords: passwordData})" variant="light">Kaydet</b-button>
        </b-form-group>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'


export default {
    data() {
        return {
            passwordData: {
                old_password: '',
                new_password1: '',
                new_password2: '',
            }
        }
    },
    methods: {
        ...mapActions({setChangePassword: 'setChangePassword'})
    },
    computed: {
        ...mapGetters({getChangePassword: 'getChangePassword'})
    }
}
</script>

<style>

</style>