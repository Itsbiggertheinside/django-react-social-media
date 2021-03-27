import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const url = 'http://127.0.0.1:8000/api/'
const headers = { 'Accept': 'application/json; text/plain', 'Content-Type': 'application/json; text/plain', 'Authorization': `Token ${sessionStorage.getItem('token')}` }


export default new Vuex.Store({

  state: {
    authToken: {},
    authenticatedUser: {},
    followedsPosts: [],
    followingList: [],
    explorePosts: [],
    postDetail: {},
    profile: {},
    likedPost: {}
  },

  mutations: {
    setAuthToken(state, payload) {
      state.authToken = payload
    },
    setAuthenticatedUser(state, payload) {
      state.authenticatedUser = payload
    },
    setFollowingList(state, payload) {
      state.followingList = payload
    },
    setFollowedsPosts(state, payload) {
      state.followedsPosts = payload
    },
    setExplorePosts(state, payload) {
      state.explorePosts = payload
    },
    setProfile(state, payload) {
      state.profile = payload
    },
    setLikedPost(state, payload) {
      state.likedPost = payload
    },
    setPostDetail(state, payload) {
      state.postDetail = payload
    }
  },

  actions: {
    async setAuthToken(state, {email, password}) {
      const authToken = await fetch(`${url}rest-auth/login/`, { 
        method:'POST', 
        headers, 
        body: JSON.stringify({email: email, password: password}) 
      })
      const response = await authToken.json()
      state.commit('setAuthToken', response)
      sessionStorage.removeItem('token')
      sessionStorage.setItem('token', response.key)
    },

    async setAuthenticatedUser(state) {
      const authenticatedUser = await fetch(`${url}rest-auth/user/`, { headers })
      const response = await authenticatedUser.json()
      state.commit('setAuthenticatedUser', response)
      sessionStorage.removeItem('username')
      sessionStorage.removeItem('profile')
      sessionStorage.setItem('username', response.username)
      sessionStorage.setItem('profile', response.profile)
    },

    async setFollowingList(state) {
      const followingList = await fetch(`${url}following/?profile`, { headers })
      const response = await followingList.json()
      state.commit('setFollowingList', response)
    },

    async setFollowedsPosts(state) {
      const followedsPosts = await fetch(`${url}following/`, { headers })
      const response = await followedsPosts.json()
      state.commit('setFollowedsPosts', response)
    },

    async setExplorePosts(state) {
      const explorePosts = await fetch(`${url}`, { headers })
      const response = await explorePosts.json()
      state.commit('setExplorePosts', response)
    },

    async setProfile(state, profile_slug) {
      const profile = await fetch(`${url}profile/${profile_slug}/`, { headers })
      const response = await profile.json()
      state.commit('setProfile', response)
    },

    async setLikedPost(state, {post_slug}) {
      const likedPost = await fetch(`${url}create/like/`, { 
        method: 'POST', 
        headers, 
        body: JSON.stringify({profile: sessionStorage.getItem('profile'), post: post_slug}) 
      })
      const response = await likedPost.json()
      state.commit('setLikedPost', response)
    },

    async setPostDetail(state, post) {
      const postDetail = await fetch(`${url}${post}/`, { headers })
      const response = await postDetail.json()
      state.commit('setPostDetail', response)
    }
  },

  modules: {},

  getters: {
    getAuthToken: state => state.authToken,
    getAuthenticatedUser: state => state.authenticatedUser,
    getFollowingList: state => state.followingList,
    getFollowedsPosts: state => state.followedsPosts,
    getExplorePosts: state => state.explorePosts,
    getProfile: state => state.profile,
    getLikedPost: state => state.likedPost,
    getPostDetail: state => state.postDetail
  }

});
