<template>
    <div id="app">
        <header id="nav">
            <!-- <Navbar /> -->
        </header>
        <main id="main">
          <b-container fluid>
            <b-row>
              <b-col lg="3" xl="2" class="left-menu">
                <LeftMenu />
              </b-col>
              <b-col lg="9" xl="10" class="main-content">
                <Navbar />
                <b-container class="mt-4">
                  <router-view />
                </b-container>
              </b-col>
            </b-row>
        </b-container>
      </main>
    </div>
</template>

<script>
import Navbar from './components/Navbar'
import LeftMenu from './components/LeftMenu';
import { mapActions } from 'vuex'

const username = sessionStorage.getItem('username')
// const profile = sessionStorage.getItem('profile')

export default {
  components: {
    Navbar, 
    LeftMenu
  },
  methods: {
    ...mapActions(['setFollowingList', 'setFollowedsPosts', 'setExplorePosts', 'setProfile', 'setLikedPosts', 'setProfileChannels'])
  },
  mounted() {
    this.setFollowingList(),
    this.setExplorePosts(),
    this.setFollowedsPosts(),
    this.setProfileChannels()
    this.setProfile(username)
  }
};

</script>

<style scoped>

  .left-menu {
    background-color: var(--background_secondary);
  }
  
  .main-content {
    padding-left: 1.5rem;
    padding-right: 1.5rem;
    box-shadow: 1px 1px 3px 3px rgb(192, 192, 192);
  }

</style>