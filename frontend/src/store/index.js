import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const url = 'http://127.0.0.1:8000/api/'
const headers = { 'Accept': 'application/json; text/plain; multipart/form-data; image/jpeg; image/png;', 'Content-Type': 'application/json; text/plain; multipart/form-data; image/jpeg; image/png;', 'Authorization': `Token ${sessionStorage.getItem('token')}` }


export default new Vuex.Store({

  state: {
    authToken: {},
    authenticatedUser: {},
    changePassword: {},
    profileSettings: {},
    followedsPosts: [],
    followingList: [],
    explorePosts: [],
    postDetail: {},
    sendPost: {},
    profile: {},
    likedPost: {},
    comments: [],
    profileChannels: [],
    currentChannelMessages: [],
    sendDirectMessage: {},
  },

  mutations: {
    setAuthToken(state, payload) {
      state.authToken = payload
    },
    setAuthenticatedUser(state, payload) {
      state.authenticatedUser = payload
    },
    setChangePassword(state, payload) {
      state.changePassword = payload
    },
    setProfileSettings(state, payload) {
      state.profileSettings = payload
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
    setProfileChannels(state, payload) {
      state.profileChannels = payload
    },
    setCurrentChannelMessages(state, payload) {
      state.currentChannelMessages = payload
    },
    setSendDirectMessage(state, payload) {
      state.sendDirectMessage = payload
    },
    setLikedPost(state, payload) {
      state.likedPost = payload
    },
    setComments(state, payload) {
      state.comments.push(payload)
    },
    setSendPost(state, payload) {
      state.sendPost = payload
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

    async setChangePassword(state, {passwords}) {
      const changePassword = await fetch(`${url}rest-auth/password/change/`, { 
        method: 'POST', 
        headers, 
        body: JSON.stringify({ new_password1: passwords.new_password1, new_password2: passwords.new_password2, old_password: passwords.old_password }) 
      })
      const response = await changePassword.json()
      state.commit('setChangePassword', response)
    },

    async setProfileSettings(state, {username, settings}) {
      const profileSettings = await fetch(`${url}update-profile/${username}/`, { 
        method: 'PUT', 
        headers, 
        body: JSON.stringify({name: settings.name, biography: settings.biography, webpage: settings.webpage, phone: settings.phone, gender: settings.gender, is_hidden: settings.is_hidden}) 
      })
      const response = await profileSettings.json()
      state.commit('setProfileSettings', response)
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
      const explorePosts = await fetch(`${url}post/`, { headers })
      const response = await explorePosts.json()
      state.commit('setExplorePosts', response)
    },

    async setProfile(state, profile_slug) {
      const profile = await fetch(`${url}profile/${profile_slug}/`, { headers })
      const response = await profile.json()
      state.commit('setProfile', response)
    },

    async setProfileChannels(state) {
      const profileChannels = await fetch(`${url}direct/channel/`, { headers })
      const response = await profileChannels.json()
      state.commit('setProfileChannels', response)
    },

    async setCurrentChannelMessages(state, directChannelCode) {
      const currentChannelMessages = await fetch(`${url}direct/channel/${directChannelCode}/`, { headers })
      const response = await currentChannelMessages.json()
      state.commit('setCurrentChannelMessages', response)
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

    async setSendPost(state, {post}) {
      const sendPost = await fetch(`${url}post/`, { 
        method: 'POST', 
        headers, 
        body: JSON.stringify({ profile: sessionStorage.getItem('profile'), content: post.content, image: post.image, slug: 'asjkdahskhd2hdk3' }) 
      })
      const response = await sendPost.json()
      state.commit('setSendPost', response)
    },

    async setSendDirectMessage(state, {directChannelCode, directMessage}) {
      const sendDirectMessage = await fetch(`${url}direct/message/`, { 
        method: 'POST', 
        headers, 
        body: JSON.stringify({ sender: sessionStorage.getItem('profile'), room: directChannelCode, message: directMessage }) 
      })
      const response = await sendDirectMessage.json()
      state.commit('setSendDirectMessage', response)
    },

    async setComments(state, {post_slug, content}) {
      const comments = await fetch(`${url}comment-create/${post_slug}/`, { 
        method: 'POST', 
        headers, 
        body: JSON.stringify({profile: sessionStorage.getItem('profile'), post: post_slug, content: content}) 
      })
      const response = await comments.json()
      state.commit('setComments', response)
    },

    async setPostDetail(state, post) {
      const postDetail = await fetch(`${url}post/${post}/`, { headers })
      const response = await postDetail.json()
      state.commit('setPostDetail', response)
    }
  },

  modules: {},

  getters: {
    getAuthToken: state => state.authToken,
    getAuthenticatedUser: state => state.authenticatedUser,
    getChangePassword: state => state.getChangePassword,
    getProfileSettings: state => state.profileSettings,
    getFollowingList: state => state.followingList,
    getFollowedsPosts: state => state.followedsPosts,
    getExplorePosts: state => state.explorePosts,
    getProfile: state => state.profile,
    getProfileChannels: state => state.profileChannels,
    getCurrentChannelMessages: state => state.currentChannelMessages,
    getSendDirectMessage: state => state.sendDirectMessage,
    getLikedPost: state => state.likedPost,
    getSendPost: state => state.sendPost,
    getPostDetail: state => state.postDetail,
    getComments: state => state.comments
  }

});
