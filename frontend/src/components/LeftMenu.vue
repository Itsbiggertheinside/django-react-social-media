<template>
    <div class="side-nav d-none d-lg-block">
        <b-nav vertical>
            <b-navbar-brand class="mx-4 mt-3">Social Network</b-navbar-brand>
            <div id="profile-informations" class="text-center mt-5">
                <b-avatar variant="primary" src="https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8cHJvZmlsZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&w=1000&q=80" size="6rem" ></b-avatar>
                <p class="font-weight-bolder h4 mt-3">Tufan Kılınç</p>
                <p class="text-muted h6">@{{profile.get_username}}</p>
                <b-row class="mt-4">
                    <b-col md="4">
                        <p class="font-weight-bolder h6">{{profile.posts.length}}</p>
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
            <div id="side-nav-menu">
                <router-link tag="b-nav-item" to="/" exact>
                    <img src="https://img.icons8.com/ios/24/000000/home--v1.png"/><span>Ana Sayfa</span>
                </router-link>
                <router-link tag="b-nav-item" to="/explore">
                    <img src="https://img.icons8.com/ios/24/000000/compass--v1.png"/><span>Keşfet</span>
                </router-link>
                <router-link tag="b-nav-item" to="/profile">
                    <img src="https://img.icons8.com/ios/24/000000/user-male-circle.png"/><span>Profil</span>
                </router-link>
                <router-link tag="b-nav-item" to="/notifications">
                    <img src="https://img.icons8.com/ios/24/000000/appointment-reminders--v1.png"/><span>Bildirimler</span>
                </router-link>
                <router-link tag="b-nav-item" to="/likeds">
                    <img src="https://img.icons8.com/ios/24/000000/appointment-reminders--v1.png"/><span>Beğenilenler</span>
                </router-link>
                <router-link tag="b-nav-item" to="/direct">
                    <img src="https://img.icons8.com/ios/24/000000/chat-message--v1.png"/><span>Mesajlar</span>
                </router-link>
                <router-link tag="b-nav-item" to="/settings">
                    <img src="https://img.icons8.com/ios/24/000000/settings--v1.png"/><span>Ayarlar</span>
                </router-link>
                <b-dropdown-divider></b-dropdown-divider>
                <router-link tag="b-nav-item" to="/logout">
                    <img src="https://img.icons8.com/ios/24/000000/shutdown--v1.png"/><span>Çıkış Yap</span>
                </router-link>
            </div>
        </b-nav>
        <follower-modal @click="setFollowingList()" :followers="followers"></follower-modal>
        <followed-modal @click="setFollowingList()" :followeds="followeds"></followed-modal>
    </div>
</template>

<script>
import FollowerModal from './modals/FollowerModal.vue'
import FollowedModal from './modals/FollowedModal.vue'
import { mapGetters } from 'vuex'

export default {
    data() {
        return {
            followers: [],
            followeds: []
        }
    },
    components: {
        FollowerModal, FollowedModal
    },
    computed: {
      ...mapGetters({profile: 'getProfile', followingList: 'getFollowingList'})
    },
    beforeMounted() {
        this.followers = this.followingList[0].followers,
        this.followeds = this.followingList[0].followeds
    }
}
</script>

<style scoped>
    .side-nav {
        height: 100%;
    }

    #side-nav-menu span {
        padding-left: 1rem;
        padding-right: 1rem;
    }
</style>
