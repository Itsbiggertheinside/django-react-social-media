<template>
    <div>
        <div class="">
            <b-avatar :src="info.owner.picture" size="1.7rem"></b-avatar>
            <span class="ml-2 profile-username">{{info.owner.username}}</span>
        </div>
        <p class="mt-5 mb-4">{{info.content}}</p>
        <b-input-group>
            <b-form-input></b-form-input>
            <b-input-group-append>
                <b-button variant="info">Yorum Yap</b-button>
            </b-input-group-append>
        </b-input-group>
    </div>
</template>

<script>
export default {
    props: ['info']
}
</script>

<style>

</style>