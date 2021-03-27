<template>
    <b-row>
        <b-col md="4">
            <div id="profile-informations" class="text-center mt-5">
                <b-avatar variant="primary" :src="picture" size="6rem" ></b-avatar>
                <p class="font-weight-bolder h4 mt-3">{{name}}</p>
                <p class="text-muted h6">@{{username}}</p>
                <b-row class="mt-4">
                    <b-col md="4">
                        <p class="font-weight-bolder h6">{{posts.length}}</p>
                        <p class="text-muted">Gönderi</p>
                    </b-col>
                    <b-col md="4" v-b-modal.modal-follower-list>
                        <p class="font-weight-bolder h6">17</p>
                        <p class="text-muted">Takipçi</p>
                    </b-col>
                    <b-col md="4" v-b-modal.modal-followed-list>
                        <p class="font-weight-bolder h6">213</p>
                        <p class="text-muted">Takip</p>
                    </b-col>
                </b-row>
            </div>
        </b-col>
        <b-col md="8" align-self="center">
            <p class="text-muted h5">Hakkında</p>
            <p>{{biography}}</p>
            <p class="text-muted h5">İnternet Sitesi</p>
            <p>{{webpage}}</p>
        </b-col>
    </b-row>
</template>

<script>
export default {
    props: ['username', 'name', 'picture', 'posts', 'follower', 'followed', 'biography', 'webpage']
}
</script>

<style>

</style>