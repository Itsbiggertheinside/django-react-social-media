<template>
    <div>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Eski Şifren: " label-for="input-oldpassword">
            <b-form-input type="password" id="input-oldpassword"></b-form-input>
        </b-form-group>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Yeni Şifre: " label-for="input-newpassword">
            <b-form-input type="password" id="input-newpassword"></b-form-input>
        </b-form-group>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Yeni Şifre Tekrarı: " label-for="input-newpassword2">
            <b-form-input type="password" id="input-newpassword2"></b-form-input>
        </b-form-group>
        <b-form-group class="my-5 text-right">
            <b-button variant="light">Kaydet</b-button>
        </b-form-group>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>