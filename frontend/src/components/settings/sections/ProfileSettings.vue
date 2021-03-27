<template>
    <div>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Adın: " label-for="input-name">
            <b-form-input id="input-name"></b-form-input>
        </b-form-group>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Hakkında: " label-for="input-biography">
            <b-form-textarea id="input-biography"></b-form-textarea>
        </b-form-group>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="İnternet siten: " label-for="input-webpage">
            <b-form-input id="input-webpage"></b-form-input>
        </b-form-group>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Telefon numaran: " label-for="input-phone">
            <b-form-input id="input-phone" placeholder="05318936592"></b-form-input>
        </b-form-group>
        <b-form-group label-cols-sm="4" label-cols-lg="2" content-cols-sm content-cols-lg="10" label="Cinsiyetin: " label-for="input-gender">
            <b-form-select id="input-gender" :options="[{value: 'M', text: 'Erkek'}, {value: 'F', text: 'Kadın'}, {value: 'U', text: 'Bilinmiyor'}]"></b-form-select>
        </b-form-group>
        <b-form-group class="my-5">
            <b-form-checkbox v-model="is_hidden" name="check-button" switch>
                Hesabını gizliye al
            </b-form-checkbox>
        </b-form-group>
        <b-form-group class="text-right">
            <b-button variant="light">Kaydet</b-button>
        </b-form-group>
    </div>
</template>

<script>
export default {
    data() {
      return {
        is_hidden: false
      }
    }
}
</script>

<style>

</style>