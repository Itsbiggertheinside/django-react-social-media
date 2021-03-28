import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/profile",
    name: "Profile",
    
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Profile.vue")
  },
  {
    path: "/explore",
    name: "Explore",
    
    component: () =>
      import(/* webpackChunkName: "explore" */ "../views/Explore.vue")
  },
  {
    path: "/direct",
    name: "Direct",
    
    component: () =>
      import(/* webpackChunkName: "direct" */ "../views/Direct.vue")
  },
  {
    path: "/likeds",
    name: "Likeds",
    
    component: () =>
      import(/* webpackChunkName: "likeds" */ "../views/Likeds.vue")
  },
  {
    path: "/settings",
    name: "Settings",
    children: [
      {
        path: 'profile',
        component: () =>
          import(/* webpackChunkName: "profileSettings" */ "../components/settings/sections/ProfileSettings.vue")
      },
      {
        path: 'password',
        component: () =>
          import(/* webpackChunkName: "changePasswordSettings" */ "../components/settings/sections/ChangePassword.vue")
      },
      {
        path: 'blockeds',
        component: () =>
          import(/* webpackChunkName: "blockedUsersSettings" */ "../components/settings/sections/Blocked.vue")
      }
    ],

    
    component: () =>
      import(/* webpackChunkName: "settings" */ "../views/Settings.vue")
  },
  {
    path: "/detail/:slug",
    name: "Detail",
    
    component: () =>
      import(/* webpackChunkName: "detail" */ "../views/Detail.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
